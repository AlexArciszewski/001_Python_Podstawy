

def menu():
    print("menu")
    
def add_to_list():
    print("dodaje do listy")
    
def remove_from_list():
    print("Usuwam z listy")

from typing import Callable

options: dict[int, Callable] = {
    1: menu,
    2: add_to_list,
    3: remove_from_list, 
           
           
           }

user_choice = int(input("Podaj swój wybór: "))
#opcja nr 1
#print(options.get(user_choice, "Invalid Option"))

#opcja nr 2
#if user_choice in options:
#    print(type(options.get(user_choice)))
#else:
#    print("Invalid Option")

#opcja nr 3
if user_choice in options:
    options.get(user_choice)()
else:
    print("Invalid Option")