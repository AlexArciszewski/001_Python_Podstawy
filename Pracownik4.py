"""
Zadanie 1:

Stwórz klasę Pracownik zawierającą następujące atrybuty:

imie (str) - imię pracownika
nazwisko (str) - nazwisko pracownika
stawka (float) - stawka godzinowa pracownika
Klasa powinna mieć również następujące metody:

pracuj() - wyświetl komunikat "Pracuję"
oblicz_wynagrodzenie(godziny: int) -> float - oblicz wynagrodzenie pracownika na podstawie podanych godzin i stawki godzinowej
Następnie stwórz klasę Programista dziedziczącą po klasie Pracownik. Klasa Programista powinna zawierać dodatkowy atrybut jezyki (list of str) - lista znanych przez programistę języków programowania.

Klasa Programista powinna również mieć następujące metody:

napisz_kod() - wyświetl komunikat "Piszę kod"
zwieksz_stawke(procent: float) - zwiększ stawkę godzinową programisty o podany procent
"""
#sfsfsff
class Employee:
    def __init__(self, name: str, last_name: str, wage: float) -> None:
        self.name = name
        self.last_name = last_name
        self.wage = wage
        
        
    def __repr__(self) -> str:
        return f"This is my current job I am {self.name} {self.last_name}"

    
    def __str__(self) -> str:
        return f"This is my current job I am {self.name} {self.last_name}"
        
        
    @staticmethod
    def work():
        print("Uaa I'm workin' on it Boss")
    
    @classmethod
    def create_new_guy(cls, name:str, last_name:str,monthly_wage:float):
        return cls(name, last_name, monthly_wage / 168)
        

    def chatter(self, working_hours:int) ->float:
        salary = self.wage * working_hours
        print(salary)
        return salary
        
class Developer(Employee):
    def __init__(self, name:str, last_name:str, str, wage: float, coding_language: list[str])->None:
        super().__init__(name, last_name, wage)
        self.coding_language = coding_language
    
    def write_code(self):
        print("I am coding boss")
    
    def increase_wage(self,percent:float):
        self.percent = percent
        self.wage = self.wage + (self.wage * percent/100)
         
        
        
def main():
    codemaster_001 = Employee(name ="John", last_name = "Woo",wage =200.10)
    codemaster_001.work()
    salary = codemaster_001.chatter(168)
    # option = "monthly"
    # if option =='monthly':
    #     player_001 = Employee.create_new_guy("Tom","Jerry", 4000)
    # elif option == "hourly":
    #     codemaster_001 = Employee(name ="John", last_name = "Woo",wage =200.10)
    # else:
    #     print("no data")
    
    
    

if __name__ == "__main__":
    main()
