
# """
# 1) Stwórz klasę Tank (zbiornik).
# Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
# Należy stworzyć następujące operacje:
# pour_water(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
# pour_out_water(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
# transfer_water(from, volume) - przelewa wodę ze zbiornika “from” do naszego (pod warunkiem, że przelewanie jest możliwe)
# Dodatkowo stworzyć metody, które pozwalają:
# Znaleźć zbiornik, w którym jest najwięcej wody
# Znaleźć zbiornik, który jest najbardziej zapełniony
# Znaleźć wszystkie puste zbiorniki
# 2) Każda operacja na zbiorniku jest rejestrowana.
# Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.
#
# Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
# Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
# Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)
#
# 3) To co zaimplementowaliśmy powyżej to demo “Event Sourcingu” - na czym ono polega?
# Zaimplementuj metodę check_state(volumeName), która pozwoli określić, czy stan wody jest spójny z tym, co mamy na liście historii operacja dla danego zbiornika.
#
# """
from __future__ import annotations
#
# class TankManager:
#     tanks = []

# class LogManager:
#     logs = []


class Tank:
    logs = []
    def __init__(self, name: str, total_capacity: int, volume:int) -> None:
        self.name = name
        self.total_capacity = total_capacity
        self.volume = volume
        #TankManager.tanks.append(self)

    def __str__(self) -> str:
        return f" {self.name} capacity:{self.total_capacity} liters"

    def pour_water(self, amount: int):
        if self.total_capacity - self.volume > amount:
            self.volume += amount  # self.volume = self.volume + ammount
            print(f"you just added {amount}")
            Tank.logs.append({'name': self.name, 'status': True})
            # -> True
        else:
            print(f"It is too much water for that tank dummy")
            Tank.logs.append({'name': self.name, 'status': False})
            # -> False

    def pour_out_water(self, amount_lost: int):
        if amount_lost < self.total_capacity: #dodałem załzenie ze mozna dolac nie wiecej niż zbiornik
            if self.volume > amount_lost:  # jesli obj wody w zbiorniku jest >od tego co chcemy wylac
                self.volume -= amount_lost  # obj wody w zbiorniku =obj wody w zbiorniku - to co chcemy wylac i to nie działa:D
                print(f"you just poured {amount_lost} of water. There is {self.volume} liters of water in the tank ")
            else:
                print(f"You can't do that")

    def __lt__(self, other):
        return self.volume < other.volume


#transfer_water(from, volume) - przelewa wodę ze zbiornika “from” do naszego (pod warunkiem, że przelewanie jest możliwe)

    def transfer_water(self, from_obj: Tank, volume_tanker2: int):
        amount_tank1 = self.total_capacity - self.volume
        if self.total_capacity and amount_tank1 > volume_tanker2: #jeśli to co chcemy przelać ze zbiornika 2 jest mniejsze od pojemnosci zbiornika 1 i od amount czyli tego co zostało w zbiorniku to można przelać
            amount_tank1 -= volume_tanker2
            print(f"you moved the {volume_tanker2} liters from tank named: {from_obj} to the {self.name} ")

    @staticmethod
    def max_water_level(list_of_tanks: list[Tank]):
        max_volume = 0
        tank_name = None
        for tank in list_of_tanks:
            if tank.volume > max_volume:
                max_volume = tank.volume
                tank_name = tank.name
        print(tank_name, max_volume)


#Znaleźć zbiornik, w którym jest najwięcej wody

# def max_water_level(self, tank:'Tank', water_level:int):
#     water_tanks = [{tank : water_level}, {tank: water_level}]
#
#     for tank, water_level in water_tanks.items():

        """
def max_water_level(self, total_capacity:int, volume:int):   
    water_tanks = {}
    tanks_list = list(water_tanks)
    tanks_list.sort()
    print(tanks_list[-1])
    print(f'Tank with the highest water level is {tanks_list[-1]} ')    
"""
def max_water_level_tank(self,tank_name:str,total_capacity:int,volume:int ):
    water_tanks = {}
    ' SELECT * from users'  # -> ORM

def tank_fill_test(tank_name: str, capacity: int, water_level: int, tanks_list=None):
    if not tanks_list:
        tanks_list = []
    tanks_dict = {}

    values = capacity - water_level
    tanks_dict = {tank_name: values}

    tanks_list.append(tanks_dict)
    # stworzyłem słowniki z wartości key:value
    print(tanks_list)

    # tanks_list.append(dict(zip(keys,values)))
    # print(tanks_list)

    # print(tanks_list)
    return tanks_list

# tank_fill_test()

tanks_list = []

tanks_list = tank_fill_test("Tank_number_one", 1000, 800, tanks_list)
tanks_list = tank_fill_test("Tank_number_two", 1000, 700, tanks_list)
tanks_list = tank_fill_test("Tank_number_three", 1000, 900, tanks_list)
tanks_list = tank_fill_test("Tank_number_four", 1000, 200, tanks_list)

print(tanks_list)


def main():
    tanks = []
    tanker_001 = Tank("Water_tanker_001", 10000, 500)
    tanker_002 = Tank("Water_tanker_002", 1000, 30)
    tanker_003 = Tank("Water_tanker_003", 10000, 7321)
    tanks.append(tanker_001)
    tanks.append(tanker_002)
    tanks.append(tanker_003)
    print(tanks)
    tanks.sort()
    print(tanks)
    print(tanks[0].volume)
    # Tank.max_water_level(tanks)
    # print(tanker_001)

    #
    # tanker_001.pour_water(11000)
    # tanker_001.pour_out_water(400)
    #
    # tanker_001.transfer_water(tanker_002, 100)
    #
    # """
    # tanker_001.max_water_level(5000,100)
    # tanker_002.max_water_level(6000,100)
    # """

    # list_of_tanks = [{"name": "Tank_number_one", "capacity": 1000, "volume": 800},
    #               {"name": "Tank_number_two", "capacity": 1000, "volume": 700},
    #               {"name": "Tank_number_three", "capacity": 1000, "volume": 900},
    #               {"name": "Tank_number_four", "capacity": 1000, "volume": 200},
    #                  {"name": "Tank_number_five", "capacity": 1000, "volume": 98}]
    # max_volume = 0
    # tank_name = None
    # for tank in list_of_tanks:
    #     if tank['volume'] > max_volume:
    #         max_volume = tank['volume']
    #         tank_name = tank['name']
    #
    #
    # list_of_tanks.sort(key= lambda obj: obj['volume'])
    # print(list_of_tanks)



if __name__ == "__main__":
    main()
""" 
{'Tank_number_one': 200}
{'Tank_number_two': 300}
{'Tank_number_three': 100}
{'Tank_number_four': 800}


"""