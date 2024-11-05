import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset for ICC Cricket World Cup 2023 points table
data = {
    "Rank": list(range(1, 11)),
    "Country": ["India", "Australia", "England", "New Zealand", "Pakistan",
                "South Africa", "Sri Lanka", "Bangladesh", "West Indies", "Afghanistan"],
    "Points": [18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare the data for machine learning
X = df[['Rank']]
y = df['Points']

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

# Function to predict points for a given rank, matches played, and wins
def predict_points(rank, matches_played, wins):
    print(f"Matches Played: {matches_played}, Wins: {wins}")
    win_percentage = (wins / matches_played) * 100
    predicted_points = model.predict([[rank]])[0]
    actual_points = df.loc[df['Rank'] == rank, 'Points'].values[0]
    return predicted_points, actual_points, win_percentage

# Function to calculate NRR for a single match
def calculate_nrr(runs_scored, balls_faced, runs_conceded, balls_bowled):
    runs_per_ball_scored = runs_scored / balls_faced
    runs_per_ball_conceded = runs_conceded / balls_bowled
    nrr = (runs_per_ball_scored - runs_per_ball_conceded) * 6  # multiplying by 6 to get per over rate
    return nrr

# Get user input
rank = int(input("Enter the rank (1-10): "))
matches_played = int(input("Enter the number of matches played: "))
wins = int(input("Enter the number of wins: "))
runs_scored = int(input("Enter the total runs scored by the team: "))
balls_faced = int(input("Enter the total balls faced by the team: "))
runs_conceded = int(input("Enter the total runs conceded by the team: "))
balls_bowled = int(input("Enter the total balls bowled by the team: "))

# Predict the points
predicted_points, actual_points, win_percentage = predict_points(rank, matches_played, wins)
print(f"Predicted Points: {predicted_points:.2f} points")
print(f"Actual Points: {actual_points:.2f} points")
print(f"Win Percentage: {win_percentage:.2f}%")

# Calculate NRR
nrr = calculate_nrr(runs_scored, balls_faced, runs_conceded, balls_bowled)
print(f"Net Run Rate (NRR) for the match: {nrr:.3f}")
