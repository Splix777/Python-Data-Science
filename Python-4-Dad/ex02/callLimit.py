# callLimit.py


def callLimit(limit: int) -> None:
    count = 0
    def callLimiter(function):

        def limit_function(*args: any, **kwargs: any):
            if count < limit:
                return function()


