# FastAPI ML Wrapper

A simple FastAPI-based API wrapper for a scikit-learn house price prediction model.

## Run Locally

```bash
uvicorn main:app --reload
```

## Test
Visit:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

Request:
```aiignore
{
  "square_feet": 1200,
  "bedrooms": 2,
  "bathrooms": 1.75,
  "year_built": 2020

```

Response:
```aiignore
{
  "predicted_price": 220000.0
}

```