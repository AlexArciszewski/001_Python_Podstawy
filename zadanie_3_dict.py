
""" 
Zad 3. 
Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście.

"Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, 
suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, 
and nothing more."

"""
text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
text2 = text.lower()

print(text2) #tekst  same małe litery
for letter in text2:
    print(letter)

print(text2.replace(",",""))
text3 = text2.replace(",","")
print(text3)
text4 = text3.replace(".","")
text5 = text4.replace("-", "")
print(text5)
text_list = list(text5.split(" "))
print(text_list)

from collections import Counter

dict1 = dict(Counter(text_list))
print(dict1)

list_words =[]
list_values =[]
for key in dict1.keys():
    print(key,dict1[key]) #słowo to key a value to dict1[key] czyli wartośc to słownik po kluczu :)

list_words=list(dict1.keys())
print(list_words)
list_values =list(dict1.keys())
print(list_values)
# Zadanie zrobione ale: chciałem zrobić listę krotek(slowo ,ilosc powtorzen) ale nie wyszło.....
















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