# app.py
import customtkinter as ctk
from tkinter import messagebox, filedialog
import numpy as np
import pandas as pd
import joblib

class SEFThreatDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SEF Threat Detection Application")
        
        self.create_widgets()
        self.model = joblib.load('models/threat_detection_model.pkl')

    def create_widgets(self):
        # Configure the grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # File upload button
        self.upload_button = ctk.CTkButton(self.root, text="Upload Data File", command=self.load_file)
        self.upload_button.grid(row=0, column=0, columnspan=2, pady=10)

        # Preview Button
        self.preview_button = ctk.CTkButton(self.root, text="Preview Data", command=self.preview_data)
        self.preview_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Calculate Button
        self.calculate_button = ctk.CTkButton(self.root, text="Calculate Threat Severity", command=self.calculate_threat_severity)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Save Button
        self.save_button = ctk.CTkButton(self.root, text="Save Data", command=self.save_file)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = ctk.CTkLabel(self.root, text="Threat Severity Score: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if not file_path:
            return

        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            else:
                messagebox.showerror("File Error", "Unsupported file format")
                return
            messagebox.showinfo("File Loaded", "File loaded successfully")
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading file: {str(e)}")

    def preview_data(self):
        try:
            if not hasattr(self, 'data'):
                raise ValueError("No data loaded. Please load a data file first.")
            print(self.data.head())  # Debugging line to print the head of the dataframe
            self.plot_data(self.data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def plot_data(self, df):
        import matplotlib.pyplot as plt
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        plt.figure(figsize=(10, 8))
        for column in numeric_columns:
            plt.hist(df[column], bins=30, alpha=0.5, label=column)
        plt.legend(loc='upper right')
        plt.title('Data Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

    def calculate_threat_severity(self):
        try:
            if not hasattr(self, 'data'):
                raise ValueError("No data loaded. Please load a data file first.")

            required_columns = [
                'Threat Level', 'Vulnerability Level', 'Impact Level', 'Environmental Data',
                'Health Data', 'Vehicle Data', 'Heart Rate', 'Blood Pressure Systolic', 
                'Blood Pressure Diastolic', 'SpO2', 'Body Temperature', 'Respiratory Rate', 
                'Latitude', 'Longitude', 'Crowd Density', 'Noise Level', 'Light Level', 
                'Stress Level', 'Weather Condition_Clear', 'Weather Condition_Rain', 
                'Weather Condition_Snow', 'Weather Condition_Fog', 'Weather Condition_Storm', 
                'Time of Day_Morning', 'Time of Day_Afternoon', 'Time of Day_Evening', 
                'Time of Day_Night', 'Day of Week_Monday', 'Day of Week_Tuesday', 
                'Day of Week_Wednesday', 'Day of Week_Thursday', 'Day of Week_Friday', 
                'Day of Week_Saturday', 'Day of Week_Sunday'
            ]

            # Check if all required columns are present
            missing_columns = [col for col in required_columns if col not in self.data.columns]
            if missing_columns:
                raise KeyError(f"Missing required columns: {missing_columns}")

            X = self.data[required_columns]
            predictions = self.model.predict(X)
            self.data['Threat Detected'] = predictions
            threat_severity_score = self.calculate_severity_score(self.data)

            self.result_label.configure(text=f'Threat Severity Score: {threat_severity_score:.2f}')
        except KeyError as e:
            messagebox.showerror("Data Error", f"Missing column in data: {str(e)}")
        except Exception as e:
            messagebox.showerror("Analysis Error", f"Error analyzing data: {str(e)}")

    def calculate_severity_score(self, df):
        threat_levels = df['Threat Level']
        detected_threats = df['Threat Detected']
        severity_score = np.mean(threat_levels * detected_threats)
        return severity_score

    def save_file(self):
        try:
            if hasattr(self, 'data'):
                file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if file_path:
                    self.data.to_csv(file_path, index=False)
                    messagebox.showinfo("Success", f"Data saved as {file_path}")
            else:
                messagebox.showwarning("Warning", "No data to save. Please generate or load data first.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = SEFThreatDetectionApp(root)
    root.mainloop()
