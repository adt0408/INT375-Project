
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:\INT 375 Project\Air quality dataset 26-03-2025  (1).csv"
data = pd.read_csv(file_path)

# Display basic information
print("Dataset Info:")
print(data.info())

# Display first few rows
print("\n🔹 First 5 Rows:")
print(data.head())

# Check for missing values
print("\Missing Values:")
print(data.isnull().sum())

# Display column names
print("\n📊 Column Names:")
print(data.columns)

