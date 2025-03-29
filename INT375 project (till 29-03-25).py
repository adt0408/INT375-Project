
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ 1. Basic Visualization of data

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
print("\nColumn Names:")
print(data.columns)

# ✅ 2. Data Cleaning

# Check for duplicates and remove them
print("\n Checking for duplicates...")
duplicates = data.duplicated().sum()
print(f"Duplicate rows: {duplicates}")
data = data.drop_duplicates()

# Checking for missing values in undesired columns
print("\nHandling missing values...")
missing_values = data.isnull().sum()
print("\nMissing values per column:")
print(missing_values)

# ✅ 3. Summary Statistics
print("\n Summary statistics for pollutants:")
print(data["pollutant_avg"].describe())






