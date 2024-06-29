import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'DataSet/CropProductiondata.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# 1) Bar graph: Sum of Production by Crop_Year
plt.figure(figsize=(10, 6))
production_by_year = df.groupby('Crop_Year')['Production'].sum()
production_by_year.plot(kind='bar', color='skyblue')
plt.xlabel('Crop Year')
plt.ylabel('Sum of Production')
plt.title('Sum of Production by Crop Year')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 2) Pie chart: Sum of Production by Season (excluding 'Whole Year')
# Filter rows where 'Season' is not 'Whole Year'
filtered_df = df[df['Season'] != 'Whole Year ']
# Calculate sum of production by season
production_by_season = filtered_df.groupby('Season')['Production'].sum()
# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(production_by_season, labels=production_by_season.index, autopct='%1.1f%%', startangle=140)
plt.title('\n\nSum of Production by Season (Excluding Whole Year)')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Assuming df is your DataFrame containing Crop and Production columns
# 3) Grouping by Crop and calculating the sum of Production
production_of_crop = df.groupby('Crop')['Production'].sum()
# Creating a horizontal bar plot
plt.figure(figsize=(20, 40))  # Adjust figsize as needed
production_of_crop.sort_values().plot(kind='barh', color='lightgreen')  # Sort values for better visualization
plt.xlabel('Sum of Production')
plt.ylabel('Crop')
plt.title('\n\nSum of Production of each crop')
plt.grid(axis='x')  # Grid along the x-axis
plt.tight_layout()
plt.show()


# 4) Pie chart: Sum of Production by State_Name
plt.figure(figsize=(8, 8))
production_by_state = df.groupby('State_Name')['Production'].sum()
plt.pie(production_by_state, autopct='%1.1f%%', startangle=140)
plt.title('\n\nSum of Production by State')
plt.legend(title='State_Name',labels=production_by_state.index, loc='center left', bbox_to_anchor=(1, 0.5))
plt.axis('equal')
plt.tight_layout()
plt.show()

df['Crop'] = df['Crop'].str.strip()
coconut_df = df[df['Crop']=='Coconut']
plt.figure(figsize=(8, 8))
production_of_coconut = coconut_df.groupby('State_Name')['Production'].sum()
plt.pie(production_of_coconut, labels=production_of_coconut.index, autopct='%1.1f%%', startangle=140)
plt.title('\n\nSum of Production of Coconut by State')
plt.legend(title='State_Name', loc='center left', bbox_to_anchor=(1, 0.5))
plt.axis('equal')
plt.tight_layout()
plt.show()


