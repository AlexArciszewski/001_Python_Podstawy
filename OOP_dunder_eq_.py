

class Person:

    def __init__(self, first_name: str, last_name: str,age:int) ->None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __eq__(self,other):
        return self.age == other.age



def main():
    
    John = Person('John', 'Doe', 25)
    Jane = Person('Jane', 'Doe', 25)
    print(John is Jane)         #false
    print(John == Jane)         #false 
    print(John == Jane)         #True bedzie po zastosowanie eq i powrownaiu wieku czyli
                                #    def __eq__(self,other):
                                #           return self.age == other.age
    
    
    
    
     
if __name__ == "__main__":
    main()





    
