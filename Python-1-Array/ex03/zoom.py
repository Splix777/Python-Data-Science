# zoom.py

import numpy as np
import matplotlib.pyplot as plt

from numpy import array as Array
from load_image import ft_load


def zoom_image(
        image: np.array = ft_load('animal.jpg'),
        new_shape: tuple = (400, 400, 1),
        ) -> Array:
    """
    Takes in an image and returns a zoomed image

    Args:
    image: numpy array
    new_shape: tuple
    start: tuple
    end: tuple

    Returns:
    numpy array
    """
    try:
        if image is None:
            raise FileNotFoundError(f"Error: File not found - {image}")

        print_img_info(
            "The shape of image is:",
            image,
            "Original Image")

        # zoomed_image = image[:400, :400, :1]
        zoomed_image = image[:new_shape[0], :new_shape[1], :new_shape[2]]

        print_img_info(
            "New shape after slicing:",
            zoomed_image,
            "Zoomed Image")

    except Exception as e:
        print(f"Error: {e}")


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


if __name__ == "__main__":
    zoom_image()
    # other_image = ft_load('4k.jpg')
    # zoom_image(other_image,(400, 400, 1))
