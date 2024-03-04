# load_image.py
import os

import numpy as np

import matplotlib.pyplot as plt
from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Takes in a path to an image and returns the image as a numpy array

    Args:
    path: string

    Returns:
    numpy array

    Example:
    path = 'path/to/image.jpg'
    print(ft_load(path))

    Output:
    [[[19 42 83]
    [23 42 84]
    [28 43 84]
    ...
    [ 0 0 0]
    [ 1 1 1]
    [ 1 1 1]]]
    """
    try:
        if not path.endswith('.jpg') and not path.endswith('.jpeg'):
            raise ValueError('File is not a .jpg or .jpeg file')

        img = Image.open(os.path.join(os.path.dirname(__file__), path))

        return np.array(img)
    except (FileNotFoundError, ValueError) as e:
        # If the file is not found, print the error and return an empty list
        print(f'Error: {e}')
        return None


def print_img_info(message: str, img: np.array, title: str) -> None:
    """
    Takes in an image and prints its shape and displays the image

    Args:
    message: string
    image: numpy array
    title: string

    Returns:
    None
    """
    # Print information about the image
    print(f"{message} {img.shape} or ({img.shape[0]}, {img.shape[1]})")
    print(np.array(img))

    # Display the image
    try:
        # Squeeze to handle single-channel images
        plt.imshow(img.squeeze(), cmap='gray')
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    try:
        picture_info = ft_load('animal.jpg')
        print(f'The shape of the image is: {picture_info.shape}',
              f'{picture_info}',
              sep='\n'
              )
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
