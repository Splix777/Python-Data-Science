# NULL_not_found.py

import math


def NULL_not_found(object: any) -> int:
    # print(f'{object.__repr__()}')
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and object is not False:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and not object:
        print(f"Empty: {type(object)}")
    elif isinstance(object, bool) and not object:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
    return 42
