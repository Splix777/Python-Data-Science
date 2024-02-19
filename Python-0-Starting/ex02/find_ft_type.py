# find_ft_type.py

def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    object_name = object_type.__name__

    if object_name in ["list", "tuple", "set", "dict"]:
        print(f'{object_name.capitalize()} : {object_type}')
    elif object_type == str:
        print(f'{object} is in the kitchen : {object_type}')
    else:
        print('Type not found')
    return 42
