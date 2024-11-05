import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset for javelin throw results
data = {
    "Rank": list(range(1, 51)),
    "Athlete": ["Neeraj Chopra", "Jakub Vadlejch", "Vitezslav Vesely", "Julian Weber", "Arshad Nadeem",
                "Aliaksei Katkavets", "Andrian Mardare", "Lassi Etelätalo", "Johannes Vetter", "Pavel Mialeshka",
                "Kim Amb", "Alexandru Mihaita Novac", "Anderson Peters", "Curtis Thompson", "Rocco van Rooyen",
                "Edis Matusevicius", "Keshorn Walcott", "Gatis Cakss", "Julius Yego", "Oliver Helander",
                "Cheng Chao-Tsun", "Magnus Kirt", "Ehab Abdelrahman", "Norbert Rivasz-Toth", "Takuto Kominami",
                "Cyprian Mrzyglod", "Alexandru Novac", "Odei Jainaga", "Ihab Abdelrahman", "Michael Shuey",
                "Kirt Magnus", "Ihsan Özturk", "Mohd Amsyar Azwa", "Hussain Al-Hizam", "Ashraf Amgad Elseify",
                "Luis Rivera", "Mohamed Mohamud", "Samuel Yeboah", "Igor Kachanov", "Pablo Diaz",
                "Marco Fortes", "Michal Deski", "Tomas Stanek", "Ricardo Pineda", "Daniel Stahl",
                "Wojciech Nowicki", "Dmytro Kosynski", "Giovanni Faloci", "Andrea Pilat", "Tanel Laanmäe"],
    "Country": ["IND", "CZE", "CZE", "GER", "PAK", "BLR", "MDA", "FIN", "GER", "BLR",
                "SWE", "ROU", "GRN", "USA", "RSA", "LTU", "TTO", "LAT", "KEN", "FIN",
                "TPE", "EST", "EGY", "HUN", "JPN", "POL", "ROU", "ESP", "EGY", "USA",
                "EST", "TUR", "MAS", "KSA", "QAT", "MEX", "SOM", "GHA", "RUS", "ARG",
                "POR", "POL", "CZE", "VEN", "SWE", "POL", "UKR", "ITA", "SLO", "EST"],
    "Distance (m)": [87.58, 86.67, 85.44, 85.30, 84.62, 83.71, 83.30, 83.28, 82.52, 82.28,
                     79.69, 79.29, 78.60, 78.20, 77.80, 77.40, 77.00, 76.60, 76.20, 75.80,
                     75.40, 75.00, 74.60, 74.20, 73.80, 73.40, 73.00, 72.60, 72.20, 71.80,
                     71.40, 71.00, 70.60, 70.20, 69.80, 69.40, 69.00, 68.60, 68.20, 67.80,
                     67.40, 67.00, 66.60, 66.20, 65.80, 65.40, 65.00, 64.60, 64.20, 63.80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare the data for machine learning
X = df[['Rank']]
y = df['Distance (m)']

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

# Function to get prediction for a given rank, velocity, and angle
def predict_distance(rank, velocity, angle):
    print(f"Initial Velocity: {velocity} m/s, Angle: {angle} degrees")
    time_of_flight = (2 * velocity * math.sin(math.radians(angle))) / 9.81
    predicted_distance = velocity * math.cos(math.radians(angle)) * time_of_flight
    actual_distance = df.loc[df['Rank'] == rank, 'Distance (m)'].values[0]
    return predicted_distance, actual_distance

# Get user input
rank = int(input("Enter the rank (1-50): "))
velocity = float(input("Enter the velocity (m/s): "))
angle = float(input("Enter the angle (degrees): "))

# Predict the distance
predicted_distance, actual_distance = predict_distance(rank, velocity, angle)
print(f"Predicted Distance: {predicted_distance:.2f} meters")
print(f"Actual Distance: {actual_distance:.2f} meters")
