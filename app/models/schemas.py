from pydantic import BaseModel, Field


# schema pydantic creation du user
class UserCreate(BaseModel):
    username : str
    password : str
    email : str


class UserVerify(BaseModel):
    username : str
    password : str


class UserResponse(UserCreate):
    id : int



# schema pydantic d'entre du model de ml

class RHRequest(BaseModel):
    Gender: str
    Age: int 

    Department: str
    JobRole: str

    MonthlyIncome: int 
    YearsAtCompany: int 

    JobSatisfaction: int 
    WorkLifeBalance: int 
    OverTime: str
    BusinessTravel: str

    Education: int 
    EducationField: str

    EnvironmentSatisfaction: int 
    JobInvolvement: int 

    JobLevel: int 
    MaritalStatus: str

    PercentSalaryHike: int 
    PerformanceRating: int 

    RelationshipSatisfaction: int 

    StockOptionLevel: int 
    TotalWorkingYears: int 
    YearsInCurrentRole: int 
    YearsWithCurrManager: int 

# schema pydantic de la sortie du model de ml

class output_ml(BaseModel):
    churn_probability: float  
    prediction: str



# schema pydantic de la sortie du model de gemini 

class output_gemini(BaseModel):
    retention_plan : list 