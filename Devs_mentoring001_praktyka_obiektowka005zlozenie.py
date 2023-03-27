""" 
Zad. 5 (DevsMentoring)
Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card). Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond). 
W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii. W Deck znaleźć mają się takie metody jak: shuffle (która może wykorzystywać metodę o tej samej 
nazwie - shuffle - z biblioteki random) oraz deal (która będzie usuwała i zwracała ostatnią kartę z talii).

Podpowiedź:
Talia kart ma się składać z 52 różnych obiektów Card o wszystkich możliwych kombinacjach pól, np. (A - Diamond, A - Clubs itd). Aby utworzyć taką kombinację, utwórz dwie niezależne 
listy - w pierwszej przechowuj możliwe figury, a w drugiej wartości. Następnie przechodząc pętlami, łącz je ze sobą i twórz obiekty.


"""


class Card:
    def __init__(self, color: str, value: str) -> None:
        self.color = color
        self.value = value
    
    def __repr__(self):
        return f"Card({self.color}, {self.value})"

    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.color == other.color and
                    self.value == other.value)


class Deck:
    values = [str(n) for n in range(2, 11)] + list('JQKA')
    colors = 'spades diamonds clubs hearts'.split()
    def __init__(self) -> None:
        self.cards = Deck.build()

    @staticmethod
    def build() -> list[Card]:
        cards = []
        for c in Deck.colors:
            for v in Deck.values:
                cards.append(Card(color=c, value=v))
        return cards
    
    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)

    def play_last(self):
        return self.cards.pop()
        # value = []
        # color = ["Hearts", "Clubs", "Diamonds" ,"Spades"]
        # for number in range(1, 14):
        #     value.append(number)
        # value[0] = "As"
        # value[10] = "J"
        # value[11] = "Q"
        # value[12] = "K"
        # for c in color:
        #     for v in value:
        #         self.cards.append(Card(c, v))
        # print(self.cards)
        # shuffle = random.shuffle(self.cards)
        # return(shuffle)
        
        
        
        
        
        
        
        
def main():
    french_deck = Deck()
    print(french_deck.cards)

    card_1 = Card('Clubs', 5)
    card_2 = Card('Clubs', 5)
    print(id(card_1))
    print(id(card_2))
    print(card_1 == card_2)

if __name__ == '__main__':
    main()

"""
# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
"""