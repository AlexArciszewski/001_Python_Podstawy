
class Obszar:
    def __init__(self, pole_):
        self.pole = pole_
    
    def __add__(self, obj):
        return self.pole + obj.pole
    
    
def main():
    obszar1 = Obszar(100)
    obszar2 = Obszar(200)
        
    print(obszar1 + obszar2)
        
if __name__ == "_main__":
    main()
        
#Przeładowanie dodawania nie działa!





























