# callLimit.py


def call_limit(limit: int):
    """
    Decorator allowing a function to be called a limited number of times.

    Args:
    limit: int - The maximum number of times the function can be called.

    Returns:
    None

    """
    count = 0

    def call_limiter(function):
        """
        Decorator allowing a function to be called a limited number of times.
        """
        def limit_function(*args: any, **kwargs: any):
            """
            Decorator allowing a function to be called a limited number of time
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            print(f'Error: {function} call too many times')
            return None
        return limit_function

    return call_limiter


if __name__ == '__main__':
    @call_limit(3)
    def f():
        print("f()")

    @call_limit(1)
    def g():
        print("g()")

    for _ in range(3):
        f()
        g()
