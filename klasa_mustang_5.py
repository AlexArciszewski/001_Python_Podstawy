from __future__ import annotations

class MyGarage:
    def __init__(self, place, cost):
        self.place = place
        self.cost = cost
        self.cars = []

    def add_new_car(self):
        pass

class Transsmisions:
    def __init__(self, type3: str, gears: int, producer: str) -> None:                                                                                   #19
        self.type3 = type3                                                                                                                       #20
        self.gears = gears                                                                                                                       #21
        self.producer = producer                                                                                                                 #22

class MyCars:                                                                                                                                     #1
    """
    docstring test.
    """
    #init inicjalizacja startowych wartości dla atrybutów/konstruktor obiektow wywołuje się podczas konstrukcji obiektów. Odbiera wartości początkowe z car_001 = My_cars(tu te wartosci) z linii 26
    def __init__(self, production_year: int, engine: Engine, make: str, model: str, transmission: Transsmisions, mileage: int, drivetrain: str) -> None:          #2
        self.production_year = production_year                                                                                                    #3
        self.engine = engine                                                                                                                      #4
        self.make = make                                                                                                                          #5
        self.model = model                                                                                                                        #6
        self.transmission = transmission                                                                                                          #7
        self.mileage = mileage                                                                                                                    #8
        self.drivetrain = drivetrain                                                                                                              #9
        self.crashes: list[str] = []


    def __len__(self):
        return len(self.crashes)
        
    # def __repr__(self) -> str:
    #     return f"MyCars(make: {self.make}, model: {self.model})"

    def __str__(self) -> str:
        return f"STR: Samochó∂ o nazwie: {self.make}"
    #
    def __eq__(self, other):
        if isinstance(other, MyCars):
            return other.production_year == self.production_year



class Engine:  # 13
    """
    engine in my car docstring test.
    """

    def __init__(self, type1: str, type2: str, displacement: int, fuel: str, horsepower: int):  # 14
        self.type1 = type1  # 15
        self.type2 = type2  # 15.5
        self.displacement = displacement  # 16
        self.fuel = fuel  # 17
        self.horsepower = horsepower  # 18

    """def __len__(self):
        return len(self.ENGINE)
    """
        
        
        
def main():                                                                                                                                       #10
    v8_302HO_tuned = Engine("combustion","NA", 5000,"gasoline", 265)                                                                              #24
    t5 = Transsmisions("manual", 5, "Borg Warner")                                                                                                  #25
      
    #car_001 = My_cars(production_year = 1994, make = "Ford", model = "Mustang GT", mileage =500000 drivetrain = "RWD" )                          #23
    car_001 = MyCars(production_year=1994, engine=v8_302HO_tuned,  make="Ford", model="Mustang GT", transmission=t5, mileage=50000, drivetrain="RWD")   #26                                         #26
    car_002 = MyCars(production_year=1994, engine=v8_302HO_tuned,  make="Ford", model="Mustang GT", transmission=t5, mileage=50000, drivetrain="RWD")
    #print(len(car_001.crashes))
    print(len(car_001))
    car_001.crashes.append('1998 road coutnry')
    print(len(car_001))

    #26                                         #26
    print(car_001==car_002)

    print(car_001)  # <class '__main__.MyCars'>
    xyz = str(car_001)
    print(xyz)
    print(repr(car_001))  # <class '__main__.MyCars'>
    # print(len(car_001))


        
if __name__ == "__main__":                                                                                                                        #11
    main()                                                                                                                                        #12


#print(car_001) #tego nie mogę wywołać indent?




"""
1. Jak wywołać car_001?
2. jak zrobić dziedziczenie?
3. Jak po co zrobiłem main?         czy hcodzi o zebranie obiektów ?
4. po co jest 
    if __name__ == "__main__":                                                                                                                        
        main()  
5. gdzie umieścić:
    def __str__(self):
        return "class training" 
        aby zamiast  <class '__main__.MyCars'> mieć "class training" chce wykorzystać obiekt jako string....
6. jak można zrobic __len__(self): ?





"""