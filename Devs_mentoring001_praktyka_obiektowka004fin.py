""" 
Zad. 4(DevsMentoring)
Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak: numer_konta, nazwa właściciela konta, 
stan konta. 
1.	Stwórz konstruktor odpowiednio uzupełniający pola.
2.	Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto. 
    Dodaj założenie, że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł.
3.	Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta. 
    Program ma wyświetlać odpowiedni komunikat, gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy (przykładowo z powodu braku wystarczającej
    ilości środków na koncie).
4.	Napisz metodę change_ownership(), która przyjmować będzie imię nowego właściciela konta i będzie aplikowała tę zmianę w obiekcie klasy.
5.	Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie.

"""
class BankAccount:
    def __init__(self, account_number: int, owner_name: str,owner_surname: str, balance=0) -> None:
        self.account_number = account_number
        self.owner_name = owner_name
        self.owner_surname = owner_surname
        self.balance = balance
    
    
    def deposit(self, amount):
        if amount > 100: # -> 101
            amount -= 2  # -> 99
        self.balance += amount  # -> 1099

    def withdraw(self, amount: int) -> None:
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"Poprawnie wyplacono {amount}")
        else:
            print("Operation forbidden")
        
    def change_ownership(self, owner_name_new, owner_surname_new):
        self.owner_name = owner_name_new
        self.owner_surname = owner_surname_new
        
        # return self.name, self.surname  #czy to jest krotka?
    
    def display(self):
        return self.account_number, self.owner_name, self.owner_surname, self.balance,
    
    
    # nie wiem wiek, którego usera ma wyswietlać funkcha display. Teraz wyświetla starego. Z nowym jest problem.
        
        
def main():
    account1 = BankAccount(406945456, "Jan", "Nowak", 43_500)
    print(account1)
    print(account1.deposit(101))
    print(account1.withdraw(50))
    print(account1.change_ownership("John", "Doe"))
    print(account1.display())
    
    
    
if __name__ == '__main__':
    main()
    