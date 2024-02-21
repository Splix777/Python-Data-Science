# pimp_image.py


import numpy as np
import matplotlib.pyplot as plt


def main():
    '''
    Prints the shape of an image and displays the image
    it then slices a portion of the image and prints the new shape
    and displays the pimped out image. we can choo

    Args:
    None

    Returns:
    None
    '''
    pass


def ft_invert(image: np.array) -> None:
    '''
    Inverts the image. Inversion is done manually by subtracting
    the pixel value from 255 to get the inverted image.

    Restriction:
    invert: =, +, -, *

    Args:
    image: numpy array

    Returns:
    None
    '''
    # Invert the image
    inverted_image = 255 - image

    # Display the image
    _print_img_info("Inverted Image:", inverted_image, "Inverted Image")


def ft_red(image: np.array) -> None:
    '''
    Displays the red channel of the image. The red channel is
    displayed by setting the green and blue channels to 0.

    Restriction:
    red: =, *

    Args:
    image: numpy array

    Returns:
    None
    '''
    # Display the red channel of the image
    red_image = image.copy()
    red_image[:, :, 1] = 0
    red_image[:, :, 2] = 0

    # Display the image
    _print_img_info("Red Channel:", red_image, "Red Channel")


def ft_green(image: np.array) -> None:
    '''
    Displays the green channel of the image. The green channel is
    displayed by setting the red and blue channels to 0.

    Restriction:
    green: =, -

    Args:
    image: numpy array

    Returns:
    None
    '''
    # Display the green channel of the image
    green_image = image.copy()
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0

    # Display the image
    _print_img_info("Green Channel:", green_image, "Green Channel")


def ft_blue(image: np.array) -> None:
    '''
    Displays the blue channel of the image. The blue channel is
    displayed by setting the red and green channels to 0.

    Restriction:
    blue: =

    Args:
    image: numpy array

    Returns:
    None
    '''
    # Display the blue channel of the image
    blue_image = image.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0

    # Display the image
    _print_img_info("Blue Channel:", blue_image, "Blue Channel")


def ft_grey(image: np.array) -> None:
    '''
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
    '''
    # Convert the image to grey scale
    grey_image = image.copy()
    grey_image[:, :, 0] = grey_image[:, :, 0] // 3
    grey_image[:, :, 1] = grey_image[:, :, 1] // 3
    grey_image[:, :, 2] = grey_image[:, :, 2] // 3
    grey_image = grey_image.sum(axis=2)

    # Display the image
    _print_img_info("Grey Image:", grey_image, "Grey Image")


def _print_img_info(message: str, img: np.array, title: str) -> None:
    '''
    Takes in an image and prints its shape and displays the image

    Args:
    message: string
    image: numpy array
    title: string

    Returns:
    None
    '''
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
    main()
