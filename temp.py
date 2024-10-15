# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with the actual dataset path or URL)
url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
df = pd.read_csv(url)

# Step 1: Data Cleaning and Preprocessing
# Display the first few rows of the dataset to check its structure
print("Dataset head:\n", df.head())

# Strip any leading/trailing whitespace from column names
df.columns = df.columns.str.strip()

# Convert 'Year' to datetime, specifying format since it includes month
df['Year'] = pd.to_datetime(df['Year'], format='%Y-%m')

# Step 2: Extract Year and Filter Recent Data
# Extract year from the date
df['Year'] = df['Year'].dt.year  # Extract only the year for further analysis

# Filter data for the most recent years (e.g., last 20 years) and create a copy
recent_years = df['Year'].unique()
recent_years = recent_years[recent_years >= (df['Year'].max() - 20)]
recent_data = df[df['Year'].isin(recent_years)].copy()  # Make a copy to avoid SettingWithCopyWarning

# Step 3: Compute Global Averages for Recent Years
# Group by year and compute average temperature globally
yearly_avg = recent_data.groupby('Year').mean()['Mean']

# Display yearly average temperature
print("\nYearly average global temperature (last 20 years):\n", yearly_avg)

# Step 4: Visualizing Recent Global Temperature Trend
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', label='Average Global Temperature (°C)', color='blue')
plt.title('Recent Global Temperature Trend (Last 20 Years)')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.xticks(yearly_avg.index, rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Step 5: Analyze Temperature Anomalies (Difference from Mean)
global_mean_temp = yearly_avg.mean()

# Use .loc to avoid SettingWithCopyWarning
recent_data.loc[:, 'Temperature_Anomaly'] = recent_data['Mean'] - global_mean_temp

# Compute yearly average anomaly
yearly_anomaly = recent_data.groupby('Year').mean()['Temperature_Anomaly']

# Plot recent temperature anomalies over time
plt.figure(figsize=(10, 6))
plt.bar(yearly_anomaly.index, yearly_anomaly.values, color='orange')
plt.title('Recent Global Temperature Anomalies (Last 20 Years)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.xticks(yearly_anomaly.index, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Insights and Summary
print("\nSummary of Recent Global Temperature Trends:")
print(f"Global Mean Temperature (Last 20 Years): {global_mean_temp:.2f} °C")
print(f"Max Anomaly Year: {yearly_anomaly.idxmax()}, Anomaly: {yearly_anomaly.max():.2f} °C")
print(f"Min Anomaly Year: {yearly_anomaly.idxmin()}, Anomaly: {yearly_anomaly.min():.2f} °C")

