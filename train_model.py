# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load the dataset
data = pd.read_csv('data/historical_data.csv')

# Preprocess the data
data.dropna(inplace=True)

# Define feature columns and target column
feature_columns = [
    "Threat Level", "Vulnerability Level", "Impact Level", "Environmental Data", "Health Data", "Vehicle Data",
    "Heart Rate", "Blood Pressure Systolic", "Blood Pressure Diastolic", "SpO2", "Body Temperature", "Respiratory Rate",
    "Latitude", "Longitude", "Crowd Density", "Noise Level", "Light Level", "Stress Level",
    "Weather Condition_Clear", "Weather Condition_Rain", "Weather Condition_Snow", "Weather Condition_Fog", 
    "Weather Condition_Storm", "Time of Day_Morning", "Time of Day_Afternoon", 
    "Time of Day_Evening", "Time of Day_Night", "Day of Week_Monday", "Day of Week_Tuesday", 
    "Day of Week_Wednesday", "Day of Week_Thursday", "Day of Week_Friday", "Day of Week_Saturday", "Day of Week_Sunday"
]

# Define target column
target_column = 'Threat Detected'

X = data[feature_columns]
y = data[target_column]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/threat_detection_model.pkl')
