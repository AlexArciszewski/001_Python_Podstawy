# def mul_I(first):
#     def mul_II(second):
#         return first * second
#     return mul_II
# mul_I_3 = mul_I(3)
# print(type(mul_I_3))
# print(mul_I_3(5))
# print(mul_I_3(10))


#
# def person_grades(arr):
#     def calculate_avg_grades(sum_of_grades, no_grades):
#         avg_grades = sum_of_grades / no_grades
#         print(avg_grades)
#
#     total_sum = sum(arr)
#     no_of_grades = len(arr)
#
#     calculate_avg_grades(total_sum, no_of_grades)
#
#
# person_grades([5, 3, 3, 3, 5])


def menu():
    print("Menu")

def add_to_list():
    print("ddoaje do listy")


def remove_from_list():
    print("Usuwam z listy")

from typing import Callable

options: dict[int, Callable] = {
    1: menu,
    2: add_to_list,
    3: remove_from_list,
}

user_choice = int(input("Podaj swoj wybor"))

#if user_choice in options:
options.get(user_choice)

# else:
#     print("Invalid option")

