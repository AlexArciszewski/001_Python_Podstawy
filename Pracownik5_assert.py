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

class Pracownik:
    def __init__(self, imie: str, nazwisko: str, stawka: float) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def __repr__(self) -> str:
        return f"This is my job. I am {self.imie} {self.nazwisko}"

    def __str__(self) -> str:
        return f"This is my job. I am {self.imie} {self.nazwisko}"

    @staticmethod
    def pracuj():
        print("pracuje")

    def oblicz_wynagrodzenie(self, godziny: int) -> float:
        return self.stawka * godziny

    @classmethod
    def create_employee(cls, name: str, surname: str, salary_per_month: float):
        return cls(name, surname, salary_per_month / 168)

    @classmethod
    def create_employee_from_yearly(cls, name: str, surname: str, salary_per_year: float):
        return cls(name, surname, salary_per_year / 2080)


class Programista(Pracownik):
    def __init__(self, imie: str, nazwisko: str, stawka: float, jezyki: list[str]) -> None:
        super().__init__(imie, nazwisko, stawka)
        self.jezyki = jezyki

    def napisz_kod(self):
        print("piszę kod")

    def zwieksz_stawke(self, procent: float):
        self.stawka = self.stawka + self.stawka * (procent / 100)
        self.stawka += self.stawka * (procent / 100)


def main():
    player_001 = Pracownik(imie="Jan", nazwisko="Nowak", stawka=50)
    print("TEST CASES")
    print(player_001.imie)
    print("=" * 79)
    assert player_001.imie == 'Jan'
    assert player_001.nazwisko == 'Nowak'
    assert player_001.stawka == 50
    assert player_001.oblicz_wynagrodzenie(10) == 500
    player_001.stawka = 60
    assert player_001.oblicz_wynagrodzenie(10) == 600

    # option = 'monthly'
    # if option == 'monthly':
    #     player_001 = Pracownik.create_employee('Jan', 'Nowak', 10_000)
    # elif option == 'hourly':
    #     player_001 = Pracownik('Jan', 'Nowak', 55)
    # elif option == 'yearly':
    #     player_001 = Pracownik.create_employee_from_yearly('Jan', 'Nowka', 120_000)
    #

if __name__ == "__main__":
    main()