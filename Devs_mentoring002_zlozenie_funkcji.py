def say_hello():
    print("Hello")
    
    
    
func_var = say_hello
say_hello() #Hello!
func_var() #Hello!



def say_hello():
    print("Hello")
    
def say_goodbye():
    print("Goodbye!")
    
def operate(what_to_say):
    print("I want to say...")
    what_to_say()
    print("Greetings!")
    
operate(say_hello)
operate(say_goodbye)

print("przykład nr2")


def outer_func():
    print("Outer!")
    
    def inner_func():
        print("Inner!")
    
    return inner_func

var =outer_func() #outer!
var() #Inner!     
