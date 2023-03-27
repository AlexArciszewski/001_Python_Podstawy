# for loop
l = []
for i in range(10): # 0, 1, 2, 3, 4,..9
    l.append(i ** 2)
print("for loop", l)

# list comprehension
l = [i for i in range(10)] # list(range(10))

l = [i**2 for i in range(10)]
print("comprehension", l)
print("="*20)

# for loop
d = {
  # i: i**2
    0: 0**2,
    1: 1**2,
    2: 2**2,
    3: 3**2
}
d = {}
for i in range(10): # 0, 1, 2, 3, 4,..9
    d[i] = i**2
print(d)

# dict comprehension
#   {key: value for ...}
d = {i: i**2 for i in range(10)}
print(d)

print("="*20)
# set comprehension
s = {i for i in range(10)}
print(s)

print("="*20)
# tuple comprehension
t = (i for i in range(10)) # nie działa! dostajemy generator
t = tuple(t) # musimy zrzutować na tuplę
t = tuple(i for i in range(10)) # to już działa
print(t)

# zbuduj dict {imie : dlugosc_imienia} na podstawie listy
# wykorzystaj dict comprehension
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
d = {name: len(name) for name in names}
print(d)


# podstawowy przykład
l = [i for i in range(10)]

# przekształć kod, by wykorzystywał dict comprehension
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
dziennik = []
# wynik: [(Jerry, 1), (Kramer, 2) ...]
for index, name in enumerate(names, start=1):
    dziennik.append((name, index))

print("="*20)
dziennik = [(name, index) for index, name in enumerate(names, start=1)]

# ZADANIE DOMOWE
# przekształć kod, by wykorzystywał dict comprehension
lista = [6, 5, 4, 3]
lista_poteg = []
# wynik: [0, 5, 8, 9] ponieważ 0*6=0, 1*5=5, 2*4=8...
for index, value in enumerate(lista):
    lista_poteg.append(index*value)

