"""
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

key1 = input("please give the name of the album you are looking for: ")


if key1 in dict:
    print(f"The author of {key} jest {dict[key]}")
else:
    print("brak danych")






















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