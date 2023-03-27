
class Parent1:
    def __init__(self):
        super().__init__()
        print("in Parent1 class...")
     
class Parent2:
    def __init__(self):
        print("in Parent2 class...")
        

class Derived(Parent1, Parent2): #kolejnosc wywołania initów zależy od kolejnosci po czym dziedziczy czyli wywolany zostanie najpierw ini klasy bazowej parent 1
    def __init__(self):
        super().__init__()
        print("In Derived class...")
        

def main():
    d = Derived()
print(Derived.mro())   #W jakiej kolejności zostaną wywołane konstruktory :)

if __name__ == "__main__":
    main()
        

class Obszar:
    def __init__(self, pole_):
        self.pole = pole_
    
    def main():
        obszar1 = Obszar(100)
        obszar2 = Obszar(200)
        
        print(obszar1 + obszar2)
        
if __name__ == "_main__":
    main()
        






























