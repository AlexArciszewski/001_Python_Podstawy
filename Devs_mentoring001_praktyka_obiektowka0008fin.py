"""
Zad. 8
Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:

first_case = {
    ‘name’: ‘first_case’,
    ‘created_task’: ‘2021-10-26T19:48:12+00:00’,
    ‘end_task’: None
}

second_case = {
    ‘name’: ‘second_case’,
    ‘created_task’: ‘2021-09-26T19:48:12+00:00’,
    ‘end_task’: ‘2021-10-26T19:48:12+00:00’
}

Klasa Case ma zawierać metodę retrieve_seconds, która zwracać będzie różnicę czasową między end_task a created_task podaną w sekundach.

UWAGA
1. Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa. 
2. Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie 
"""

first_case = {
                "name": "first_case",
                "created_task": "2021-10-26T19:48:12+00:00",
                "end_task": None
                }
        
second_case = {
                "name": "second_case",
                "created_task": "2021-09-26T19:48:12+00:00",
                "end_task": "2021-10-26T19:48:12+00:00"
                }



from datetime import date
from datetime import datetime
class Case:
      
    def __init__(self, name:str, created_task:date, end_task:date) -> None:
        self.name = name
        self.created_task = created_task 
        self.end_task = end_task
        
        
        
    
                  
        
    def retrieve_seconds(self) -> None:
        d1 = (datetime.strptime(self.created_task, '%Y-%m-%dT%H:%M:%S%z'))
        d2 = (datetime.strptime(self.end_task, '%Y-%m-%dT%H:%M:%S%z'))
        delta = d2 - d1
        return print(f'Difference is {delta.days} days')


    
    
    
    


def main():
    case_001 =Case("second_case", "2021-09-26T19:48:12+00:00","2021-10-26T19:48:12+00:00" )
    case_001.retrieve_seconds()


if __name__ == "__main__":
    main()

