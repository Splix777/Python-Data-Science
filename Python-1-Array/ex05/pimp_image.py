# pimp_image.py


import numpy as np

from load_image import print_img_info, ft_load


def ft_invert(image: np.array) -> None:
    """
    Inverts the image. Inversion is done manually by subtracting
    the pixel value from 255 to get the inverted image.

    Restriction:
    invert: =, +, -, *

    Args:
    image: numpy array

    Returns:
    None
    """
    # Invert the image
    inverted_image = 255 - image

    # Display the image
    print_img_info("Inverted Image:", inverted_image, "Inverted Image")


def ft_red(image: np.array) -> None:
    """
    Displays the red channel of the image. The red channel is
    displayed by setting the green and blue channels to 0.

    Restriction:
    red: =, *

    Args:
    image: numpy array

    Returns:
    None
    """
    # Display the red channel of the image
    red_image = image.copy()
    red_image[:, :, 1] = 0
    red_image[:, :, 2] = 0

    # Display the image
    print_img_info("Red Channel:", red_image, "Red Channel")


def ft_green(image: np.array) -> None:
    """
    Displays the green channel of the image. The green channel is
    displayed by setting the red and blue channels to 0.

    Restriction:
    green: =, -

    Args:
    image: numpy array

    Returns:
    None
    """
    # Display the green channel of the image
    green_image = image.copy()
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0

    # Display the image
    print_img_info("Green Channel:", green_image, "Green Channel")


def ft_blue(image: np.array) -> None:
    """
    Displays the blue channel of the image. The blue channel is
    displayed by setting the red and green channels to 0.

    Restriction:
    blue: =

    Args:
    image: numpy array

    Returns:
    None
    """
    # Display the blue channel of the image
    blue_image = image.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0

    # Display the image
    print_img_info("Blue Channel:", blue_image, "Blue Channel")


def ft_grey(image: np.array) -> None:
    """
    Converts the image to grey scale. We have to manually
    calculate the grey scale value for each pixel. Due to
    exercise restrictions, we can't use the numpy function
    np.dot() to convert the image to grey scale.

    Restriction:
    grey: =, /

    Args:
    image: numpy array

    Returns:
    None
    """
    # Convert the image to grey scale
    grey_image = image.copy()
    grey_image[:, :, 0] = grey_image[:, :, 0] // 3
    grey_image[:, :, 1] = grey_image[:, :, 1] // 3
    grey_image[:, :, 2] = grey_image[:, :, 2] // 3
    grey_image = grey_image.sum(axis=2)

    # Display the image
    print_img_info("Grey Image:", grey_image, "Grey Image")


if __name__ == "__main__":
    # Load the image
    array = ft_load("landscape.jpg")

    # Invert the image
    ft_invert(array)

    # Display the red channel of the image
    ft_red(array)

    # Display the green channel of the image
    ft_green(array)

    # Display the blue channel of the image
    ft_blue(array)

    # Convert the image to grey scale
    ft_grey(array)

    # Print the docstring of the ft_invert function
    print(ft_invert.__doc__)