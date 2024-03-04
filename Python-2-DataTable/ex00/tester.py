from load_csv import load

try:
    print(load('life_expectancy_years.csv', debug=True))
except FileNotFoundError as e:
    print(f'Error: {e}')
