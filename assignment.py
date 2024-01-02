# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:11:34 2024

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV files.
df = pd.read_csv('C:/Users/USER/Desktop/DHV/master.csv')

# Select specific countries
selected_countries = ['Norway', 'Switzerland', 'Iceland', 'Denmark', 'Netherlands', 'Finland', 'Australia', 'Canada', 'New Zealand', 'Sweden']
df_selected_countries = df[df['country'].isin(selected_countries)]

# Set style
sns.set_style("whitegrid")

# Set up the subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

# Main title
fig.suptitle('Suicide Rates in Developed Countries', fontsize=18, ha='center')

# Set background color for the entire dashboard
fig.set_facecolor('#E6E6FF')   # Light Purple 

# Plot 1: Bar chart - Total Suicides by Country
sns.barplot(x='suicides_no', y='country', data=df_selected_countries, ax=axes[0, 1], 
            order=df_selected_countries.groupby('country')['suicides_no'].sum().sort_values(ascending=False).index, palette='viridis', errorbar=None)
axes[0, 1].set_title('Total Suicides by Country')

# Plot 2: Grouped Bar chart - Suicides for Male and Female Comparison (5-year gap)
df_gender_comparison_5year = df_selected_countries[df_selected_countries['sex'].isin(['male', 'female'])]
df_gender_comparison_5year = df_gender_comparison_5year[df_gender_comparison_5year['year'] % 5 == 0]

sns.barplot(x='year', y='suicides_no', hue='sex', data=df_gender_comparison_5year, ax=axes[1, 1], palette='viridis', errorbar=None)
axes[1, 1].set_title('Suicides Comparison: Male vs. Female (5-year Gap)')
axes[1, 1].legend(title='Gender', loc='upper center')  # Adjust legend location and add title

# Plot 3: Pie chart - Distribution of Suicides by Age with gap and increased size
age_distribution = df_selected_countries.groupby('age')['suicides_no'].sum()
colors = sns.color_palette('viridis')[0:len(age_distribution)]

# Add gap and increase size
wedgeprops = {'linewidth': 2, 'edgecolor': 'white', 'width': 0.4}
axes[1, 0].pie(age_distribution, labels=age_distribution.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=wedgeprops, radius=1)
axes[1, 0].set_title('Distribution of Suicides by Age')

# Plot 4: Line chart - Total Suicides Over Years
sns.lineplot(x='year', y='suicides_no', data=df_selected_countries, estimator='sum', ax=axes[0, 0], color='#004b00', marker='o')
axes[0, 0].set_title('Total Suicides Over Years')

# Adjust layout including legend
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Add paragraph, student name, and student ID at the bottom
plt.figtext(0.1, -0.1, 'This dashboard visualizes suicide rate data for selected countries over the years. It includes total suicides over years, total suicides by country, a comparison of suicides between males and females (5-year gap), and the distribution of suicides by age.', fontsize=10, ha='left', va='bottom', color='black')
plt.figtext(0.5, -0.15, 'Student Name: Your Name\nStudent ID: Your ID', fontsize=10, ha='right', va='bottom', color='black')

# Save the figure
plt.savefig("suicide_rate.png", dpi=300, bbox_inches='tight')

# Show the plots
plt.show()
