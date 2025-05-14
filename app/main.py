from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("house_price_model.pkl")

class HouseData(BaseModel):
    square_feet: float

@app.post("/predict")
def predict_price(data: HouseData):
    input_data = np.array([[data.square_feet]])
    prediction = model.predict(input_data)
    return {"predicted_price": prediction[0]}
