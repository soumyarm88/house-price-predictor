# Use official Python image
FROM python:3.9-slim

# Set workdir
WORKDIR /app

# Copy dependencies and install
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY app/ .

# Expose port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
