""" 
Zadanie 5
Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
Przykładowy input: n = 5
Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""

def number_generator():
    dict = {}
    number = int(input("Please give me the number: "))
    
    for key in range(1, number + 1):
        #print(key)
        value = key**2
        dict[key] = value
    
    print(dict)
    
number_generator()