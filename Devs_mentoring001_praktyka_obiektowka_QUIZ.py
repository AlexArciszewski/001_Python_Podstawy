from datetime import date
#from dateutil import parser
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
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
#print(first_case["end_task"], second_case["end_task"])   
t_one = first_case["created_task"]
t_one2 = first_case["end_task"]
t_two2 = second_case["created_task"]
t_two2 = second_case["end_task"]
print(first_case["created_task"])
s = ('2021-10-26T19:48:12+00:00')
datetime.fromisoformat(s.replace('Z', '+00:00'))
print(s)
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
datetime_1 = parse('2021-09-26T19:48:12+00:00')
datetime_2 = parse('2021-10-26T19:48:12+00:00')
delta = relativedelta(datetime_2, datetime_1)
print(f"{delta.years} year {delta.months} months {delta.days} days {delta.hours} hours {delta.hours} minutes ago")
print(datetime.fromisoformat('2021-10-26T19:48:12+00:00'))


print("date")
print(first_case["created_task"])
print(first_case["end_task"])
print(second_case["created_task"])
print(second_case["end_task"])

print("date")
print(datetime.strptime(first_case["created_task"], '%Y-%m-%dT%H:%M:%S%z'))

"""
url -> https://opentdb.com/
url_to_api = https://opentdb.com/api.php?amount=10&category=18&difficulty=easy


10 pytań, użytkownik odpowiada 1-4, zliczanie niepoprawnych i pooprawnych odpowiedzi,
 *zliczanie czasu srednio na odpowiedź.
Question, Quiz

user dostaje pytanie -> odpowiedz -> pytanie -> odpowiedz -> na koncu jest mu wyswietlane podsumowanie po 10 pytaniach.
"""

import requests

# class Quiz:
#     def __init(self) -> None:
#         self


class Questions:
    def __init__(self, url: str):
        self.url = url

    def _get_raw_data(self) -> list[dict[str, str | list]]:
        raw_data = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy').json()['results']
        return raw_data

    def create_questions(self) -> list[dict[str, str | list]]:
        """
            return list without unused data from _raw_data,
            - question
            - correct_answer
            - answers

        """
        question_set = []
        for question in self._get_raw_data():
            print(question['question'])
            print(question['correct_answer'])
            print(question['incorrect_answers'])
            question_set.append({'question': question['question'], 'correct_answer': question['correct_answer'], 'answers': [question['correct_answer'], *question['incorrect_answers']]})
        return question_set


def main():
    questions = Questions('')
    questions.create_questions()
if __name__ == '__main__':
    main()

