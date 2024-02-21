# ft_calculator.py
class calculator:
    """
    A calculator class for performing arithmetic operations between
    a vector and a object. We overload the +, *, - and / operators.

    Attributes:
        vector (list): The vector on which operations will be performed.

    Methods:
        __init__(self, vector): Init the calculator with the provided vector.

        __add__(self, object): + a object value to each element of the vec.

        __mul__(self, object): * each element of the vector by a object value.

        __sub__(self, object): - a object value from each element of the vector

        __truediv__(self, object): / each element of the vector by a object val
    """

    def __init__(self, vector: list) -> None:
        """
        Initializes the calculator with the provided vector.

        Args:
            vector (list): The vector on which operations will be performed.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Returns:
            The resulting vector after addition.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return list(self.vector)

    def __mul__(self, object) -> None:
        """
        Returns:
            The resulting vector after multiplication.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return list(self.vector)

    def __sub__(self, object) -> None:
        """
        Returns:
            The resulting vector after subtraction.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return list(self.vector)

    def __truediv__(self, object) -> None:
        """
        Returns:
            The resulting vector after division.
            None if the object value is 0 or an exception is raised.

        Raises:
            ZeroDivisionError: If the object value is 0.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return list(self.vector)
        except ZeroDivisionError as e:
            print(f"{ZeroDivisionError.__name__}:", e)
            return None
        except Exception as e:
            print(f"{Exception.__name__}:", e)
            return None
