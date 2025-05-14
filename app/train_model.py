import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('king_county_house_data.csv')
df_params = df[['sqft_living', 'bedrooms', 'bathrooms', 'yr_built']]
df_prices = df['price']

# Dummy training data
X = df_params.to_numpy()
y = df_prices.to_numpy()

model = LinearRegression()
model.fit(X, y)

# Save model to file
joblib.dump(model, "house_price_model.pkl")
