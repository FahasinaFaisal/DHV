import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV files.
df = pd.read_csv(
    'C:/Users/USER/Desktop/DHV/master.csv')

# Select specific countries
selected_countries = ['United States', 'United Kingdom', 'Sweden', 'Germany', 'Egypt', 'India', 'Japan', 'Canada', 'Spain', 'Thailand']
df_selected_countries = df[df['country'].isin(selected_countries)]

# Set up the subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Bar chart 1 - Total Suicides Over Years
df_subset_year = df_selected_countries[['year', 'suicides_no']].groupby('year', as_index=False).sum()
sns.lineplot(x='year', y='suicides_no', data=df_subset_year, estimator='sum', ax=axes[0, 0])
axes[0, 0].set_title('Total Suicides Over Years')

# Bar chart 2 - Total Suicides by Country
df_subset_country = df_selected_countries[['country', 'suicides_no']].groupby('country', as_index=False).sum().sort_values('suicides_no', ascending=False)
sns.barplot(x='suicides_no', y='country', data=df_subset_country, ax=axes[0, 1])
axes[0, 1].set_title('Total Suicides by Country')

# Pie chart - Distribution of Suicides by Gender
df_subset_gender = df_selected_countries[['sex', 'suicides_no']].groupby('sex', as_index=False).sum()
axes[1, 0].pie(df_subset_gender['suicides_no'], labels=df_subset_gender['sex'], autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Distribution of Suicides by Gender')

# Bar chart 3 - Total Suicides by Generation
df_subset_generation = df_selected_countries[['generation', 'suicides_no']].groupby('generation', as_index=False).sum().sort_values('suicides_no', ascending=False)
sns.barplot(x='suicides_no', y='generation', data=df_subset_generation, ax=axes[1, 1])
axes[1, 1].set_title('Total Suicides by Generation')

# Adjust layout
plt.tight_layout()

# Add a paragraph
plt.figtext(0.5, 0.01, 'This dashboard shows the total number of suicides over the years, by country, by gender, and by generation.', ha='center', va='center', fontsize=12)

# Show the plots
plt.show()