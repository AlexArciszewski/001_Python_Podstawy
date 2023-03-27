""" 
Zad. 3(DevsMentoring)
Stwórz klasę reprezentującą Prostokąt. Dodaj do niej metody obliczające pole i obwód z 
przechowywanych pól - szerokościi długości. 


"""
class Rectangle:
    
    def __init__(self, width: float, length: float) -> None:
        self.width = width
        self.length = length
        
    def rec_circumference(self) -> float:
        return 2 * (self.width + self.length)
    
    def rec_area(self) -> float:
        return self.width * self.length
    
def main():
    rect = Rectangle(10,20)
    print(rect.rec_circumference())
    print(rect.rec_area())
    
if __name__ == "__main__":
    main()
    