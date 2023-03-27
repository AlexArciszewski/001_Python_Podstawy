
""" 
Zad 3. 
Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście.

"Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, 
suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, 
and nothing more."

"""

from collections import Counter

text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
#print(text.lower())
print(text.lower().replace(",","").replace(".","").replace("-", ""))

print(len(text))

count = Counter(text)
print(count) # tak liczy liczbę znaków
counts = {}

text2 = text.split()  #podział na słowa
for word in text2:      #dla slowa w tekscie jak slowo w slowniku to wartość po kluczu word slownika count  = wartośc +1
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
print(counts)











