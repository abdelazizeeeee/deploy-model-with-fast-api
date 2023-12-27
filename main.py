from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
model_ = joblib.load("/Users/macmini/Desktop/BERT/Salaries_prediction copy.ipynb")



class Features(BaseModel):
    age : str
    gender : str 
    exp : str 
    educ_lvl : str 
    job : str 


@app.post("/")
async def root(features: Features):

    if features.gender == "men":
        features.gender = 1
    else:
        features.gender = 0


    if features.educ_lvl == "Bachelor":
        features.educ_lvl = 0
    elif features.educ_lvl == "High School":
        features.educ_lvl = 1
    elif features.educ_lvl == "Master's":
        features.educ_lvl = 2
    elif features.educ_lvl == "Other":
        features.educ_lvl = 3
    elif features.educ_lvl == "PhD":
        features.educ_lvl = 4
    

    if features.job == "IT":
        features.job = 1
    elif features.job == "Business":
        features.job = 0
    elif features.job == "Manager":
        features.job = 2
    elif features.job == "Marketing":
        features.job = 3
    elif features.job == "Other":
       features.job = 4


    prediction = model_.predict(
                pd.DataFrame(
                    {
                        "Age": [features.age],
                        "Years of Experience": [features.exp],
                        "Gender_encoded": [features.gender],
                        "Education Level_encoded": [features.educ_lvl],
                        "Job Title_encoded": [features.job],
                    }
                )
            )

    return f"The predection of salary is {prediction[0]}"