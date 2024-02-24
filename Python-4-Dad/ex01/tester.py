from in_out import outer
from in_out import square
from in_out import pow

another_counter = outer(3, square)
print(another_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
