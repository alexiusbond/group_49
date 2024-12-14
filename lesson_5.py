# import random
from email.policy import default
from random import randint, choice as get_random_element

import emoji
from termcolor import cprint
from decouple import config

from utilities import calculator as calc
from utilities.templates import Person

print(randint(1, 100))
print(get_random_element([1, 2, 3, 4, 5]))

print(calc.multiplication(8, 4))
my_friend = Person("Jim", 40)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize("Python is fun :red_heart:"))

file_path = config("FILE_PATH")
print(file_path)

commented = config("COMMENTED", default=0, cast=int)
print(commented*3)