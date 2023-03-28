#1. Dodawanie na końcu.

my_list =[1, 2, 3]
my_list.append(4)
print(my_list)
#[1, 2, 3, 4]



#2. Wydłużanie na końcu.

my_list =[1, 2, 3]
my_list.extend([4,5,6])
print(my_list)
#[1, 2, 3, 4, 5, 6]



#3. insert umeiszczanie elementu w konkretnym miejscu.

my_list =[1, 2, 3]
my_list.insert(1,4)
print(my_list)
#[1, 4, 2, 3]



#4.remove usuniecie pierwszego wskazanego elementu.

my_list =[1, 2, 3, 2]
my_list.remove(2)

print(my_list)
#[1, 3, 2]



#5.pop() usunięcie i zwórcenie konkretnego elementu z lsity

my_list =[1, 2, 3, 4]
popped_element = my_list.pop(1)

print(my_list)
#.[1, 3, 4] usunięcie elementu z pozycji nr 1 czyli drugiego od lewej jest nim (2)
print(popped_element)
#2 



#6 index() zwrocenie indexu danego elementu pierwszego od lewej 
my_list =[1, 2, 3, 4]
index_of_two = my_list.index(2)
print(index_of_two)
#1




#7 count() metoda zwraca numer ile razy dany element był w danej liście.

my_list =[1, 2, 3, 2, 4, 2]
count_of_two = my_list.count(2)

print(count_of_two)
# 3




#8 sort()metoda sortowanie rosnące.
my_list = [3, 1, 2, 5, 4]
my_list.sort()

print(my_list)
#[1, 2, 3, 4, 5]



#9 reverse() sortowanie malejące

my_list = [1, 2, 3, "one", "two"]
my_list.reverse()

print(my_list)
#['two', 'one', 3, 2, 1]



#10 copy płytka kopia bez zmian w oryginale.

my_list = [1,2,3]
my_list_copy =my_list.copy()

print(my_list)
print(my_list_copy)

my_list_copy.append(4)

print(my_list)
print(my_list_copy)

#[1, 2, 3]
#[1, 2, 3, 4]



#11 update aktualizacja elemnetu na danej pozycji w liscie

my_list = [1, 2, 3, 4, 5]
my_list[2] = 10

print(my_list)
#[1, 2, 10, 4, 5] na pozycji w nawiasie kwadratowym w lsite włacza sie element



#12 sort(reverse =True/False)metoda sortowanie rosnące.

my_list = [3, 1, 2, 5, 4]
my_list.sort(reverse= True)

print(my_list)
#[5, 4, 3, 2, 1]



#13 print(len(list)) metoda sortowanie rosnące.

my_list = [3, 1, 2, 5, 2, 4]
print(len(my_list))

#6 jest 6 elementów




#14 lista.pop(len(lista) -1) usuniecie ostatniego elementu

my_list = [3, 1, 2, 5, 2, 4]
print(len(my_list))
#6
my_list.pop(len(my_list)-1)
print(my_list)

print(len(my_list))
#5



#15 max i min el.listy

my_list = [3, 1, 2, 5, 2, 4]

print(max(my_list))

#max wartośc 5
print(min(my_list))

#min wartośc 5



#16 lista.insert(a,b) na pozycję a wstaw b

my_list = [3, 1, 2, 5, 2, 4]

my_list.insert(0,100)
print(my_list)

#[100, 3, 1, 2, 5, 2, 4]



#BONUS! Python slicing for string!!!


print("word"[::-1]) #pierwsze ":" nie ma pozycji startu lecimy od poczatku, drugie ":" nie ma endu czyli lecimy domyślnie od końca, -1 to step od końca po jednej literce.
#wynik to: drow

 




