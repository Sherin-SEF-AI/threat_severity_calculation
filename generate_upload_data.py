# generate_upload_data.py
import numpy as np
import pandas as pd

# Function to generate synthetic data for threat severity calculation
def generate_threat_severity_data(num_samples=100):
    data = {
        "Threat Level": np.random.randint(1, 11, num_samples),
        "Vulnerability Level": np.random.randint(1, 11, num_samples),
        "Impact Level": np.random.randint(1, 11, num_samples),
        "Environmental Data": np.random.uniform(0, 100, num_samples),
        "Health Data": np.random.uniform(0, 100, num_samples),
        "Vehicle Data": np.random.uniform(0, 100, num_samples),
        "Heart Rate": np.random.randint(60, 100, num_samples),
        "Blood Pressure Systolic": np.random.randint(90, 140, num_samples),
        "Blood Pressure Diastolic": np.random.randint(60, 90, num_samples),
        "SpO2": np.random.randint(90, 100, num_samples),
        "Body Temperature": np.random.uniform(36.5, 37.5, num_samples),
        "Respiratory Rate": np.random.randint(12, 20, num_samples),
        "Latitude": np.random.uniform(-90, 90, num_samples),
        "Longitude": np.random.uniform(-180, 180, num_samples),
        "Weather Condition": np.random.choice(["Clear", "Rain", "Snow", "Fog", "Storm"], num_samples),
        "Time of Day": np.random.choice(["Morning", "Afternoon", "Evening", "Night"], num_samples),
        "Day of Week": np.random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], num_samples),
        "Crowd Density": np.random.randint(0, 100, num_samples),
        "Noise Level": np.random.uniform(0, 100, num_samples),
        "Light Level": np.random.uniform(0, 100, num_samples),
        "Stress Level": np.random.randint(0, 10, num_samples)
    }

    df = pd.DataFrame(data)
    df = pd.get_dummies(df, columns=["Weather Condition", "Time of Day", "Day of Week"])

    return df

# Generate synthetic data
num_samples = 1000
synthetic_data = generate_threat_severity_data(num_samples)

# Save the synthetic data to a CSV file
synthetic_data.to_csv('data/threat_severity_data.csv', index=False)
print(f"Synthetic data with {num_samples} samples saved to 'data/threat_severity_data.csv'")
