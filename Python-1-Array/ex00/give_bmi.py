# give_bmi.py

import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Takes in a list of heights and weights and returns a list of BMIs

    Args:
    height: list of heights in meters
    weight: list of weights in kilograms

    Returns:
    list of BMIs

    Example:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))

    Output:
    [56.6, 29.0] <class 'list'>
    """
    try:
        # Check if the lists have the same size
        if len(height) != len(weight):
            raise ValueError("Input lists must have the same size")

        # Check if the elements are numeric (int or float)
        if (
            not all(isinstance(h, (int, float)) for h in height) or
            not all(isinstance(w, (int, float)) for w in weight)
        ):
            raise TypeError("All elements in input lists must be int or float")

        # Convert input lists to NumPy arrays
        height = np.array(height)
        weight = np.array(weight)

        # Check for zero division
        if (height == 0).any():
            raise ZeroDivisionError("Height cannot be zero")

        # Perform BMI calculation
        return np.round(weight / np.square(height), 5).tolist()
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f'Error: {e}')
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Takes in a list of BMIs and a limit and returns a list of booleans

    Args:
    bmi: list of BMIs
    limit: limit for BMI

    Returns:
    list of booleans

    Example:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(apply_limit(bmi, 26))

    Output:
    [True, True]
    '''
    try:
        if bmi and limit:
            # Check if the elements are numeric (int or float)
            if not all(isinstance(b, (int, float)) for b in bmi):
                raise TypeError("bmi must be a list of int or float")

            # Check if the limit is an int
            if not isinstance(limit, int):
                raise TypeError("Limit must be an int")

            return [bmi > limit for bmi in bmi]
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')
        return []


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
