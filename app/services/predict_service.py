import joblib
import pandas as pd

model = joblib.load("ML/logistic_regression.pkl")

def predict_probability(data):

    df =  pd.DataFrame([data.dict()])
    
    return model.predict_proba(df)[0][0]

# test = {
#   "Gender": "Male",
#   "Age": 32,
#   "Department": "Sales",
#   "JobRole": "Sales Executive",
#   "MonthlyIncome": 4500,
#   "YearsAtCompany": 5,
#   "JobSatisfaction": 3,
#   "WorkLifeBalance": 3,
#   "OverTime": "Yes",
#   "BusinessTravel": "Travel_Rarely",
#   "Education": 3,
#   "EducationField": "Marketing",
#   "EnvironmentSatisfaction": 3,
#   "JobInvolvement": 3,
#   "JobLevel": 2,
#   "MaritalStatus": "Single",
#   "PercentSalaryHike": 12,
#   "PerformanceRating": 3,
#   "RelationshipSatisfaction": 3,
#   "StockOptionLevel": 1,
#   "TotalWorkingYears": 8,
#   "YearsInCurrentRole": 3,
#   "YearsWithCurrManager": 2
# }

# print(predict(test))

