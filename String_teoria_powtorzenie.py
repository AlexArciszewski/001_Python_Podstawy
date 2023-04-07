name = "aleksander"
print(len(name)) #nawias fioletowy to argument w postaci nazwy zmiennej która sprawdzamy
print(name.capitalize()) #obiekt string ma metody np capitalize(pierwsza duza litera). najpierw zmienna a pózniej po kropce
                         #metoda ta metoda nie przyjmuje argumentów wiec jest(0 na koncu)
print(name.upper()) # duże litery w słowie
print(name.lower()) # małe litery
print(name[0])      #pierwsza litera
print(name[-1])     #ostatnia litera
print(name[0:3])    # trzy litery zaczynając od pierwszej na pozycji zero
print(name[1:])     # wszystkie litery zaczynając od drugiej. Po : nie piszemy nic to idzie do konca
print(name[-3:])    # trzy ostatnie

zdanie = " To jest przypomnienie podstaw programowania z roznych kursow jak udemy, yt i inne."
print(zdanie.split(" ")) #rozdzielenie zdania na wyrazy gdzie rozdielającym znakiemjest spacja Tworzy sie lista

#otrzymamy:['', 'To', 'jest', 'przypomnienie', 'podstaw', 'programowania', 'z', 'roznych', 'kursow', 'jak', 'udemy,', 'yt', 'i', 'inne.']

join_string = " " #zrobienie zdania z listy

print(join_string.join(['To', 'jest', 'przypomnienie', 'podstaw', 'programowania', 'z', 'roznych', 'kursow', 'jak', 'udemy,', 'yt', 'i', 'inne.']))

#otrzymamy: To jest przypomnienie podstaw programowania z roznych kursow jak udemy, yt i inne.


print(name.startswith("a")) #true bo name =aleksander i zaczyna się od a
print(name.startswith("A")) # false bo a a nie A
print(name.endswith("r")) #true bo konczy sie na małe r
print(name.endswith("R")) #false bo konczy sie na małe r

print(name.rstrip("r")) #usuneicie z prawej pierwzego r
print(name.lstrip("a")) #usuneicie zlweje pierwszego a
print(name.strip("a"))
name2 = "ealeksandere"
print(name2.strip("e")) #usuniecie skrajnych liter



name3 =" olo "

print(name3.strip()) #usuneicie nadmiernych spacji


first_name = "Aleksander"
last_name  = "Arciszewski"
print(first_name + " " + last_name) #dodanie stringow

#pocja nr 2 #dodanie stringow
print(join_string.join([first_name,last_name]))


james_bond = 7
print(str(james_bond).zfill(3)) #3 ile znakow mammiec nowy string z zerami
#otrzymamy 007

txt = "Example"
print(txt.find("ple")) #4 pozycja to p i jest w Example.
print(txt.find("le")) #5pozycja to l i odniej się zaczyna
string = "anakonda"
print(string.islower()) #True jeśli są same małe litery
print(string.isupper()) #True jeśli są same duże litery
print(string.istitle()) #True jeśli pierwsza jest duża litera a pozostałe małe
print(string.isspace()) #True jeśli jest wszystkie znaki to spacja
print(string.isalnum()) #True jeśli jesli znaki sa alfanumeryczne a-z i 0-9 nie alfanumeryczna jest spacja !#%&?
print(string.isalpha()) #True jeśli jesli znaki sa z alfabetu
print(string.isascii()) #True jeśli jesli znaki sa ASCII
print(string.isdecimal()) #True jeśli jesli znaki są cyframi [0-9]
print(string.isdigit()) #True jeśli jesli string to liczba [0-9] ulamki False
print(string.isnumeric()) #True jeśli jesli string to liczba [0-9] to co is digit jednak ulamek da True
