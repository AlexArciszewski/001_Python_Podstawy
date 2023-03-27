
"""
Zad 4. 
Przekształć poniższy tekst, dopisując w nawiasach do polskich nazw ptaków ich łacińskie odpowiedniki.

Skorzystaj w tym celu ze słownika zawierającego następujące elementy:

{'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula', 'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major', 'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris', 'szczygiel' : 'Carduelis carduelis', 'szpak' : 'Sturnus vulgaris', 'kopciuszek' : 'Phoenicurus ochruros'}

Tekst:
W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel.
"""

string = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."



dict = {'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula', 'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major', 'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris', 'szczygiel' : 'Carduelis carduelis', 'szpak' : 'Sturnus vulgaris', 'kopciuszek' : 'Phoenicurus ochruros'}


for key, value in dict.items():
    string = string.replace(key, key+"("+ value +")")
    
print(string)







""" 
for key in dict:
    print(key)
    print(dict[key])

list = string.split()
print(list)
list1 =[]
list2=[]
for key in dict:
    list1.append(key)
    list2.append(dict[key])
print(list,"\n\n\n", list1,"\n\n", list2,"\n")

for word in list:
    print(word)

for word1 in list1:
    print(word1)

for word2 in list2:
    print(word2)

for word in list:
    if word == word1:
        list.append(word2)
print(list)




"""

        














"""
for key in dict:
    print(key)      ##kos wilga rudzik kukulka pleszka bogatka drozd zieba dzwoniec szczygiel szpak kopciuszek          
for key in dict:
    print(dict[key]) #Turdus merula Oriolus oriolus Erithacus rubecula Cuculus canorus Phoenicurus phoenicurus Parus major Turdus philomelos Fringilla coelebs Chloris chloris Carduelis carduelis Sturnus vulgaris
tring_divided = string.split()
print(string_divided)
count = Counter(text)
print(count) # tak liczy liczbę znaków
counts ={}
text2 = text.split()  #podział na słowa
for word in text2:      #dla slowa w tekscie jak slowo w slowniku to wartość po kluczu word slownika count  = wartośc +1
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
print(counts)
"""












