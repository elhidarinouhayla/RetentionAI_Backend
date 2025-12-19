from fastapi import FastAPI,HTTPException,Depends
from app.database import Base,engine,get_db
from sqlalchemy.orm import session
from app.models.schemas import UserCreate, UserResponse,  UserVerify, output_ml, RHRequest, output_gemini
from app.models.models import User, Prediction
from .auth import create_token, verify_token, hache_password, verify_password
from app.services.predict_service import predict_probability
from app.services.gemini_service import retention_gemini
from fastapi.middleware.cors import CORSMiddleware
import joblib



app = FastAPI()
Base.metadata.create_all(bind=engine)

model = joblib.load("ML/logistic_regression.pkl")


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# creation d'un username :
@app.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db: session=Depends(get_db)):
    exist = db.query(User).filter(User.username == user.username).first()

    if exist:
        raise HTTPException(status_code=400, detail= "username existe deja")
    
    # haching password
    hashed_pwd = hache_password(user.password)
    
    new_user = User(username=user.username, password=hashed_pwd, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# verifier l'identifiant et retourner token
@app.post("/login")
def login(user:UserVerify, db: session=Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username
        ).first()
    
    if not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=400, detail="username or password incorect")
    
    token = create_token(db_user.username)

    return {"token" : token}



#  creation d'endpoint predict en utilisant le modele du ml

@app.post("/predict", response_model=output_ml)
def predict(data: RHRequest, user: dict=Depends(verify_token)):

    risck_level = predict_probability(data)

    if risck_level >= 0.50:
        prediction = "RISCk_ELLEVE"
    else:
        prediction = "RISCK_FAIBLE"

    # ✅ CORRECTION : Utiliser "churn_probability" en minuscule
    return {"churn_probability": float(risck_level),
            "prediction": prediction}




#  creation d'endpoint generate-retention-plan en utilisant le model de gemini

@app.post("/generate_retention_plan", response_model=output_gemini)
def generate_retention_plan(data: RHRequest, user: dict = Depends(verify_token)):

    prediction_result = predict(data, user)

    probability = prediction_result["churn_probability"]
    risck_level = prediction_result["prediction"]

    if risck_level != "RISCk_ELLEVE":
        return {"retention_plan":[ "Aucun plan requis, reteintion faible"]}
    
    else:
        result = retention_gemini(probability, 
                                risck_level)
        return {"retention_plan": result}




