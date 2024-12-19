#make sure to install pandas before running
import pandas as pd
import matplotlib.pyplot as plt

# Load data files
debt_data = pd.read_csv('central_government_debt.csv', encoding='ISO-8859-1')
gdp_data = pd.read_csv('canada_gdp.csv')

# Function to create bar chart of top 5 countries with the highest debt in 2022
def top_5_countries_2022(data):
    debt_2022 = data[['country_name', '2022']].dropna()
    debt_2022.columns = ['Country', 'DebtRate2022']
    top_5 = debt_2022.nlargest(5, 'DebtRate2022')

    plt.figure(figsize=(8, 5))
    plt.bar(top_5['Country'], top_5['DebtRate2022'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Debt Rate in 2022 (%)')
    plt.title('Top 5 Countries with Highest Debt in 2022')
    plt.tight_layout()
    plt.show()

# Function to create a line chart for debt rates over time for selected countries
def line_chart_countries(data, countries):
    selected_data = data[data['country_name'].isin(countries)].set_index('country_name')
    years = list(map(str, range(1950, 2023)))

    plt.figure(figsize=(15,6))  # Increase figure size
    for country in countries:
        plt.plot(years, selected_data.loc[country, years], label=country)
    
    plt.xlabel('Year')
    plt.ylabel('Debt Rate (%)')
    plt.title('Debt Rate Over Time for Selected Countries')
    plt.legend(loc='upper left')  # Adjust the location as needed

    
    # Rotate and adjust x-axis labels
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()



# Scatter plot for Debt Rate vs. GDP for Canada
def debt_vs_gdp_scatter(debt_data, gdp_data, country_name):
    canada_debt = debt_data[debt_data['country_name'] == country_name].iloc[0]
    years = list(map(str, range(1990, 2023)))
    debt_rates = canada_debt[years].astype(float).values

    # Extract GDP values from the GDP file
    gdp_values = gdp_data.loc[0, years]  # Extract single row of GDP values
    gdp_values = gdp_values.replace('[\\$,]', '', regex=True).astype(float)  # Remove $, commas

    # Match lengths of GDP and debt rates, in case any years are missing
    min_length = min(len(gdp_values), len(debt_rates))
    gdp_values = gdp_values[:min_length]
    debt_rates = debt_rates[:min_length]
    
    plt.figure(figsize=(10, 5))
    plt.scatter(gdp_values, debt_rates, color='purple')
    plt.xlabel('GDP (USD)')
    plt.ylabel('Debt Rate (%)')
    plt.title(f'Debt Rate vs. GDP for {country_name}')
    plt.tight_layout()
    plt.show()

# Function to create a bar chart for the 10 countries with the lowest debt in 2022
def lowest_10_countries_2022(data):
    debt_2022 = data[['country_name', '2022']].dropna()
    debt_2022.columns = ['Country', 'DebtRate2022']
    lowest_10 = debt_2022.nsmallest(10, 'DebtRate2022')

    plt.figure(figsize=(13, 5))
    plt.bar(lowest_10['Country'], lowest_10['DebtRate2022'], color='lightgreen')
    plt.xlabel('Country')
    plt.ylabel('Debt Rate in 2022 (%)')
    plt.title('Top 10 Countries with Lowest Debt in 2022')
    plt.tight_layout()
    plt.show()

# Call the functions to visualize
top_5_countries_2022(debt_data)
line_chart_countries(debt_data, ['United States', 'Japan', 'India'])
debt_vs_gdp_scatter(debt_data, gdp_data, 'Canada')
lowest_10_countries_2022(debt_data)
