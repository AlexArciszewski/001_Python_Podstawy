class Uzytkownik:
    def __init__(self, nazwa_, email_, haslo_):
        self.nazwa = nazwa_
        self.email = email_
        self.haslo = haslo_
        
    def __str__(self):
        return self.nazwa + " " + self.email + " " + self.haslo
    
    
class Program:
    def __init__(self):
        self.czy_uruchomiony = True
        self.uzytkownicy = []
    
        
    def dodaj_uzytkownika(self):
        nazwa = input("Podaj nazwe uzytkownika")
        email = input( "Podaj email uzytkownika")
        haslo = input("podaj haslo uzytkownika")
        
        nowy_uzytkownik = Uzytkownik(nazwa, email, haslo)
        self.uzytkownicy.append(nowy_uzytkownik)
        
        
    def zapisz(self):
        with open("uzytkownicy.txt","a") as plik:
            for uzytkownik in self.uzytkownicy:
                plik.writeln(str(uzytkownik))
             
                
    def wyswietl_menu(self):
        while(self.czy_uruchomiony):
            print("wybierz opcje: ")
            print("1 - Dodaj uzytkownika")
            print("2 - Zapisz do pliku")
            print("3 - Dodaj uzytkownika")
            
            wybor =input()
            self.wykonaj_z_menu(wybor)
    
    
    def wykonaj_z_menu(self, wybor):
        if wybor == "1":
            self.dodaj_uzytkownika()
        elif wybor == "2":
            self.zapisz()
        elif wybor == "3":
            self.czy_uruchomiony = False
        else:
            print("operacja zabroniona")
  
            
def main():
    menu = Program()
    
    menu.wyswietl_menu()

        
if __name__ == "__main__":
    main()      
                  
            




























