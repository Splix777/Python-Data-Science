# new_student.py

import string
import secrets


from dataclasses import dataclass, field


def generate_id() -> str:
    """
    This function generates a random id for a student.

    Returns:
    str: a random id
    """
    return "".join(secrets.choice(string.ascii_lowercase) for _ in range(15))


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
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        This method initializes the object.
        """
        if not isinstance(self.name, str) or not isinstance(self.surname, str):
            raise TypeError("Name and surname must be strings.")
        if len(self.name) < 2 or len(self.surname) < 2:
            raise ValueError("Name and surname must be at least 2 characters long.")
        if not self.name.isalpha() or not self.surname.isalpha():
            raise ValueError("Name and surname must contain only alphabetic characters.")
        self.login = self.name[0].upper() + self.surname.lower()
        self.active = True


if __name__ == "__main__":
    student = Student(name='Edward', surname='Agle')
    print(student)
