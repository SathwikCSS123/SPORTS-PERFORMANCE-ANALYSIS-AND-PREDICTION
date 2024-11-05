import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Constants for the scoring formula
BASE_SCORE = 720  # Starting score before considering angle and wind speed.
OPTIMAL_ANGLE = 45.0  # The ideal angle for the shot.
ANGLE_PENALTY_COEFFICIENT = 0.1  # Penalty per degree deviation from the optimal angle.
WIND_PENALTY_COEFFICIENT = 0.2  # Penalty per unit of wind speed.

# Dataset for archery scores
data = {
    "Rank": list(range(1, 51)),
    "Initial_Angle": [45, 40, 42, 44, 47, 38, 41, 43, 48, 46,
                      39, 41, 44, 42, 47, 45, 40, 43, 46, 38,
                      42, 44, 47, 39, 41, 45, 43, 46, 38, 40,
                      42, 47, 39, 41, 44, 46, 48, 40, 43, 45,
                      47, 42, 39, 44, 41, 48, 46, 45, 43, 38],
    "Wind_Speed": [2, 1, 3, 0, 2, 1, 3, 0, 2, 1,
                   3, 0, 2, 1, 3, 0, 2, 1, 3, 0,
                   2, 1, 3, 0, 2, 1, 3, 0, 2, 1,
                   3, 0, 2, 1, 3, 0, 2, 1, 3, 0,
                   2, 1, 3, 0, 2, 1, 3, 0, 2, 1],
    "Score": [710, 718, 712, 722, 705,
              720, 714, 725, 708, 717,
              723, 711, 719, 713, 726,
              707, 721, 715, 710, 716,
              724, 709, 718, 712, 723,
              704, 721, 714, 726, 708,
              717, 725, 710, 718, 711,
              722, 705, 720, 712, 721,
              708, 714, 726, 709, 717,
              723, 706, 719, 722, 711]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare the data for machine learning
X = df[['Rank', 'Initial_Angle', 'Wind_Speed']]
y = df['Score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

# Function to get prediction for a given rank, initial angle, and wind speed
def predict_score(rank, initial_angle, wind_speed):
    # Calculate the deviation from the optimal angle
    angle_deviation = abs(initial_angle - OPTIMAL_ANGLE)
    # Apply penalties based on angle and wind speed
    predicted_score = BASE_SCORE - (ANGLE_PENALTY_COEFFICIENT * angle_deviation) - (WIND_PENALTY_COEFFICIENT * wind_speed)
    # Ensure the score doesn't drop below 0
    predicted_score = max(predicted_score, 0)
    actual_score = df.loc[df['Rank'] == rank, 'Score'].values[0]
    return predicted_score, actual_score

# Get user input
rank = int(input("Enter the rank (1-50): "))
initial_angle = float(input("Enter the initial angle (degrees): "))
wind_speed = float(input("Enter the wind speed: "))

# Predict the score
predicted_score, actual_score = predict_score(rank, initial_angle, wind_speed)
print(f"Predicted Score: {predicted_score:.2f}")
print(f"Actual Score: {actual_score:.2f}")
