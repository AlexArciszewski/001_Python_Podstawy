
#1.Find all of the numbers from 1-1000 that are divisible by 7.add()

from shlex import split


for i in range(1,1001):
    if i % 7== 0:
        print(i)
        
l =[]
l= [i for i in range(1,1001) if i % 7== 0]
print(l)
l.append(i)
print(l)
#2.Find all of the numbers from 1-1000 that have a 3 in them

Li = []
for i in range(1,1001):
    if "3" in str(i): #jeśli dana cyfra czy litera ma bć w elemencie listy to robimy z tych elementów stringa i sprawdzamy czy string czyli "cygra" jest w str(i)
        Li.append(i)
print(Li)
Lis =[]
sentence = "Chyba znowu zablokował się tłoczek w zacisku tylnym mustanga"
for letter in sentence:
    if letter == " ":
        Lis.append(letter)
print(Lis)
print(Lis.count(" "))

List=[letter for letter in sentence if letter == " "]
print(List)
print(List.count(" "))

some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
spaces = [s for s in some_string if s == ' ']
print(len(spaces))
print(some_string.count(" "))

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
# Przy użyciu warunkowego list comprehension stwórz listę zawierającą wspólne elementy listy a i b
#list_common = ?

list_common =[]
for number11 in list_a:
    if number11 in list_b:
        list_common.append(number11)
print(list_common)

list_common2 =[number11 for number11 in list_common if number11 in list_b]
print(list_common2)


## Przy użyciu warunkowego list comprehension stwórz listę zawierającą podzielne przez 7 liczby z zakresu <a, b> (a, b wprowadzone przez użytkownika)
#divisible = ?

x = int(input("podaj pierwsza liczba: " ))
y = int(input("podaj pierwsza liczba: " ))
bucket =[]
for number12 in range(x,y):
    if number12 % 7 ==0:
        bucket.append(number12)
print(bucket)
bucket3 = [number12 for number12 in range(x,y) if number12 % 7 ==0]
print(bucket3)

#Create a list of all the consonants in the string “Yellow Yaks like yelling 
# and yawning and yesturday they yodled while eating yuky yams”


myList=[]
string22 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print(string22.split(" "))
myList2 =(string22.split(" "))
print("List from string:",myList2)
#myList.append(string22.split(" "))
#(myList)


#Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). 
#Result would look like (index, value), (index, value)

messyList =["hi", 4, 8.99, "apple", ("t,b","n")]
for index, item in enumerate(messyList):
    print(index,item)
    
    

#enumerate przyklad krotka odp;[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]
mylist = ['A', 'B' ,'C', 'D']
e_list = enumerate(mylist)
print(list(e_list))
#enumerate przyklad krotka [(2, 'A'), (3, 'B'), (4, 'C'), (5, 'D')]
mylist = ['A', 'B' ,'C', 'D']
e_list = enumerate(mylist,2)
print(list(e_list))



mylist = ['A', 'B' ,'C', 'D']

for i in enumerate(mylist):
  print(i)
  print("\n")

print("Using startIndex as 10")    

for i in enumerate(mylist, 10):
  print(i)
  print("\n")
  
#0, 'A')
#(1, 'B')
#(2, 'C')
#(3, 'D')

#Using startIndex as 10
#(10, 'A')
#(11, 'B')
#(12, 'C')
#(13, 'D')



#Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4,]
list_b = [2, 3, 4, 5]
list_c =[]
for number33 in list_a:
    if number33 in list_b:
        list_c.append(number33)
print(list_c)
list_c =[number33 for number33 in list_a if number33 in list_b]
print(list_c)

#Get only the numbers in a sentence like 
# ‘In 1984 there were 13 instances of a protest with over 1000 people attending’

string101 ="In 1984 there were 13 instances of a protest with over 1000 people attending"
listNumbers=[]
listWords = string101.split(" ")
print(listWords)
for number in listWords:
    print(number)
    if "1" in str(number):
        listNumbers.append(number)
print(listNumbers)

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. 
# Result would look like ‘odd’,’odd’, ‘even’

listaNumerow =[]
for i in range(20):
    if i % 2 ==0:
        print("even")
        listaNumerow.append("even")
    else:
        print("odd")
        listaNumerow.append("odd")
print(listaNumerow)    

listaNumerow2 =[i for i in range(20) if i % 2 ==0]
print(listaNumerow2)
#Produce a list of tuples consisting of only the matching numbers in these lists:
# list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. 
# Result would look like (4,4), (12,12)


list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
list_c =[]
list_d =[]
for number in list_a:
    if number in list_b:    
        list_c.append(number)
print(list_c)
for number in list_b:
    if number in list_c:    
        list_d.append(number)
print(list_d)
list_d.sort()
print(list_d)

for x in zip(list_c, list_d):
    print(x)
    

list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
list_c =[]
list_b.sort()
for number in list_a:
    if number in list_b:
        list_c.append(number)
print(list_c)
for number2 in list_c:
    print(number2)
list_c =list_d
print(list_d)
list_e =enumerate(list_d,number) 
print(list(list_e))
[(i, i) for i in list_a if i in list_b]
#mam [(0, 1), (1, 2), (2, 7)] :/

#Find all of the words in a string that are less than 4 letters
listaa =[]
zdanie ="Find all of the words in a string that are less than 4 letters"
print(zdanie.split(" "))

listaa.append(zdanie.split(" "))
print(listaa)



list_c = []
list_c = [x for x in range(1,1000) if x % 5 == 0]
print(list_c)