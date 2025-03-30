
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

# ✅ 4.Statistics of different States


# ✅ 1. Grouping the data by state
state_group = data.groupby('state')['pollutant_avg']


# Mean (average) pollution level by state
mean_pollution = state_group.mean().reset_index()
print("\nMean Pollution Level by State:")
print(mean_pollution)

# Median pollution level by state
median_pollution = state_group.median().reset_index()
print("\nMedian Pollution Level by State:")
print(median_pollution)

# Maximum pollution level by state
max_pollution = state_group.max().reset_index()
print("\nMaximum Pollution Level by State:")
print(max_pollution)

# Minimum pollution level by state
min_pollution = state_group.min().reset_index()
print("\nMinimum Pollution Level by State:")
print(min_pollution)

# Standard deviation of pollution level by state
std_pollution = state_group.std().reset_index()
print("\nStandard Deviation of Pollution Level by State:")
print(std_pollution)






