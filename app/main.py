from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("house_price_model.pkl")

class HouseData(BaseModel):
    square_feet: float
    bedrooms: int
    bathrooms: float
    year_built: int

@app.post("/predict")
def predict_price(data: HouseData):
    input_data = np.array([[data.square_feet, data.bedrooms, data.bathrooms, data.year_built]])
    prediction = model.predict(input_data)
    return {"predicted_price": prediction[0]}
