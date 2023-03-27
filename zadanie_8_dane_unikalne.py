""" 
Zad 8.
Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
Dla danych:
{ "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
Oczekujemy wyniku:
“S002”, “S009”, “S007”
"""
dict = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }

print(dict["VI"], dict["X"], dict["XI"],)
list = []
for key in dict:
    print(key)

for key in dict:
    print(dict[key])

for key,dict[key] in dict.items():
    print(key +" " + dict[key])
    list.append(key +" " + dict[key])
    
    
print(list)
list_final = []
for key in dict:
    list_final.append(dict[key])
print(list_final)
list_final.pop(len(list_final)-3)       #czy tej i 2 poniższych linii nie można jakoś scalić?
list_final.pop(len(list_final)-3)
list_final.pop(len(list_final)-3)
list_final.pop(0)
print(list_final)