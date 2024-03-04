# S1E7.py

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def die(self):
        """Method to kill the Baratheon character"""
        self.is_alive = False

    def __str__(self):
        """String representation of the Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Representation of the Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def die(self):
        """Method to kill the Lannister character"""
        self.is_alive = False

    def __str__(self):
        """String representation of the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Representation of the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Class method to create a Lannister character"""
        return cls(first_name, is_alive)
