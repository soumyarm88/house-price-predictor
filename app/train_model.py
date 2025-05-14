import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy training data
X = np.array([[1000], [1500], [2000], [2500], [3000]])  # square feet
y = np.array([100000, 150000, 200000, 250000, 300000])  # price

model = LinearRegression()
model.fit(X, y)

# Save model to file
joblib.dump(model, "house_price_model.pkl")
