# load_image.py


from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> list:
    '''
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
    '''
    try:
        if not path.endswith('.jpg') and not path.endswith('.jpeg'):
            raise ValueError('File is not a .jpg or .jpeg file')

        # Try to load the image
        img = Image.open(os.path.join(os.path.dirname(__file__), path))

        print(f'The shape of the image is: {np.array(img).shape}')
        print(np.array(img))
        return np.array(img)
    except (FileNotFoundError, ValueError) as e:
        # If the file is not found, print the error and return an empty list
        print(f'Error: {e}')
        return []


def main():
    print(ft_load('landscape.jpg'))


if __name__ == '__main__':
    main()
