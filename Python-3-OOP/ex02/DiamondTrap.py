# DiamondTrap.py
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, name):
        super().__init__(name)
        self._eyes = "green"
        self._hairs = "black"

    def set_eyes(self, color):
        self._eyes = color

    def set_hairs(self, color):
        self._hairs = color

    def get_eyes(self):
        return self._eyes

    def get_hairs(self):
        return self._hairs