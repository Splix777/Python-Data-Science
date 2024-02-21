# zoom.py


import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    '''
    Prints the shape of an image and displays the image
    it then slices a portion of the image and prints the new shape
    and displays the new zoomed image

    Args:
    None

    Returns:
    None
    '''
    try:
        # Load the image
        image = ft_load('animal.jpg')

        # Check if the image is loaded successfully
        if image is None:
            raise FileNotFoundError(f"Error: File not found - {image}")

        _print_img_info(
            "The shape of image is:",
            image,
            "Original Image")

        # Zoom into the image (slicing a portion)
        zoomed_image = image[:400, :400, :1]

        _print_img_info(
            "New shape after slicing:",
            zoomed_image,
            "Zoomed Image")

    except Exception as e:
        print(f"Error: {e}")


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
