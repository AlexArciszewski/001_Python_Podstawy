"""
Utworzyć klasy Notatka (Note) i Notatnik (Notebook). Klas notatki przechowuje autora, treść i czas utworzenia (autor i treść są podawane jako argumenty konstruktora, a czas
jest pobierany i zapisywany przy tworzeniu obiektu).

Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów, lecz tworzy pustą listę do której będą dodawane obiekty klasy Notatka. Klasa Notatnika musi posiadać 
implementacje metod, pozwalających: dodać nową notatkę, dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki. Dodatkowo musi 
być obsłużona sytuacja kiedy notatnik jest pusty.

"""
"""
Przykład:
>>> nb = Notebook()
>>> nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
>>> nb.wyswietl_wszystko()
Masz takie notatki:
1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
>>> n1 = Note("Andrii", "Sprawdzic instrukcje ")
>>> nb.dodaj(n1)
>>> nb.wyswietl_wszystko()
Masz takie notatki:
1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
2. Andrii: "Sprawdzic instrukcje" o godzinie 22:20


Podpowiedź:
do reprezentacji czasu można użyć modułu
datetime
Dokumentacja modułu
datetime
https://docs.python.org/3/library/datetime.html

Przykład:
>>> import datetime
>>> t = datetime.datetime.now()
>>> t
datetime.datetime(2021, 4, 8, 22, 39, 46, 274407)
>>> t.hour
22
>>> t.minute
27
"""
from datetime import date
class Note:
    def __init__(self, author:str, memo_content: str) -> None:
        self.author = author
        self.memo_content = memo_content
        self.message_date = ''

        
    # def create_note(self):
    #     self.note =[]
    #     user_name =str(input("Pls give me your name: "))
    #     for _ in range(0,1):
    #         self.note.append(user_name)
    #     text = str(input("Add text of  your note: "))
    #     for _ in range(0,1):
    #         self.note.append(text)
    #     today = date.today()
    #     for _ in range(0,1):
    #         self.note.append(today)
    #     self.note =[user_name, text, today]
    #     return self.note


class Notebook:
    def __init__(self) -> None:
        self.notebook = []

    def add_existing_note(self, note: 'Note'):
        self.notebook.append(note)
        print("Pomyslnie dodano notatke.")
    
    def add_new_note(self, text: str, content: str):
        self.notebook.append(Note(text, content))

    def create_new_note(self):
        text = input("Podaj text")
        content = input("podaj content notatki")
        self.notebook.append(Note(text, content))



    #     else:
    #         print(f"there is no note number{n} in your notebook")
    # def add_existing_note(self, note: 'Note', text: 'Note'):
    #     n = int(input(print("Pls choose the note you wannna change")))
    #     print(f"you chose note number {n}")
    #     if n < len(self.notebook):
    #         print(self.notebook[n])
    #         self.notebook[n] = note
    #         change_text = str(input(print("Pls choose the text you wannna change")))
    #         # note.text = change_text
    #         self.notebook[n].text = change_text
    #         print("operation succesful")
    #     else:
    #         print(f"there is no note number{n} in your notebook")
        pass #co to znaczy dodać istniejącą notatkę? czym to się różni od dodania nowej notatki?
    
    def count_notes(self, note:'Note'):  
        if note in self.notebook:
            return print(f"You have {len(self.notebook)} notes in your notebook")
        else:
            return print("your notebook is empty")  #czy to wystarczy do sprawdzania czy sa notatki w notatniku czy lepiej gdzies dać try i except?
         
    
    def print_all_notes(self, note:'Note'):
        for note in self.notebook:
            print(note)
            return print(note)


def main():
    note__001 = Note("jan Kowalski", "Czesc", 12012023)


if __name__ == "__main__":
    main()

# Pytania
# 1. Jak wykorzystać obiekt z jednej klasy w drugiej? Starałem się zrobić coś jak w zadaniu nr6 ze słownikami.
#   To jest chyba mój główny problem w zadaniach czyli musze w drugiej klasie wykorzystac coś z pierwszej bez dziedziczenia

# 2. Czy lepsza jest obłsuga zeranotatek w notatni z wykrozystaniem try i except czy if?

# 3.Jak sprawdzić czy takie zadanie na obiektach działa? powinienem stworzyć jakąs notatkę i sprawdzić czy się zapisuje?

# 4 Co to znaczy dodać istniejącą notatkę? czym to się różni od dodania nowej notatki?

""" 
# Import date class from datetime module
from datetime import date
 
# Returns the current local date
today = date.today()
print("Today date is: ", today)


"""




