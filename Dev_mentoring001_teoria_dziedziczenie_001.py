class Wielokat:
    
    def __init__(self, boki_, suma_katow_):
        self.boki = boki_
        self.suma_katow = suma_katow_

    def oblicz_obwod(self):
        return sum(self.boki)
    
    def wyswietl_sume_katow(self):
        print(self.suma_katow)
        
class Trojkat(Wielokat):
    
    def __init__(self, a, b, c):
        super().__init__([a, b, c ], 180)
        
    def oblicz_pole(self):
        a, b, c = self.boki[0], self.boki[1], self.boki[2]
        p = (self.boki[0] + self.boki[1] + self.boki[2]) / 2
        return (p*(p - a)*(p -b)*(p-c)) ** 0.5 
    
    
def main():
    trojkat_rownoramienny =Trojkat(5, 5, 5)
    print(trojkat_rownoramienny.oblicz_obwod())
    trojkat_rownoramienny.wyswietl_sume_katow()
    print("{:.4f}".format(trojkat_rownoramienny.oblicz_pole()))
    
if __name__ == "__main__":
    main()
    


































