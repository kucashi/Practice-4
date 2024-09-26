"""Functions to solve the practice problem. Beside 'multiple' function the rest of them could have been written directly in main.py file."""

def multiple(number, divisor):
    figure_sum = sum(int(figure) for figure in number)
    if figure_sum % divisor == 0:
        print(f"{number} divides by {divisor}")
    else:
        print(f"{number} does not divides by {divisor}")

def ex1():
    a = int(input("please insert a natural number a = "))
    b = int(input("please insert a natural number b = "))
    if a > b:
        print("a - b =", a - b)
    else:
        print("b - a =", b - a)

def ex2():
    number = input("please enter a number: ")
    three_multiple = 0
    if int(number) % 2 == 0:
        print(int(number) + int(number[2]))
    else:
        multiple(number, 3)

def ex3():
    user = "windows_user"
    passw = "P@rolla"
    username = input("enter a username: ")
    password = input("enter a password: ")

    if user == username and passw == password:
        print(f"{username} logged successfully!")
        first_name = input("enter your first name: ")
        sur_name = input("enter your sur name: ")
        email = input("enter your email: ")
        it_experience = float(input("enter your it experience in years: "))
        if it_experience < 1.5:
            print(f"{first_name} {sur_name} is junior")
        elif 1.5 <= it_experience <= 3:
            print(f"{first_name} {sur_name} is intermediate")
        else:
            print(f"{first_name} {sur_name} is senior")
    else:
        print("please check credentials")

def ex4():
    file_name = input("enter a file name with extension: ")
    extension = file_name[file_name.rfind(".") + 1::]
    print(extension)

def ex5():
    phrase = input("enter a phrase: ")
    words = phrase.split(" ")
    print(len(words))

def ex6():
    time = int(input("enter a time: "))
    if time < 0:
        print("enter a positive number !")
        return
    phase = time % 5
    if phase <= 2:
        print("green")
    else:
        print("red")

def ex7():
    command = "platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …"
    start_index = command.rfind(":")
    end_index = command.rfind(";")
    print(command[start_index + 2 : end_index])

def ex8():
    message = input("enter your message: ")
    if message.isnumeric():
        print(pow(float(message), 2))
    else:
        print(message)

def ex9():
    message = input("enter you message: ")
    spaces = message.split(" ")
    if len(spaces) > 1:
        print("spaces = ", len(spaces) - 1)
    else:
        print("there are no spaces")

def ex10():
    number = input("enter a number: ")
    multiple(number, 8)

def ex11():
    email = input("enter your email: ")
    sub_string = email.rfind("@")
    if sub_string > 0:
        print(email[sub_string +1 ::])
    else:
        print("no domain entered")

def ex12():
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    message = input("enter your message: ")
    counter = 0
    for i in message:
        if vocals.__contains__(i):
            counter += 1
    print(f"there are {counter} vocals")

def ex13():
    message = input("enter your message: ")
    if message.isnumeric():
        print(float(message))
    else:
        print(message)

def ex14():
    number = input("enter a number: ")
    if int(number) > 100:
        print(sum(int(figure) for figure in number))
    else:
        number = "Python"
        print(number)

def ex15():
    message = input("enter your message: ")
    if message.startswith("Python"):
        print(True)
    else:
        print(False)