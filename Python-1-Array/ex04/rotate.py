# rotate.py


import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    '''
    Prints the shape of an image and displays the image
    it then slices a portion of the image and prints the new shape
    and displays the new rotated image, we can rotate the image by
    90, 180, 270 degrees

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

        _print_img_info("The shape of image is:", image, "Original Image")

        zoomed_image = image[:400, :400, :1]

        # Manually transpose the image
        transposed_image = manual_transpose(zoomed_image, rotate=270)

        _print_img_info(
            "New shape after Transpose:",
            transposed_image, "Manually Transposed Image")

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


def manual_transpose(image: np.array, rotate: int) -> np.array:
    '''
    Takes in an image and returns the transposed image. We
    rotate the image by 90, 180, 270 degrees depending on the
    value of rotate. If rotate is not 90, 180, 270, we return
    the original image

    Args:
    image: numpy array

    Returns:
    numpy array
    '''
    if rotate in {90, 270}:
        transposed_image = np.zeros((
            image.shape[1],
            image.shape[0],
            image.shape[2]),
            dtype=image.dtype)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if rotate == 270:
                    transposed_image[j, i] = image[i, image.shape[1] - j - 1]
                elif rotate == 90:
                    transposed_image[j, i] = image[image.shape[0] - i - 1, j]

        return transposed_image


if __name__ == "__main__":
    main()
