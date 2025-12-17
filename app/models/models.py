from app.database import Base
from sqlalchemy import String, Integer, Column, DateTime
from datetime import datetime



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False )
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    passwordhash = Column(String, nullable=False)
    created_at= Column(DateTime, default= datetime.now )



class Prediction(Base):
    __tablename__="prediction_history"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default= datetime.now )
    user_id = Column(String, nullable=False )
    employee_id = Column(String, nullable=False )
    probability = Column(String)