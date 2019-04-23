import math
import random


def primary_school_quiz(flag, n):
    '''(int, int) -> int
    Preconditions: flag and n are non-negative numbers
    Returns number of the generated answers that were answered correctly'''
    result = 0
    for i in range(n):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if flag == 0:
            print("Question", i+1)
            ans = int(input("What is the result of " + str(x) + "-" + str(y) + " ? "))
            if ans == (x - y):
                result = result + 1
        if flag == 1:
            print("Question", i+1)
            ans = int(input("What is the result of " + str(x) + "^" + str(y) + " ? "))
            if ans == (x**y):
                result = result + 1
    return result


def high_school_eqsolver(a,b,c):
    '''(float, float, float) -> None'''
    quad_eq = str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0"
    sqrt = b^2 - 4*a*c
    if sqrt >= 0:
        plus_sqrt = (-1*b + math.sqrt(sqrt)) / (2*a)
        neg_sqrt = (-1*b - math.sqrt(sqrt)) / (2*a)
        print("The quaderatic equation " + quad_eq + "\nhas the following real roots:")
        print(str(plus_sqrt) + " and " + str(neg_sqrt))
    elif sqrt <= -1:
        plus_sqrt = str((-1*b)/2) + "i " + str(math.sqrt(-sqrt)/(2*a))
        neg_sqrt = str((-1*b)/2) - "i " + str(math.sqrt(-sqrt)/(2*a))
        print("The quaderatic equation \n" + quad_eq + "\nhas the following complex roots:")
        print(plus_sqrt) + "\n and " + neg_sqrt





# main

print("*************************************************************")
print("*                                                           *")
print("*  __Welcome to my math quiz-generator / equation-solver__  *")
print("*                                                           *")
print("*************************************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    string = "  __" + name + ", Welcome to my quiz-generator for primary school students.__  "
    print("*" * (len(string) + 2))
    print("*" + (" " * len(string)) + "*")
    print("*" + string + "*")
    print("*" + (" " * len(string)) + "*")
    print("*" * (len(string) + 2))
    
    ques_type = int(input(name + ", what would you like to practice? Enter \n0 for subtraction \n1 for exponentiation \n"))
    ques_num = int(input("How many practice questions would you like to do? "))
    print(name + ", here is/are your " + str(ques_num) + " question(s):")
    result = primary_school_quiz(ques_type, ques_num)
    if result/ques_num >= 0.9:
        print("Congratulations " + name + ", You'll probably get an A tomorrow. Now go eat your dinner and go to sleep. Good bye " + name)
    elif result/ques_num >= 0.7:
        print("You did well, " + name + ", but I know you can do better.")
    else:
        print("I think you need more practice " + name + ".")

elif status=='2':
    string = "  __quadratic equation, a·x^2 + b·x + c = 0, solver for " + name + "__  "
    print("*" * (len(string) + 2))
    print("*" + (" " * len(string)) + "*")
    print("*" + string + "*")
    print("*" + (" " * len(string)) + "*")
    print("*" * (len(string) + 2))
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = int(input("Enter a number the coeffecient a: "))
            b = int(input("Enter a number the coeffecient b: "))
            c = int(input("Enter a number the coeffecient c: "))

            high_school_eqsolver(a,b,c)
 
else:
    print(name + ", you are not a target audience for this software.")

print("Good bye "+name+"!")
