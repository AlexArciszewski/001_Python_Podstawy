""" 
Stwórz klasę Shape i jej podklasę Square. Square ma posiadać konstruktor, który przyjmie length jako argument. 
Obie klasy mają posiadać metodę obliczającą pole figury. Domyślnie Shape ma zwracać wartość 0.


"""

class Shape:
    def __init__(self, first_side_length:int, height_lenght_second_side:int) -> None:
        self.first_side_length = first_side_length
        self.height_lenght_second_side = height_lenght_second_side
        area = self.first_side_length * height_lenght_second_side
        #return area
    
    def shape_area(self):    
        area = self.first_side_length * self.height_lenght_second_side
        return area
    
class Square(Shape):
    def __init__(self,first_side_length:int,height_lenght_second_side:int) -> None:
        super().__init__(self,first_side_length, height_lenght_second_side)
        
    def square_area(self):    
        square_area = self.first_side_length * self.height_lenght_second_side
        return square_area





def main():
    figure001 = Shape(first_side_length = 5, height_lenght_second_side = 6)
    figure001.shape_area()


if __name__ == "__main__":
    main()
    
    
    
         
 