import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("sales.csv")

# Convert date column
data['Date'] = pd.to_datetime(data['Date'])

# Create numeric index
data['Day'] = range(len(data))

# Prepare data
X = data[['Day']]
y = data['Sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 5 days
future_days = [[len(data)+i] for i in range(5)]
predictions = model.predict(future_days)

print("Future Predictions:", predictions)

# Plot graph
# Plot graph
plt.figure(figsize=(8,5))   # ✅ ADD HERE (first line)

plt.plot(data['Sales'], label='Actual Sales')
plt.plot(range(len(data), len(data)+5), predictions, label='Predicted Sales')

plt.legend()
plt.title("Demand Prediction")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.grid(True)   # ✅ ADD HERE (before show)

plt.show()