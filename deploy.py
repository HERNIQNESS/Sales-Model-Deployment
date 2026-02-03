from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load('sales_reg_model.joblib')
feature_name = joblib.load('model_features.joblib')

app = FastAPI(title = 'Sales Regression Model API')

class SalesFeatures(BaseModel):
    Marketing_Spend: float
    Store_Size: float
    Month_Number: int 
    
@app.get('/')
def root():
    return{'message':'Sales model healthy'}

@app.post('/predict')
def predict_sales(data: SalesFeatures):
    x = np.array([[getattr(data, f)for f in feature_name]])
    prediction = model.predict(x)[0]
    return {'predict_sales': float(prediction)}