"""
Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy: Manager oraz Order.
W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia, a wartością jego ilość na
stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.

Funkcjonalność programu to:
- dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt, którego id znajduje się już w słowniku, to
nie będziemy dodawali nowej pary do dicta, ale zwiększali ilość danego obiektu w słowniku (zwiększali odpowiednią
wartość w słowniku)).
- usuwanie o 1 zamówienia ze słownika o określonym id

Podpowiedź:
Pseudokod slownika:
self.orders = {obiekt1 : jego_ilosc}

Sprzedawanie produktu:

def sell(self, id_to_sell):
    for order in self.orders:
        if order.id == id_to_sell:
           self.orders[order] -= 1

"""


# TODO

class Manager:
    def __init__(self) -> None:
        self.orders = {}

    def add_order(self, new_order: 'Order'):
        if not self.orders:
            self.orders[new_order] = 1
            return
        for order in list(self.orders): # ->
            if order.idx == new_order.idx:
                self.orders[order] += 1
            else:
                self.orders[new_order] = 1
        # if order in self.orders:
        #     self.orders[order] += 1
        # else:
        #     self.orders[order] = 1

    def sell_order(self, order: 'Order'):
        if order in self.orders:
            self.orders[order] -= 1
            if self.orders[order] == 0:
                del self.orders[order]



class Order:
    def __init__(self, idx: int, name: str, price: int) -> None:
        self.idx = idx
        self.name = name
        self.price = price
    #
    # def __eq__(self, other: 'Order'):
    #     if isinstance(self, other):
    #         return self.idx == other.idx
    #
    # def __hash__(self):
    #     return hash(self.idx)

    def __repr__(self) -> str:
        return f" < {self.name} {self.price}>"


def main():
    manager = Manager()
    order = Order(1, 'rower', 999)
    order_1 = Order(1, 'rower', 999)
    order_2 = Order(2, 'laptop', 9999)

    manager.add_order(order)
    manager.add_order(order_1)
    manager.add_order(order_2)

    print(manager.orders)
if __name__ == "__main__":
    main() 
