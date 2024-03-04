# load_csv.py


import os
import pandas as pd
from pandas import DataFrame


def load(path: str, debug: bool = False) -> DataFrame | None:
    """
    Loads a csv file into a pandas dataframe.

    Args:
    path: str

    Returns:
    pd.DataFrame
    """
    try:
        csv_shape = pd.read_csv(
            os.path.join(os.path.dirname(__file__), path)).shape
        if debug:
            print(f'Loading dataset of dimensions {csv_shape}')
        return pd.read_csv(os.path.join(os.path.dirname(__file__), path))
    except (FileNotFoundError, NotADirectoryError) as e:
        if debug:
            print(f'Error: {e}')
        return None


if __name__ == '__main__':
    print(load('life_expectancy_years.csv'))
