# import random
#
# cards = []
# value = []
# color = ["Hearts", "Clubs", "Diamonds" ,"Spades"]
# for number in range(1, 14):
#     value.append(number)
# value[0] = "As"
# value[10] = "J"
# value[11] = "Q"
# value[12] = "K"
# for c in color:
#     for v in value:
#         cards.append((v,"of",c))
# print(cards)
# random.shuffle(cards)
# print("shuffled: ")
# print(cards)


class Doctor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday_party(self, date="NaN"):
        print(f"Gratulacje {self.name} skonczyles wlasnie {self.age + 1}, dzisiejszego dnia {date}")

    @staticmethod
    def info():
        print("To jest klasa doktor")

    @staticmethod
    def today_date():
        from datetime import datetime
        print(datetime.now())


    def mixed_party(self, party_name: str) -> None:
        Doctor.today_date()
        print(f"Dzisiejszy impreza z powodu {party_name}")
        print("I jeszcze z powodu urodzin: ")
        self.birthday_party()



doctor = Doctor("Jan", 33)
doctor_1 = Doctor("Robert", 51)
doctor_2 = Doctor("Witold", 28)
doctor_3 = Doctor("Zbigniew", 41)

doctor.birthday_party()
doctor_1.birthday_party()
doctor_2.birthday_party()
doctor_3.birthday_party()

doctor.info()

Doctor.info()

doctor.mixed_party('narodziny dziecka')
