from pydantic import BaseModel, Field
from typing import Literal



class UserCreate(BaseModel):
    username : str
    password : str
    email : str


class UserVerify(BaseModel):
    username : str
    password : str


class UserResponse(UserCreate):
    id : int




class RHRequest(BaseModel):
    Gender: str
    Age: int = Field(..., ge=1, le=120)

    Department: str
    JobRole: str

    MonthlyIncome: int = Field(..., ge=0)
    YearsAtCompany: int = Field(..., ge=0)

    JobSatisfaction: int = Field(..., ge=1, le=4)
    WorkLifeBalance: int = Field(..., ge=1, le=4)
    OverTime: str
    BusinessTravel: str

    Education: int = Field(..., ge=1, le=5)
    EducationField: str

    EnvironmentSatisfaction: int = Field(..., ge=1, le=4)
    JobInvolvement: int = Field(..., ge=1, le=4)

    JobLevel: int = Field(..., ge=0)
    MaritalStatus: str

    PercentSalaryHike: int = Field(..., ge=0)
    PerformanceRating: int = Field(..., ge=3, le=4)

    RelationshipSatisfaction: int = Field(..., ge=1, le=4)

    StockOptionLevel: int = Field(..., ge=0)
    TotalWorkingYears: int = Field(..., ge=0)
    YearsInCurrentRole: int = Field(..., ge=0)
    YearsWithCurrManager: int = Field(..., ge=0)

class output_ml(BaseModel):
    Churn_probability : float
    prediction : str