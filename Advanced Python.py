'''
List comprehensions
'''

# e.g.
import random

my_list = [random.randint(1, 1000) for i in range(1, 13)]
print(my_list)

'''
Decorators
'''

'''
What if we want to add some further functionality in certain function by using another function?
Here we can use a decorator function to get through the problem in a neat way. Let's see how it works
with an example.
'''


# e.g.
def title_decorator(print_value_function):
    def wrapper(*args, **kwargs):
        print_value_function(*args, **kwargs)

    return wrapper


@title_decorator
def print_value_function(name, age):
    print(name + " your age is " + str(age) + ".\n")


print_value_function("Symeon", 26)

'''
Lambdas expressions
'''

'''
A lambda expression is a shorthand for defining a function in a one line function code.
'''

'''
Syntax:
name_of_function = lambda variable: actions
'''

# e.g.
contains_a = lambda word: True if 'a' in word else False

# e.g.
long_string = lambda string: True if len(string) > 12 else False

# e.g.
ends_in_a = lambda my_word: True if my_word[-1] == 'a' else False

print(contains_a("Banana"))  # and so on




