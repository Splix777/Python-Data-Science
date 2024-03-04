# DiamondTrap.py
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a King with green eyes and black hair.

    Args:
        name (str): The name of the King.

    Attributes:
        _eyes (str): The color of the King's eyes.
        _hairs (str): The color of the King's hair.

    Methods:
        set_eyes(color): Sets the color of the King's eyes.
        set_hairs(color): Sets the color of the King's hair.
        get_eyes(): Returns the color of the King's eyes.
        get_hairs(): Returns the color of the King's hair.
    """

    def __init__(self, first_name):
        """
        Initializes a new instance of the class.

        Args:
            self: The instance of the class.
            first_name (str): The name of the instance.
        """
        super().__init__(first_name)
        self.eyes = "green"
        self.hair = "black"

    def __str__(self):
        """
        King of the Andals, the Rhoynar, and the First Men,
        Lord of the Seven Kingdoms, and Protector of the Realm

        Returns:
            _type_: _description_
        """
        return f"♔{self.__class__.__name__} {self.first_name}♔"

    def set_eyes(self, color):
        """
        Sets the color of the eyes.

        Args:
            self: The instance of the class.
            color: The color to set for the eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Sets the color of the hair.

        Args:
            self: The instance of the class.
            color: The color to set for the hair.
        """
        self.hair = color

    def get_eyes(self):
        """
        Returns the color of the eyes.

        Args:
            self: The instance of the class.

        Returns:
            The color of the eyes.
        """
        return self.eyes

    def get_hairs(self):
        """
        Returns the color of the hair.

        Args:
            self: The instance of the class.

        Returns:
            The color of the hair.
        """
        return self.hair
