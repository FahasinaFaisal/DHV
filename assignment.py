# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('Dataset/master.csv')

# Select specific countries for analysis
selected_countries = ['Norway', 'Switzerland', 'Iceland', 'Denmark', 'Netherlands', 'Finland', 'Australia', 'Canada', 'New Zealand', 'Sweden']
df_selected_countries = df[df['country'].isin(selected_countries)]

# Set the style of the plots
sns.set_style("whitegrid")

# Set up subplots for a 2x2 grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 15))

# Main title of the infographic
fig.suptitle('Evaluating Suicide Rates from 1985 to 2020', fontsize=26, ha='center', color='#4B0082')

# Set background color for the entire infographic
fig.set_facecolor('#F5F5DC')

# Plot 1: Bar chart - Total Suicides by Country
sns.barplot(x='suicides_no', y='country', data=df_selected_countries, ax=axes[0, 1], 
            order=df_selected_countries.groupby('country')['suicides_no'].sum().sort_values(ascending=False).index, palette='magma', errorbar=None)
axes[0, 1].set_title('Visualisation B: Total Suicides by Country\n', fontsize=18, ha='center', color='indigo')

# Plot 2: Grouped Bar chart - Suicides for Male and Female Comparison (5-year gap)
df_gender_comparison_5year = df_selected_countries[df_selected_countries['sex'].isin(['male', 'female'])]
df_gender_comparison_5year = df_gender_comparison_5year[df_gender_comparison_5year['year'] % 5 == 0]

sns.barplot(x='year', y='suicides_no', hue='sex', data=df_gender_comparison_5year, ax=axes[1, 1], palette='plasma', errorbar=None)
axes[1, 1].set_title('Visualisation D: Suicides Comparison: Male vs. Female (5-year Gap)\n', fontsize=18, ha='center', color='indigo')
axes[1, 1].legend(title='Gender', loc='upper center')  

# Plot 3: Pie chart - Distribution of Suicides by Age with gap and increased size
age_distribution = df_selected_countries.groupby('age')['suicides_no'].sum()
colors = sns.color_palette('inferno', len(age_distribution))

wedgeprops = {'linewidth': 2, 'edgecolor': 'white', 'width': 0.4}
axes[1, 0].pie(age_distribution, labels=age_distribution.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=wedgeprops, radius=1.2)
axes[1, 0].set_title('Visualisation C: Distribution of Suicides by Age\n', fontsize=18, ha='center', color='indigo')

# Plot 4: Line chart - Total Suicides Over Years
sns.lineplot(x='year', y='suicides_no', data=df_selected_countries, estimator='sum', ax=axes[0, 0], color='purple', marker='o')
axes[0, 0].set_title('Visualisation A: Total Suicides Over Years\n', fontsize=18, ha='center', color='indigo')

# Adjust layout including legend
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Add paragraph describing the visualizations and student information at the bottom
fig.text(0.02, -0.18, '''
This infographic illustrates the changes in global suicide rates over years, specific countries, age groups, and genders.

Visualisation A: From 1985 to 2020, global suicide rates fluctuated, showing periods of vulnerability and successes in prevention efforts, with a noticeable decrease by 2020.

Visualisation B: Norway, New Zealand, and Iceland consistently had lower rates due to strong healthcare and societal support. Canada stood out with the highest number of suicides, emphasizing the need for targeted interventions.

Visualisation C: Individuals aged 35-54 faced higher suicide risks, whereas children and the elderly tend to have lower rates. calling for specific strategies considering cultural and healthcare factors.

Visualisation D: Males consistently had higher suicide rates, peaking in 2020, highlighting the importance of gender-sensitive approaches.
''', fontsize=16, ha='left', va='bottom', color='#4B0082', wrap=True, bbox=dict(facecolor='#F5F5DC', edgecolor='#E6E6FF', boxstyle='round,pad=1.5'))

# Add student information
fig.text(0.98, 0.95, 'Student Name: Your Name\nStudent ID: Your ID', fontsize=18, ha='right', va='top', color='#4B0082')

# Save the figure
plt.savefig("suicide_rate.png", dpi=300, bbox_inches='tight')

# Show the plots
plt.show()
