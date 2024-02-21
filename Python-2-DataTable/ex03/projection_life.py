# projection_life.py


import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    '''

    '''
    income_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")

    gdp_1900 = income_df['1900']
    life_expectancy_1900 = life_df['1900']
    
    plt.figure(figsize=(10, 6))
    plt.scatter(gdp_1900, life_expectancy_1900)
    plt.title('Life Expectancy vs GDP in 1900')
    plt.xlabel('GDP in 1900')
    plt.ylabel('Life Expectancy in 1900')
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.grid(True)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    '''
    Create a program that calls the load function from the first exercise, loads the files "in-
    come_per_person_gdppercapita_ppp_inflation_adjusted.csv" and "life_expectancy_years.csv",
    and displays the projection of life expectancy in relation to the gross national product of
    the year 1900 for each country.

    Your graph must have a title, a legend for each axis and a legend for each graph.
    You must display the year 1900.
    '''
    main()