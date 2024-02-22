# ft_calculator.py
class calculator:
    """
    A calculator class for performing arithmetic operations between
    a vector and a object. We overload the +, *, - and / operators.

    Calculations (dot product, addition, subtraction) are performed
    on two vectors. The vectors are lists of numbers.

    Decorators:
        @staticmethod
        - A method that does not require access to the instance or class.
        - It does not modify the state of the class or instance
        - We do not need to instantiate the class to use the method.

    Attributes:
        vector (list): The vector on which operations will be performed.

    Methods:
        dotproduct(self, V1: list[float], V2: list[float]) -> None
        - Calculate the dot product of two vectors.

        add_vec(self, V1: list[float], V2: list[float]) -> None
        - Add two vectors.

        sous_vec(self, V1: list[float], V2: list[float]) -> None
        - Subtract two vectors.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            The dot product of the two vectors.
        """
        dot_product = sum(x * y for x, y in zip(V1, V2))
        print(f'Dot product is: {dot_product}')
        return dot_product

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            The sum of the two vectors.
        """
        sum_vec = [x + y for x, y in zip(V1, V2)]
        print(f'Add Vector is: {sum_vec}')
        return sum_vec

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            The difference of the two vectors.
        """
        diff_vec = [x - y for x, y in zip(V1, V2)]
        print(f'Subtract Vector is: {diff_vec}')
        return diff_vec
