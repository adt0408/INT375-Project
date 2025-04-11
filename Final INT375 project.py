import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅  Basic Visualization of data
file_path = "C:\\INT 375 Project\\Air quality dataset 26-03-2025  (1).csv"
data = pd.read_csv(file_path)

data['pollutant_avg'] = pd.to_numeric(data['pollutant_avg'], errors='coerce')
data = data.dropna(subset=['pollutant_avg'])

print("Dataset Info:")
print(data.info())

print("\n🔹 First 5 Rows:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nColumn Names:")
print(data.columns)

# ✅  Data Cleaning
print("\n Checking for duplicates...")
duplicates = data.duplicated().sum()
print(f"Duplicate rows: {duplicates}")
data = data.drop_duplicates()

print("\nHandling missing values...")
print("\nMissing values per column:")
print(data.isnull().sum())

# ✅  Summary Statistics
print("\n Summary statistics for pollutants:")
print(data["pollutant_avg"].describe())

# ✅  Grouping the data by state
state_group = data.groupby('state')['pollutant_avg']
print("\nMean Pollution Level by State:")
print(state_group.mean().reset_index())
print("\nMedian Pollution Level by State:")
print(state_group.median().reset_index())
print("\nMaximum Pollution Level by State:")
print(state_group.max().reset_index())
print("\nMinimum Pollution Level by State:")
print(state_group.min().reset_index())
print("\nStandard Deviation of Pollution Level by State:")
print(state_group.std().reset_index())

# ✅  Group by city and calculate the average pollution level
city_pollution = data.groupby('city')['pollutant_avg'].mean().reset_index()
top_5_cities = city_pollution.sort_values('pollutant_avg', ascending=False).head(5)



# ✅ Filter the dataset to include only the top 5 cities
top_5_data = data[data['city'].isin(top_5_cities['city'].tolist())]

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

# ✅ Latitude and Longitude statistics by state
for feature in ['latitude', 'longitude']:
    print(f"\n{feature.upper()} Statistics by State:")
    print("Mean:")
    print(data.groupby('state')[feature].mean().reset_index())
    print("Median:")
    print(data.groupby('state')[feature].median().reset_index())
    print("Minimum:")
    print(data.groupby('state')[feature].min().reset_index())
    print("Maximum:")
    print(data.groupby('state')[feature].max().reset_index())
    print("Std Dev:")
    print(data.groupby('state')[feature].std().reset_index())
    print("Variance:")
    print(data.groupby('state')[feature].var().reset_index())
    print("Count:")
    print(data.groupby('state')[feature].count().reset_index())

# ✅ Bar chart - Top 5 Most Polluted Cities
plt.figure(figsize=(12, 6))
sns.barplot(x='pollutant_avg', y='city', hue='city', data=top_5_cities, palette='Reds', legend=False)
plt.title('Top 5 Most Polluted Cities (Average µg/m³)')
plt.xlabel('Average Pollution Level (µg/m³)')
plt.ylabel('City')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()

# ✅ Scatter Plot - Geographic distribution
plt.figure(figsize=(12, 6))
sns.scatterplot(x='longitude', y='latitude', hue='pollutant_avg', data=data, palette='coolwarm', edgecolor='black')
plt.title('Geographical Distribution of Air Quality Monitoring Stations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title="Pollutant Level")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Bar Chart - Monitoring stations per state
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

# ✅ Pie chart - Pollutant types
pollutant_counts = data['pollutant_id'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title('Distribution of Pollutant Types Recorded')
plt.axis('equal')
plt.tight_layout()
plt.show()

# ✅ Bar Chart - Avg pollution by pollutant type
avg_pollutant_values = data.groupby('pollutant_id')['pollutant_avg'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='pollutant_id', y='pollutant_avg', data=avg_pollutant_values, palette='Oranges_r', hue='pollutant_id', legend=False)
plt.title('Average Pollution Level by Pollutant Type')
plt.xlabel('Pollutant')
plt.ylabel('Average Level (µg/m³)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Top 10 cities with highest max pollution
top_10_max_pollution = data.groupby('city')['pollutant_max'].max().reset_index().sort_values('pollutant_max', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='pollutant_max', y='city', data=top_10_max_pollution, palette='rocket', hue='city', legend=False)
plt.title('Top 10 Cities with Highest Maximum Pollution Levels')
plt.xlabel('Maximum Pollution Level (µg/m³)')
plt.ylabel('City')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Line Plot - Pollution Range by State
min_max_pollution = data.groupby('state')[['pollutant_min', 'pollutant_max']].agg('min').reset_index()

plt.figure(figsize=(14, 6))
plt.plot(min_max_pollution['state'], min_max_pollution['pollutant_min'], label='Min Pollution', marker='o')
plt.plot(min_max_pollution['state'], min_max_pollution['pollutant_max'], label='Max Pollution', marker='o')
plt.xticks(rotation=90)
plt.title('Pollution Range (Min vs Max) by State')
plt.xlabel('State')
plt.ylabel('Pollution Level (µg/m³)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Heatmap - Correlation
corr_data = data[['latitude', 'longitude', 'pollutant_avg', 'pollutant_min', 'pollutant_max']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_data, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap: Geographic & Pollution Features')
plt.tight_layout()
plt.show()

# ✅ Boxplot - Pollution by Pollutant Type
plt.figure(figsize=(12, 6))
sns.boxplot(x='pollutant_id', y='pollutant_avg', hue='pollutant_id', data=data, palette='Set3', legend=False)
plt.title('Distribution of Pollution Levels by Pollutant Type')
plt.xlabel('Pollutant Type')
plt.ylabel('Pollutant Average (µg/m³)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Bar Plot - State-wise Std Dev
state_std = data.groupby('state')['pollutant_avg'].std().reset_index().sort_values('pollutant_avg', ascending=False)

plt.figure(figsize=(14, 6))
sns.barplot(x='pollutant_avg', y='state', data=state_std, palette='mako', hue='state', legend=False)
plt.title('State-wise Variability in Pollution Levels (Standard Deviation)')
plt.xlabel('Standard Deviation of Pollution')
plt.ylabel('State')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Boxplot - Pollution by State
plt.figure(figsize=(16, 7))
sns.boxplot(x='state', y='pollutant_avg', hue='state', data=data, palette='Set3', legend=False)
plt.xticks(rotation=90)
plt.title('Distribution of Pollution Levels by State')
plt.xlabel('State')
plt.ylabel('Pollutant Level (µg/m³)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Histogram - Overall Pollution Distribution
plt.figure(figsize=(8, 4))
sns.histplot(data['pollutant_avg'], bins=30, kde=True, color='skyblue', stat='density', element='bars')
plt.title('Overall Distribution of Pollutant Average (µg/m³)')
plt.xlabel('Pollutant Average (µg/m³)')
plt.ylabel('Density')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Boxplot - Detect Outliers
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['pollutant_avg'], color='salmon')
plt.title('Boxplot of Pollutant Averages (Detecting Outliers)')
plt.xlabel('Pollutant Average (µg/m³)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ✅ Top 10 Polluted States
top_states = data.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_states.values, y=top_states.index, hue=top_states.index, palette='Reds_r', legend=False)
plt.title('Top 10 Most Polluted States (Average µg/m³)')
plt.xlabel('Average Pollutant Level (µg/m³)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# ✅ Least Polluted States
least_states = data.groupby('state')['pollutant_avg'].mean().sort_values().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=least_states.values, y=least_states.index, hue=least_states.index, palette='Greens', legend=False)
plt.title('Top 10 Least Polluted States (Average µg/m³)')
plt.xlabel('Average Pollutant Level (µg/m³)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# ✅ Top & Least Polluted Cities
top_cities = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
least_cities = data.groupby('city')['pollutant_avg'].mean().sort_values().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette='Oranges', legend=False)
plt.title('Top 10 Most Polluted Cities (Average µg/m³)')
plt.xlabel('Average Pollutant Level (µg/m³)')
plt.ylabel('City')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=least_cities.values, y=least_cities.index, hue=least_cities.index, palette='Blues', legend=False)
plt.title('Top 10 Least Polluted Cities (Average µg/m³)')
plt.xlabel('Average Pollutant Level (µg/m³)')
plt.ylabel('City')
plt.tight_layout()
plt.show()

# ✅ Scatter - Pollution vs Latitude/Longitude
plt.figure(figsize=(8, 4))
sns.scatterplot(x='latitude', y='pollutant_avg', data=data, alpha=0.5)
plt.title('Pollution Level vs Latitude')
plt.xlabel('Latitude')
plt.ylabel('Pollutant Average (µg/m³)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.scatterplot(x='longitude', y='pollutant_avg', data=data, alpha=0.5)
plt.title('Pollution Level vs Longitude')
plt.xlabel('Longitude')
plt.ylabel('Pollutant Average (µg/m³)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

