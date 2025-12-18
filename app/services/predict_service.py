import joblib
import pandas as pd

model = joblib.load("ML/logistic_regression.pkl")
# print(model.classes_)
def predict_probability(data):

    df =  pd.DataFrame([data.dict()])
    
    return model.predict_proba(df)[0][1]

# risque eleve
# {
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

