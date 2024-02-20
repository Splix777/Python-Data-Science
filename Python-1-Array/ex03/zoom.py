# zoom.py


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    try:
        # Load the image
        image = cv2.imread(
            os.path.join(os.path.dirname(__file__),
                         "animal.jpg"))

        # Check if the image is loaded successfully
        if image is None:
            print("Error: File not found")
            return

        _print_img_info("The shape of image is:", image, "Original Image")
        # Zoom into the image (slicing a portion)
        zoomed_image = image[:400, :400, :1]
        _print_img_info(
            "New shape after slicing:", zoomed_image, "Zoomed Image"
        )
    except Exception as e:
        print(f"Error: {e}")


def _print_img_info(arg0, arg1, arg2):
    # Print information about the image
    print(arg0, arg1.shape, f'or ({arg1.shape[0]}, {arg1.shape[1]})')
    print(np.array(arg1))

    # Display the original image
    try:
        plt.imshow(cv2.cvtColor(arg1, cv2.COLOR_BGR2RGB))
        plt.title(arg2)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
