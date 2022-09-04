def get_name():
    name = input("What is your name?")
    return(name)

def say_name(name):
    say = f"your name is : {name}"
    print(say)

def get_and_say():
    name = get_name()
    say_name(name)
    

get_and_say()
print('Hello')