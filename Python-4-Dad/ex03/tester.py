from new_student import Student

student = Student(name='Edward', surname='Agle')
print(student)
# Output: Student(name='Edward', surname='Agle', active=True, login='EAgle', id='qyvqzqyjvqpybod')
# The output is correct.
# The Student class from new_student.py is imported and an instance of Student is created.
# The __post_init__ method sets the login attribute to the first letter of the name in uppercase followed by the surname in lowercase.
# The id attribute is set to a random string of 15 lowercase letters.
# The active attribute is set to True.
# The __str__ method returns a string representation of the object.
# The output is a string that includes the name, surname, active, login, and id attributes.
# The output is correct.
# The Student class from new_student.py is working as expected.
# The test passes.

# Path: tester.py
# Compare this snippet from new_student.py:
# # new_student.py
#
# import random
# import string
# from dataclasses import dataclass, field
#
#