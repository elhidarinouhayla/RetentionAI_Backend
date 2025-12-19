import joblib
import pandas as pd

model = joblib.load("ML/logistic_regression.pkl")
# print(model.classes_)
def predict_probability(data):

    df =  pd.DataFrame([data.dict()])
    
    return model.predict_proba(df)[0][1]

# risque eleve
# {
#   "Gender": "Female",
#   "Age": 26,
#   "Department": "Sales",
#   "JobRole": "Sales Representative",
#   "MonthlyIncome": 2800,
#   "YearsAtCompany": 1,
#   "JobSatisfaction": 1,
#   "WorkLifeBalance": 1,
#   "OverTime": "Yes",
#   "BusinessTravel": "Travel_Frequently",
#   "Education": 2,
#   "EducationField": "Marketing",
#   "EnvironmentSatisfaction": 1,
#   "JobInvolvement": 1,
#   "JobLevel": 1,
#   "MaritalStatus": "Single",
#   "PercentSalaryHike": 11,
#   "PerformanceRating": 3,
#   "RelationshipSatisfaction": 1,
#   "StockOptionLevel": 0,
#   "TotalWorkingYears": 3,
#   "YearsInCurrentRole": 1,
#   "YearsWithCurrManager": 0
# }


# risque faible
# {
#   "Gender": "Female",
#   "Age": 29,
#   "Department": "Research & Development",
#   "JobRole": "Research Scientist",
#   "MonthlyIncome": 5200,
#   "YearsAtCompany": 6,
#   "JobSatisfaction": 4,
#   "WorkLifeBalance": 4,
#   "OverTime": "No",
#   "BusinessTravel": "Travel_Frequently",
#   "Education": 4,
#   "EducationField": "Life Sciences",
#   "EnvironmentSatisfaction": 4,
#   "JobInvolvement": 4,
#   "JobLevel": 2,
#   "MaritalStatus": "Married",
#   "PercentSalaryHike": 15,
#   "PerformanceRating": 4,
#   "RelationshipSatisfaction": 4,
#   "StockOptionLevel": 2,
#   "TotalWorkingYears": 10,
#   "YearsInCurrentRole": 4,
#   "YearsWithCurrManager": 4
# }


# print(predict(test))

