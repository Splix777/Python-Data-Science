# aff_pop.py

import matplotlib.pyplot as plt
from load_csv import load


def proc_data(population_data):
    '''
    Processes the population string and returns
    the population as an integer.

    Args:
    population_data: string of population data

    Returns:
    population: float of population data
    '''
    if population_data.endswith('B'):
        return float(population_data[:-1]) * 1_000_000_000
    elif population_data.endswith('M'):
        return float(population_data[:-1]) * 1_000_000
    elif population_data.endswith('k'):
        return float(population_data[:-1]) * 1_000
    else:
        return float(population_data)


def plot_population_projections(df, countries):
    '''
    Plots the population projections for the specified countries.

    Args:
    df: DataFrame containing population data
    countries: List of countries to plot

    Returns:
    None
    '''
    try:
        max_population = 0
        for country in countries:
            country_data = df[df['country'] == country]
            if country_data.empty:
                print(f'Error Invalid Country: {country}')
                continue

            years = country_data.columns[1:].astype(int)

            population = [proc_data(pop) for pop in country_data.iloc[0, 1:]]
            max_population = max(max_population, max(population))

            plt.plot(years, population, label=country)

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.xticks(range(1800, 2051, 40))
        plt.xlim(1800, 2050)
        plt.ylabel('Population')
        plt.legend(loc='lower right')
        plt.tight_layout()

        y_ticks = [0, max_population / 2, max_population]
        plt.yticks(y_ticks, [f'{int(pop / 1_000_000)}M' for pop in y_ticks])

        plt.show()

    except FileNotFoundError as e:
        print(f'File not found: {e}')


def main():
    try:
        df = load('population_total.csv')

        # List of countries to plot
        countries_to_plot = [
            'Spain',
            'France',
            'Germany',
            'Italy',
            'United Kingdom',
            'Not a real country',
            ]

        plot_population_projections(df, countries_to_plot)

    except FileNotFoundError as e:
        print(f'File not found: {e}')


if __name__ == "__main__":
    main()
