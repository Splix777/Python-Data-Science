from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
print(Joffrey)
print(Joffrey.__str__.__doc__)

print('Class:', King.__name__)
print(type(Joffrey))
# Base class:
for base_class in King.__bases__:
    print(f'Base Class: {base_class}')
