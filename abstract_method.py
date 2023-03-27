#Klasa abstrakcyjna to taka klasa której instancji nie możemy stworzyć. Służy ona do tego by z 
# niej dziedziczyć i implementować te metody które oznaczone zostały jako abstrakcyjne. Przykład takiej klasy:
#

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass
   
    def method2(self):
        return "Helo!"

    def __str__(self):
        return f'Jestem {self.__class__.__name__}'


class ConcreteClass(AbstractClass):
    def method1(self):
        print("Heeelo!")


print(ConcreteClass())



#Jestem ConcreteClass


from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        return "Helo!"


#print(AbstractClass())
#TypeError: Can't instantiate abstract class AbstractClass with abstract method method1




