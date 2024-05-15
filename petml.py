import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Load the CSV data
def load_csv():
    data = pd.read_csv('fake_animals.csv')
    return data

data = load_csv()
# Step 2: Handle missing values
data.fillna(0, inplace=True)  # Replace NaN values with 0 (or choose a different strategy)

# Step 3: Split the data into features (X) and target variable (y)
X = data[['age','weight','affection','appetite', 'vaccinated','injury','wound']].values
y = data['overall_health'].values

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Take input from the user
affection = int(input("Enter affection level (1 - 10): "))
vaccinated = int(input("Enter vaccination status (0/1): "))
age = int(input("Enter age (1 - 15): "))
weight = float(input("Enter weight (1 - 50): "))
appetite = float(input("Enter appetite level (1 - 10): "))
injury = int(input("Enter injury status(0/1): "))
wound = int(input("Enter if there is any wound (0/1): "))

# Step 6: Predict the overall health based on user input
user_input = np.array([[age,weight,affection,appetite,vaccinated,injury,wound]])
print(user_input['age'])
prediction = model.predict(user_input)
#prediction = np.maximum(0.0000, np.minimum(100.0000, prediction))
#prediction_clipped = np.clip(prediction, 0, 100) 
print("Predicted overall health percentage:",prediction[0])
