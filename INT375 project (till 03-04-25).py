
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ 1. Basic Visualization of data

# Load the dataset
file_path = "C:\\INT 375 Project\\Air quality dataset 26-03-2025  (1).csv"
data = pd.read_csv(file_path)

# Display basic information
print("Dataset Info:")
print(data.info())

# Display first few rows
print("\n🔹 First 5 Rows:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
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



# ✅ 5. Grouping the data by state
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


# ✅ 6.Group by city and calculate the average pollution level
city_pollution = data.groupby('city')['pollutant_avg'].mean().reset_index()

# ✅ Sort the cities by average pollution level in descending order
top_5_cities = city_pollution.sort_values('pollutant_avg', ascending=False).head(5)

# ✅ 7.Bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='pollutant_avg', y='city', hue='city', data=top_5_cities, palette='Reds', legend=False)


plt.title('Top 5 Most Polluted Cities (Average µg/m³)')
plt.xlabel('Average Pollution Level (µg/m³)')
plt.ylabel('City')
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()

# ✅ 8. Filter the dataset to include only the top 5 cities
top_5_data = data[data['city'].isin(top_5_cities['city'].tolist())]

# ✅ Mean pollution level by city
mean_pollution = top_5_data.groupby('city')['pollutant_avg'].mean().reset_index()
print("\n Mean Pollution Level by City:")
print(mean_pollution)

# ✅ Median pollution level by city
median_pollution = top_5_data.groupby('city')['pollutant_avg'].median().reset_index()
print("\n Median Pollution Level by City:")
print(median_pollution)

# ✅ Maximum pollution level by city
max_pollution = top_5_data.groupby('city')['pollutant_avg'].max().reset_index()
print("\n Maximum Pollution Level by City:")
print(max_pollution)

# ✅ Minimum pollution level by city
min_pollution = top_5_data.groupby('city')['pollutant_avg'].min().reset_index()
print("\n Minimum Pollution Level by City:")
print(min_pollution)

# ✅ Standard Deviation by city
std_pollution = top_5_data.groupby('city')['pollutant_avg'].std().reset_index()
print("\n Standard Deviation by City:")
print(std_pollution)

# ✅ Variance by city
var_pollution = top_5_data.groupby('city')['pollutant_avg'].var().reset_index()
print("\n Variance by City:")
print(var_pollution)

# ✅ Count of records for each city
count_pollution = top_5_data.groupby('city')['pollutant_avg'].count().reset_index()
print("\n Count of Records by City:")
print(count_pollution)

# ✅ 4.Statistics of latitudes of different States

# ✅ 1. Mean Latitude by State
mean_latitude = data.groupby('state')['latitude'].mean().reset_index()
print("\nMean Latitude by State:")
print(mean_latitude)

# ✅ 2. Median Latitude by State
median_latitude = data.groupby('state')['latitude'].median().reset_index()
print("\nMedian Latitude by State:")
print(median_latitude)

# ✅ 3. Minimum Latitude by State
min_latitude = data.groupby('state')['latitude'].min().reset_index()
print("\nMinimum Latitude by State:")
print(min_latitude)

# ✅ 4. Maximum Latitude by State
max_latitude = data.groupby('state')['latitude'].max().reset_index()
print("\nMaximum Latitude by State:")
print(max_latitude)

# ✅ 5. Standard Deviation of Latitude by State
std_latitude = data.groupby('state')['latitude'].std().reset_index()
print("\nStandard Deviation of Latitude by State:")
print(std_latitude)

# ✅ 6. Variance of Latitude by State
var_latitude = data.groupby('state')['latitude'].var().reset_index()
print("\nVariance of Latitude by State:")
print(var_latitude)

# ✅ 7. Count of Latitude Records by State
count_latitude = data.groupby('state')['latitude'].count().reset_index()
print("\nCount of Latitude Records by State:")
print(count_latitude)

# ✅ 4. Statistics of Longitudes of Different States

# ✅ 1. Mean Longitude by State
mean_longitude = data.groupby('state')['longitude'].mean().reset_index()
print("\nMean Longitude by State:")
print(mean_longitude)

# ✅ 2. Median Longitude by State
median_longitude = data.groupby('state')['longitude'].median().reset_index()
print("\nMedian Longitude by State:")
print(median_longitude)

# ✅ 3. Minimum Longitude by State
min_longitude = data.groupby('state')['longitude'].min().reset_index()
print("\nMinimum Longitude by State:")
print(min_longitude)

# ✅ 4. Maximum Longitude by State
max_longitude = data.groupby('state')['longitude'].max().reset_index()
print("\nMaximum Longitude by State:")
print(max_longitude)

# ✅ 5. Standard Deviation of Longitude by State
std_longitude = data.groupby('state')['longitude'].std().reset_index()
print("\nStandard Deviation of Longitude by State:")
print(std_longitude)

# ✅ 6. Variance of Longitude by State
var_longitude = data.groupby('state')['longitude'].var().reset_index()
print("\nVariance of Longitude by State:")
print(var_longitude)

# ✅ 7. Count of Longitude Records by State
count_longitude = data.groupby('state')['longitude'].count().reset_index()
print("\nCount of Longitude Records by State:")
print(count_longitude)

# ✅ Scatter Plot: Geographical Distribution of Air Quality Monitoring Stations
plt.figure(figsize=(12, 6))

# Scatter plot with longitude on x-axis and latitude on y-axis
sns.scatterplot(x=data['longitude'], y=data['latitude'], hue=data['pollutant_avg'], palette='coolwarm', edgecolor='black')

# Labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Air Quality Monitoring Stations')
plt.legend(title="Pollutant Level", loc='best')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

