# new_student.py

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    This function generates a random id for a student.

    Returns:
    str: a random id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    This class represents a student.

    Attributes:
    name: str
    surname: str
    active: bool
    login: str
    id: str

    Methods:
    __post_init__: initializes the object
    """
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        This method initializes the object.
        """
        self.login = self.name[0].upper() + self.surname.lower()
        self.active = True


if __name__ == "__main__":
    student = Student(name='Edward', surname='Agle')
    print(student)
