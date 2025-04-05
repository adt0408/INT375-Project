import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ 1. Basic Visualization of data

# Load the dataset
file_path = "C:\\INT 375 Project\\Air quality dataset 26-03-2025  (1).csv"
data = pd.read_csv(file_path)

# Convert pollutant_avg to numeric
data['pollutant_avg'] = pd.to_numeric(data['pollutant_avg'], errors='coerce')
data = data.dropna(subset=['pollutant_avg'])

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

# ✅ 6. Group by city and calculate the average pollution level
city_pollution = data.groupby('city')['pollutant_avg'].mean().reset_index()

# ✅ Sort the cities by average pollution level in descending order
top_5_cities = city_pollution.sort_values('pollutant_avg', ascending=False).head(5)

# ✅ 7. Bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='pollutant_avg', y='city', hue='city', data=top_5_cities, palette='Reds', legend=False)
plt.title('Top 5 Most Polluted Cities (Average µg/m³)')
plt.xlabel('Average Pollution Level (µg/m³)')
plt.ylabel('City')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()

# ✅ 8. Filter the dataset to include only the top 5 cities
top_5_data = data[data['city'].isin(top_5_cities['city'].tolist())]

# ✅ Pollution statistics for top 5 cities
print("\nMean Pollution Level by City:")
print(top_5_data.groupby('city')['pollutant_avg'].mean().reset_index())

print("\nMedian Pollution Level by City:")
print(top_5_data.groupby('city')['pollutant_avg'].median().reset_index())

print("\nMaximum Pollution Level by City:")
print(top_5_data.groupby('city')['pollutant_avg'].max().reset_index())

print("\nMinimum Pollution Level by City:")
print(top_5_data.groupby('city')['pollutant_avg'].min().reset_index())

print("\nStandard Deviation by City:")
print(top_5_data.groupby('city')['pollutant_avg'].std().reset_index())

print("\nVariance by City:")
print(top_5_data.groupby('city')['pollutant_avg'].var().reset_index())

print("\nCount of Records by City:")
print(top_5_data.groupby('city')['pollutant_avg'].count().reset_index())

# ✅ Latitude statistics by state
print("\nMean Latitude by State:")
print(data.groupby('state')['latitude'].mean().reset_index())

print("\nMedian Latitude by State:")
print(data.groupby('state')['latitude'].median().reset_index())

print("\nMinimum Latitude by State:")
print(data.groupby('state')['latitude'].min().reset_index())

print("\nMaximum Latitude by State:")
print(data.groupby('state')['latitude'].max().reset_index())

print("\nStandard Deviation of Latitude by State:")
print(data.groupby('state')['latitude'].std().reset_index())

print("\nVariance of Latitude by State:")
print(data.groupby('state')['latitude'].var().reset_index())

print("\nCount of Latitude Records by State:")
print(data.groupby('state')['latitude'].count().reset_index())

# ✅ Longitude statistics by state
print("\nMean Longitude by State:")
print(data.groupby('state')['longitude'].mean().reset_index())

print("\nMedian Longitude by State:")
print(data.groupby('state')['longitude'].median().reset_index())

print("\nMinimum Longitude by State:")
print(data.groupby('state')['longitude'].min().reset_index())

print("\nMaximum Longitude by State:")
print(data.groupby('state')['longitude'].max().reset_index())

print("\nStandard Deviation of Longitude by State:")
print(data.groupby('state')['longitude'].std().reset_index())

print("\nVariance of Longitude by State:")
print(data.groupby('state')['longitude'].var().reset_index())

print("\nCount of Longitude Records by State:")
print(data.groupby('state')['longitude'].count().reset_index())

# ✅ Scatter Plot: Geographical Distribution
plt.figure(figsize=(12, 6))
sns.scatterplot(x='longitude', y='latitude', hue='pollutant_avg', data=data, palette='coolwarm', edgecolor='black')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Air Quality Monitoring Stations')
plt.legend(title="Pollutant Level", loc='best')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# ✅ Count of stations per state
station_counts = data['state'].value_counts().reset_index()
station_counts.columns = ['state', 'station_count']

plt.figure(figsize=(14, 6))
sns.barplot(x='station_count', y='state', data=station_counts, palette='Blues_r', hue='state', legend=False)
plt.title('Number of Monitoring Stations by State')
plt.xlabel('Number of Stations')
plt.ylabel('State')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Pie chart for pollutant type distribution
pollutant_counts = data['pollutant_id'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title('Distribution of Pollutant Types Recorded')
plt.axis('equal')
plt.show()

# ✅ Avg pollutant value by pollutant type
avg_pollutant_values = data.groupby('pollutant_id')['pollutant_avg'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='pollutant_id', y='pollutant_avg', data=avg_pollutant_values, palette='Oranges_r', hue='pollutant_id', legend=False)
plt.title('Average Pollution Level by Pollutant Type')
plt.xlabel('Pollutant')
plt.ylabel('Average Level (µg/m³)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# ✅ Top 10 cities with highest max pollution
city_max_pollution = data.groupby('city')['pollutant_max'].max().reset_index()
top_10_max_pollution = city_max_pollution.sort_values('pollutant_max', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='pollutant_max', y='city', data=top_10_max_pollution, palette='rocket', hue='city', legend=False)
plt.title('Top 10 Cities with Highest Maximum Pollution Levels')
plt.xlabel('Maximum Pollution Level (µg/m³)')
plt.ylabel('City')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Pollution range (Min vs Max) by state
state_pollution_min = data.groupby('state')['pollutant_min'].min().reset_index()
state_pollution_max = data.groupby('state')['pollutant_max'].max().reset_index()
pollution_range = pd.merge(state_pollution_min, state_pollution_max, on='state')

plt.figure(figsize=(14, 6))
plt.plot(pollution_range['state'], pollution_range['pollutant_min'], label='Min Pollution', marker='o')
plt.plot(pollution_range['state'], pollution_range['pollutant_max'], label='Max Pollution', marker='o')
plt.xticks(rotation=90)
plt.title('Pollution Range (Min vs Max) by State')
plt.xlabel('State')
plt.ylabel('Pollution Level (µg/m³)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
