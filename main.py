"""Practice session 4"""
import Logic

command = input("Select the exercise from 1-15: ")
while command != "exit":
    match command:
        case "1":
            Logic.ex1()
        case "2":
            Logic.ex2()
        case "3":
            Logic.ex3()
        case "4":
            Logic.ex4()
        case "5":
            Logic.ex5()
        case "6":
            Logic.ex6()
        case "7":
            Logic.ex7()
        case "8":
            Logic.ex8()
        case "9":
            Logic.ex9()
        case "10":
            Logic.ex10()
        case "11":
            Logic.ex11()
        case "12":
            Logic.ex12()
        case "13":
            Logic.ex13()
        case "14":
            Logic.ex14()
        case "15":
            Logic.ex15()
    command = input("Select the exercise from 1-15: ")