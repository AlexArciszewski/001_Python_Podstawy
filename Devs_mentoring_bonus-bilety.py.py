"""
Napisz program w Pythonie, który będzie symulował system klasowy dla systemu transportu publicznego.
 Klasy będą reprezentować różne rodzaje biletów, takie jak bilety jednorazowe, bilety okresowe, bilety ulgowe itp.
Każda klasa będzie miała swoje własne atrybuty i metody, takie jak cena, czas ważności, możliwość zwrotu itp.
 Program powinien umożliwiać użytkownikowi wybór odpowiedniego biletu i wyświetlenie jego szczegółów.
"""
from datetime import datetime
from datetime import timedelta
class Ticket:
    def __init__(self, price: int) -> None:
        self.price = price
        self.refund = True


class PeriodTicket(Ticket):
    def __init__(self, price:int, period: datetime):
        super().__init__(price)
        self.period = period

class DiscountedTicket(Ticket):
    DISCOUNTS = {
        'teacher': 30,
        'uni_student': 51

    }
    def __init__(self, price:int, period: datetime, discount_type: str):
        super().__init__(price)
        self.discount_type = discount_type



def main():
    

    a = input("Choose the ticket")
    if a == "1":
        print("You chose a period ticket")
    elif a == "2":
        print("You chose a discount ticket")
        discount = input("Choose discount:")
        if discount in DiscountedTicket.DISCOUNTS:
            discount_type = discount
            ticket = DiscountedTicket(price=13, minutes=15 , discount_type=discount_type)
        else:
            print("Operation not allowed")      
    else:
        print("Operation not allowed")


    discount001 = DiscountedTicket(2, 1, "teacher")
    print(discount001)
if __name__ == "__main__":
    main()