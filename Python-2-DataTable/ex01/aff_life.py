# aff_life.py


import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def draw_line_graph(data, title, x_label, y_label, x_ticks):
    """
    Function that draws a line graph using the data provided.

    Args:
    data: list
    title: str
    x_label: str
    y_label: str
    x_ticks: list

    Returns:
    None
    """
    plt.plot(data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(range(0, len(data), 40), x_ticks)
    plt.show()


def main():
    """
    Program that calls the load function from load_csv.py. Loads
    a csv file and displays the country information of the country
    the users campus is located in. We will then display the
    life expectancy for that country using the pandas dataframe.
    We will display the country information and the life expectancy
    in a pandas line graph.

    Uses the load function from load_csv.py to load the csv file.

    Extracts the country information for the users campus
    df = df[df['country'] == 'Spain']
    df stands for dataframe and we are using the pandas

    We use np.arange to create an array of years from 1800 to 2100
    with a step of 40 years. We then use plt.plot to plot the
    life expectancy for Spain. We then use plt.title to set the
    title of the graph, plt.xlabel to set the x-axis label, and
    plt.ylabel to set the y-axis label. We then use plt.xticks to
    set the x-axis ticks to the years array. Finally, we use
    plt.show to display the graph.
    Args:
    None

    Returns:
    None
    """
    try:
        df = load('life_expectancy_years.csv')
        spain_data = df[df['country'] == 'Spain']
        years = np.arange(1800, 2100, 40)

        draw_line_graph(
            spain_data.iloc[0, 2:].tolist(),
            'Life Expectancy in Spain',
            'Year',
            'Life Expectancy',
            years
        )

    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except KeyError as e:
        print(f'Country not found in the dataset: {e}')


if __name__ == "__main__":
    main()
