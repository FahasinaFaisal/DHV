
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects
import seaborn as sns

# Read the CSV file
df = pd.read_csv('master.csv')

# Select specific countries for analysis
selected_countries = ['Norway', 'Switzerland', 'Iceland', 'Denmark',
                      'Netherlands', 'Finland', 'Australia', 'Canada', 'New Zealand', 'Sweden']
df_selected_countries = df[df['country'].isin(selected_countries)]

# Set the style of the plots
sns.set_style("whitegrid")

# Set up subplots for a 2x2 grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 15))

# Main title of the infographic
fig.suptitle('Understanding How Economic Growth Affects Suicide Rates',
             fontsize=38, ha='center', color='#4B0082',
             weight='bold', va='center',
             path_effects=[matplotlib.patheffects.withStroke(linewidth=3, foreground='#800080', alpha=0.7)])

# Set background color for the entire infographic
fig.set_facecolor('#FFFFFF')

# Plot 1: Horizontal Grouped Bar chart - GDP per Capita and Total Suicides for Selected Countries
bar_height = 0.35  # Height of the bars
bar_positions = range(len(selected_countries))  # Set positions for the bars

# Plot GDP per Capital bars
gdp_bars = axes[0, 1].barh(bar_positions, df_selected_countries.groupby('country')['gdp_per_capital'].mean(),
                           height=bar_height, color='#6A0572', label='GDP per Capital')

# Plot Total Suicides bars
suicide_bars = axes[0, 1].barh([pos + bar_height for pos in bar_positions], df_selected_countries.groupby('country')['suicides_no'].sum(),
                               height=bar_height, color='#F9C74F', label='Total Suicides')

axes[0, 1].set_title('Visualisation B: GDP per Capital and Total Suicides\n',
                     fontsize=18, ha='center', color='indigo', weight='bold')
axes[0, 1].set_xlabel('Values',weight='bold')
axes[0, 1].set_ylabel('Country',weight='bold')
axes[0, 1].set_yticks([pos + bar_height / 2 for pos in bar_positions])
axes[0, 1].set_yticklabels(selected_countries)

# Add legend to the plot
axes[0, 1].legend()

# Plot 2: Grouped Bar chart - Suicides for Male, Female, and Total Population Comparison (5-year gap)
df_age_5year = df_selected_countries[(
    df_selected_countries['age'] == '35-54 years') & (df_selected_countries['year'] % 5 == 0)]

sns.barplot(x='year', y='suicides_no', hue='sex', data=df_age_5year,
            ax=axes[1, 1], palette=['#6A0572', '#F9C74F'], errorbar=None)
axes[1, 1].set_title('Visualisation D: Suicides Comparison (35-54 years): Male vs. Female(5-year Gap)\n',
                     fontsize=18, ha='center', color='indigo', weight='bold')
axes[1, 1].legend(title='Gender', loc='upper center')

# Plot 3: Pie chart - Distribution of Suicides by Age with gap and increased size
age_distribution = df_selected_countries.groupby('age')['suicides_no'].sum()
colors = sns.color_palette('plasma')

# Explode the "35-54 years" segment for emphasis
explode = [0.1 if age == '35-54 years' else 0 for age in age_distribution.index]
wedgeprops = {'linewidth': 2, 'edgecolor': 'white', 'width': 0.8}
axes[1, 0].pie(age_distribution, labels=age_distribution.index, autopct='%2.1f%%', startangle=90,
               colors=colors, explode=explode, wedgeprops=wedgeprops, shadow=True, radius=1.2)
axes[1, 0].set_title('Visualisation C: Distribution of Suicides by Age\n',
                     fontsize=18, ha='center', color='indigo', weight='bold')

# Plot 4: Line chart - Compare Suicides_no and HDI_for_Year Over Years
ax1 = axes[0, 0]

# Line chart for Suicides_no
sns.lineplot(x='year', y='suicides_no', data=df_selected_countries, estimator='sum',
             ax=ax1, color='#4B0082', marker='o', label='Suicides_no', errorbar=None)

# Secondary y-axis for HDI_for_year
ax2 = ax1.twinx()
sns.lineplot(x='year', y='HDI for year', data=df_selected_countries, estimator='mean',
             ax=ax2, color='#D2691E', marker='s', label='HDI for Year', errorbar=None)

# Set titles and labels for the primary y-axis
ax1.set_title('Visualisation A: Suicides numbers and HDI for Year Over Years\n',
              fontsize=18, ha='center', color='indigo', weight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Suicides_no', color='#4B0082')
ax1.tick_params(axis='y', labelcolor='#4B0082')

# Set titles and labels for the secondary y-axis
ax2.set_ylabel('HDI for Year', color='#D2691E')
ax2.tick_params(axis='y', labelcolor='#D2691E')

# Add legend for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Add paragraph describing the visualizations and student information at the bottom
fig.text(0.01, -0.22, r'''
$\mathbf{This\ infographic\ explores\ how\ economic\ factors,\ human\ development,\ and\ suicide\ rates\ interconnect\ in\ developed\ countries.}$

$\mathbf{Visualisation\ A:}$ Looking at the Human Development Index (HDI) and suicide rates, it suggests that improving healthcare and education, measured by HDI, may lower suicide rates.

$\mathbf{Visualisation\ B:}$ Considering Gross Domestic Product (GDP) and suicide rates, a trend emerges – countries with higher GDP generally have lower suicide rates.

$\mathbf{Visualisation\ C:}$ Examining age groups and suicide rates reveals that those aged 35-54 face a higher risk, prompting the need for targeted strategies considering culture and healthcare.

$\mathbf{Visualisation\ D:}$ In terms of gender within the higher-risk age group (35-54), men consistently exhibit a higher number of suicides than women.

In summary, the detailed discoveries provide a solid foundation for crafting targeted plans and rules to tackle mental health issues and decrease suicide rates, especially among specific groups of people. Knowing how money, development, and the characteristics of different groups influence each other gives important insights for creating effective strategies in mental health and well-being programs.''', fontsize=16, ha='left', va='bottom', color='#4B0082', wrap=True, bbox=dict(facecolor='#F5F5DC', edgecolor='#E6E6FF', boxstyle='round,pad=1.5'))
# Add student information
fig.text(0.98, 0.95, 'Student Name: Fahasena Faisal\nStudent ID: 21068198\n',
         fontsize=18, ha='right', va='top', color='#4B0082')

# Save the figure
plt.savefig("21068198.png", dpi=300, bbox_inches='tight')
