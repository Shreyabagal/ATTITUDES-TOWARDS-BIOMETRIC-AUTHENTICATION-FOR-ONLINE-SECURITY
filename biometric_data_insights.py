# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Load the CSV file
file_path = '/content/Biometric_Authentication.csv'  
data = pd.read_csv(file_path, encoding='latin-1') 

# Step 2: Take the first 200 responses
data = data.head(200)

# Step 3: Overview of the data
print("Data Overview:\n", data.info())
print("\nFirst 5 rows:\n", data.head())

# Step 4: Clean the data if needed
print("\nMissing Values:\n", data.isnull().sum())
data.fillna('Unknown', inplace=True)

# Step 5: Analyzing general statistics
print("\nBasic Statistics:\n", data.describe())

# Step 6: Count Plot for Categorical Question
plt.figure(figsize=(10,6))
print(data.columns)
sns.countplot(x='Gender', data=data)  
plt.title('Distribution of Responses for Question')
plt.xticks(rotation=45)
plt.show()

# Step 7: Histogram for numerical question (replace 'NumericQuestion' with actual column)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
sns.histplot(data['Age'], kde=True, bins=10)  
plt.title('Histogram of Numeric Responses')
plt.show()

# Step 8: Cross-tabulation for insights between two categorical questions (replace columns accordingly)
cross_tab = pd.crosstab(data['Gender'], data['Occupation'])  
print("\nCross Tabulation:\n", cross_tab)

# Step 9: Export cleaned data or results back to CSV
data.to_csv('cleaned_biometric_data.csv', index=False)

# Step 10: Correlation Analysis for Numerical Data
# Function to get the mid-point of an age range
def get_mid_age(age_range):
    if '-' in age_range:
        start, end = map(int, age_range.split('-'))
        return (start + end) / 2
    try:
        return float(age_range)  # If already numeric, convert to float
    except ValueError:
        return np.nan  # Handle cases with invalid values
# Apply the function to the 'Age' column
data['Age'] = data['Age'].apply(get_mid_age)
# Drop rows with NaN values in 'Age' column to avoid errors with correlation
data = data.dropna(subset=['Age'])
# Now calculate the correlation matrix
correlation_matrix = data.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation_matrix)

# Step 11: Heatmap for Correlation Matrix
plt.figure(figsize=(12,9))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlations')
plt.show()

# Step 12: Boxplot to Analyze Spread of Responses for a Numerical Column (replace 'NumericQuestion')
plt.figure(figsize=(8,6))
sns.boxplot(y=data['Are you aware of any regulations governing the use of biometric data? '])
plt.title('Boxplot of Numeric Responses')
plt.show()

# Step 13: Scatter Plot for Analyzing Relation between Two Numeric Columns (replace columns accordingly)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Age', y='Gender', data=data)
plt.title('Scatter Plot between Two Numeric Responses')
plt.show()

# Step 14: Grouping Data by Categories and Analyzing Mean Values (replace 'CategoryColumn' and 'NumericColumn')
grouped_data = data.groupby('Gender')['Age'].mean()
print(f"\nGrouped Data Analysis:\n{grouped_data}")

# Step 15: Line Plot to Show Trends in Grouped Data
grouped_data.plot(kind='line', figsize=(10,6), marker='o', title='Mean Numeric Responses by Category')
plt.show()

# Step 16: Frequency Distribution of Each Question (Categorical Columns)
categorical_columns = data.select_dtypes(include='object').columns  
for column in categorical_columns:
    plt.figure(figsize=(10,6))
    sns.countplot(y=column, data=data, palette='Set2')
    plt.title(f'Frequency Distribution of {column}')
    plt.show()

# Step 17: Analyzing Specific Responses for a Particular Question
response_counts = data['Occupation'].value_counts() 
print(f"\nResponse Distribution for Satisfaction Question:\n{response_counts}")
plt.figure(figsize=(8,6))
sns.barplot(x=response_counts.index, y=response_counts.values, palette='Blues_d')
plt.title('Satisfaction Levels with Biometric Authentication')
plt.xlabel('Satisfaction Level')
plt.ylabel('Frequency')
plt.show()
 

