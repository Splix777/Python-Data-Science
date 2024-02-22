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

    def __init__(self, name):
        """
        Initializes a new instance of the class.

        Args:
            self: The instance of the class.
            name (str): The name of the instance.

        Attributes:
            _eyes (str): The color of the eyes.
            _hairs (str): The color of the hair.
        """
        super().__init__(name)
        self._eyes = "green"
        self._hairs = "black"

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
        self._eyes = color

    def set_hairs(self, color):
        """
        Sets the color of the hair.

        Args:
            self: The instance of the class.
            color: The color to set for the hair.
        """
        self._hairs = color

    def get_eyes(self):
        """
        Returns the color of the eyes.

        Args:
            self: The instance of the class.

        Returns:
            The color of the eyes.
        """
        return self._eyes

    def get_hairs(self):
        """
        Returns the color of the hair.

        Args:
            self: The instance of the class.

        Returns:
            The color of the hair.
        """
        return self._hairs
