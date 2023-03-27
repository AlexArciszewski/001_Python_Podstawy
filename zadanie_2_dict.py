"""
Zad 2. 
Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o nowych albumach do słownika. Program ma zawierać proste menu.

Zad 1. 
Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
• wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
• pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika. 

Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

{'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
"""



dict = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

print("Hello to my album holder")

for key in dict:
    print(key)
    #print(dict[key])

a = input("What do U want? write add or del ")
if a == "add":
    print(" U can add new album and author to the database")
    value2 = input("Give me the author: ")
    key2 = input("Give me the name of the album: ")
    dict2 ={value2:key2}
    dict.update(dict2)
    print(dict)
elif a == "del":
    print("U can delete album! ")
    key =input("Give me the name of the album: ")
    if key in dict:
        print(f"The author of {key} jest {dict[key]}")
        dict.pop(key)
        print(dict)
    else:
        print("brak danych")
else:
    print("Operation forbidden")    






















"""
#dostaję klucze ze slownika
for keys in dict:
    print(keys)

#dostaję:
#The Sensual World
#Shaday
#Achtung Baby
#Aion
#Invisible Touch
print("\n")
print(dict.keys())
#dostaję  listę kluczy ze słownika albumy    dict_keys(['The Sensual World', 'Shaday', 'Achtung Baby', 'Aion', 'Invisible Touch'])
print("\n")
print(dict.values())
#dostaję  listę wartości ze słownika wykonawcy    dict_values(['Kate Bush', 'Ofra Haza', 'U2', 'Dead Can Dance', 'Genesis'])

print("\n")
print("\n")
print("\n")


print("Zadanie 1")
dict = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
print(dict.keys())
print(dict.values())    
print("band srearch by album ver.1.02")
key1 = input("Please give the name of the album: ")
print(f"You chose the album: {key1}")
if key1 in dict:
    print("The album is in our database")
    print(f"The Band is: {dict[key1]}") 
    
else:
    print("incorrect data")  
"""