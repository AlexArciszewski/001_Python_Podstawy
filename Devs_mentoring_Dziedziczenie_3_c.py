#Devs mentoring Zadanie 3 Dziedziczenie

""" 

Part I: Members, Students and Instructors

You're starting your own web development school called Codebar! Everybody at Codebar - whether they are attending workshops or teaching them - is a Member:

    Each member has a full_name.
    Each member should be able to introduce themselves (e.g., "Hi, my name is Kevin!").

Each Member is also either a Student or an Instructor:

    Each Student has a reason for attending Codebar (e.g., "I've always wanted to make websites!").
    Each Instructor a bio (e.g., "I've been coding in Python for 5 years and want to share the love!").
    Each Instructor also has a set of skills (e.g., ["Python", "Javascript", "C++"]).
    An Instructor can gain a new skill using add_skill.

Part II: Workshops

Codebar also has Workshops. Each Workshop has:

    A date.
    A subject.
    A group of instructors.
    A roster of students.
    An add_participant method that accepts a member as an argument. If the Member is an Instructor, add them to the instructors list. If a Member is a Student, add them to the students list.

Create another method print_details that outputs the details of the workshop.





"""



from datetime import datetime
from datetime import timedelta



class Member:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
    
    def __repr__(self) -> str:
        return f"Hi, my name is {self.name} {self.surname}" # z str nie dawało rady ciekawe
        
        
class Student(Member):
    def __init__(self, name: str, surname: str, why_coding: str) -> None:
        super().__init__(name, surname)
        self.why_coding = why_coding
        
    def reason(self) -> str:     #zwraca stringa
        return self.why_coding
        


class Instructor(Member):
    def __init__(self, name: str, surname: str, bio: str, skill_set:list) -> None:
        super().__init__(name, surname)
        self.bio = bio
        self.skill_set = skill_set
        
    def your_bio(self)-> str:               #dlaczego tutaj nie mam jak dla studenta
        return self.bio
    
    def skills(self):
        return self.skill_set
    def add_skill(self):
        
        list = []
        """
        for skill in self.skill_set:
            list.append(self.skill_set) #tak będzie dwa bo dla dwoch powstanie to wywalamy
        """
        list = self.skill_set
       
        a = input("Please add new skill in coding: ")
        print("Your new skill is: ",a )
        
        self.skill_set.append(a)
        print(f"Your new set of skills is: {list}")
        
class Workshops:
    def __init__(self, date: datetime, subject: str, instructors_group: dict, students_rosters: dict) -> None:
        self.date = date
        self.subject = subject
        self.instructors_group = instructors_group
        self.students_rosters = students_rosters
        
    def add_participant(self):
           
        instructors_group = {}
        student_rosters = {}
        
        b = input("Greetings! Choose your status. Press 1 for student and 2 for the instructor ")
        if b == "1":
            print("You are a student.Please add your name to a list")
            name = input("Please give me the your name: ")
            surname = input("Please give me the your surname: ")
            student_rosters['name'] = name
            student_rosters['surname'] = surname
            print(student_rosters) 
        elif b == "2":
            print("You are the instructor .Please add your name to a list")
            name = input("Please give me the your name: ")
            surname = input("Please give me the your surname: ")
            instructors_group['name'] = name
            instructors_group['surname'] = surname
            print(instructors_group)
            
        else:
            print("Operation not allowed")   
            
    def __repr__(self) -> str:
        return f" The {self.subject}course starts: {self.date} Instructors: {self.instructors_group} and students:{self.students_rosters}"  
              
            
              
    @classmethod
    def show_details(cls,date: datetime, subject: str, instructors_group: dict, students_rosters: dict):
        return cls(date,subject,instructors_group, students_rosters)
    """
    def add_more_participants(self,name, surname, reason):
        self.name = name
        self.surname = surname
        self.reason = reason
        students = []
        instructors = []
        
        
        
        
        c = input("Greetings! Choose your status. Press 1 for student and 2 for the instructor ")
        if c == "1":
            print("You are a student.Please add your name to a list")
            self.name = input("Please give me the your name: ")
            self.surname = input("Please give me the your surname: ")
            
            students.append(Student(self.name, self.surname))
            print(students)
        
        elif c == "2":
            print("You are the instructor .Please add your name to a list")
            self.name = input("Please give me the your name: ")
            self.surname = input("Please give me the your surname: ")
            self.reason = input("Reason")
            instructors.append(Instructor("name","surname","reason"))
            print(instructors)
            
            
        else:
            print("Operation not allowed")   
    """    
    def add_more_participants(self,name, surname, status):
        self.name = name
        self.surname = surname
        self.status = status
        students = []
        instructors = []
        self.status = input("pls write your status:instructror or student" )
        if self.status == "instructor":
            instructors.append(self.name + self.surname + self.status)
            print(instructors)
        elif self.status == "student":
            students.append(self.name + self.surname)
            print(students)
        else:
            print("operation forbidden")
            
        
        
            
        
        
        
        
        
        

#Create another method print_details that outputs the details of the workshop.    
        
        



def main():
    member001 = Member("John", "Doe")
    print(member001)
    
    student001 = Student("Jackie", "Chan", "I want to create kick-ass games")
    print(student001)
    print(student001.why_coding)
    
    
    instructor001 = Instructor("John", "Woo", "I've been coding in Python for 5 years and want to share the love!",["C","Python"])
    print(instructor001)
    
    print(instructor001.bio)
    print(instructor001.your_bio)  #dlaczego wyświetla bound method
    print(instructor001.skill_set) 
    
    instructor001.add_skill()
    
    workshop_001 =Workshops(2022,"Python",{'name':"Michal",'surname':"Nowak",'status': "i"}, {'name':"Jan",'surname':"Kowalski",'status': "s"} )

    workshop_001.add_participant()
    print(workshop_001)
    workshop_002 =Workshops.show_details(2023,"Java",{'name':"Bolek",'surname':"Lolek",'status': "i"}, {'name':"Clint",'surname':"Eastwood",'status': "s"} )
    print(workshop_002)
    workshop_001.add_more_participants("john", "doe","instructor")
    
if __name__ == "__main__":
    main()
    



""" 
Requirements
Part I: Members, Students and Instructors

You're starting your own web development school called Codebar! Everybody at Codebar - whether they are attending workshops or teaching them - is a Member:

    Each member has a full_name.
    Each member should be able to introduce themselves (e.g., "Hi, my name is Kevin!").

Each Member is also either a Student or an Instructor:

    Each Student has a reason for attending Codebar (e.g., "I've always wanted to make websites!").
    Each Instructor a bio (e.g., "I've been coding in Python for 5 years and want to share the love!").
    Each Instructor also has a set of skills (e.g., ["Python", "Javascript", "C++"]).
    An Instructor can gain a new skill using add_skill.

Part II: Workshops

Codebar also has Workshops. Each Workshop has:

    A date.
    A subject.
    A group of instructors.
    A roster of students.
    An add_participant method that accepts a member as an argument. If the Member is an Instructor, add them to the instructors list. If a Member is a Student, add them to the students list.

Create another method print_details that outputs the details of the workshop.
Test Your Code

Make your code work for the following calls and print out the response you can see in the comments below:

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details
# =>
# Workshop - 12/03/2014 - Shutl
#
# Students
# 1. Jane Doe - I am trying to learn programming and need some help
# 2. Lena Smith - I am really excited about learning to program!
#
# Instructors
# 1. Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.
# 2. Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love
#

Bonus

The print_details method currently does a number of different things, like printing out workshop details, the list of Students and the list of Coaches.

Create separate methods to print the workshop details (date and classroom), a method to print out the students and one to print out the coaches. Call these from print_details instead of having all the code there.

    Hint: look into defining private class methods.

Plagiarism

Take a moment to refamiliarize yourself with the Plagiarism policy. Plagiarized work will not be accepted.
Contributors

Original content from DC at f01e95. Original contributors can be found in that repository's history. Recent contributors can be found in this repository's history.
License

    All content is licensed under a CC­BY­NC­SA 4.0 license.
    All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.













"""