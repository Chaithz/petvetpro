import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the CSV data
def load_csv():
    data = pd.read_csv('datasetanimals.csv')
    return data
data = load_csv()

# Step 2: Handle missing values
def fill_missing_values(data):
    data.fillna(0, inplace=True)  # Replace NaN values with 0 (or choose a different strategy)
    return 

# Step 3: Split the data into features (X) and target variable (y)
def variables():
    X = data[['age','weight','affection','appetite', 'vaccinated','injury','wound']].values
    y = data['overall_health'].values
    return X,y

def train_model():
    model = LinearRegression()
    X,y=variables()
    model.fit(X, y)
    return model

# Step 4: Train the model
# def model_train(X,y):
#     model = LinearRegression()
#     model.fit(X, y)
#     return model
# model=model_train()

# Step 5: Take input from the user
def inputs():
    affection = int(input(" "))
    vaccinated = int(input("Enter vaccination status (0/1): "))
    age = int(input("Enter age (1 - 15): "))
    weight = float(input("Enter weight (1 - 50): "))
    appetite = float(input("Enter appetite level (1 - 10): "))
    injury = int(input("Enter injury status(0/1): "))
    wound = int(input("Enter if there is any wound (0/1): "))
    return affection,vaccinated,age,weight,appetite,injury,wound

# Step 6: Predict the overall health based on user input
def prediction(affection,vaccinated,age,weight,appetite,injury,wound):
    # Convert input values to numeric
    age = float(age)
    weight = float(weight)
    affection = float(affection)
    appetite = float(appetite)

    # Convert categorical data to numeric using LabelEncoder
    le = LabelEncoder()
    vaccinated = le.fit_transform([vaccinated])[0]
    injury = le.fit_transform([injury])[0]
    wound = le.fit_transform([wound])[0]
    user_input = np.array([[age,weight,affection,appetite,vaccinated,injury,wound]])
    model = train_model()
    prediction = model.predict(user_input)
    return prediction[0]

#prediction = np.maximum(0.0000, np.minimum(100.0000, prediction))
#prediction_clipped = np.clip(prediction, 0, 100) 
print("Predicted overall health percentage:",prediction)
