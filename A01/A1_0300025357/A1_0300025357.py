import turtle
import math


s=turtle.Screen()
t=turtle.Turtle()


#Question 01
def mh2kh(s):
    '''(float) -> float
    Preconditions: s is non-negative
    Returns speed in km/h given miles/h'''
    return s * 1.609


#Question 02
def pythogorean_pair(a,b):
    '''(int) -> bool
    Returns True if a and b are pythogorean pairs, false if not'''
    return int == type(a) and int == type(b) and ((((a**2)+(b**2))**(1/2))%1) == 0


#Question 03
def in_out(xs,ys,side):
    '''(float, float, float) -> bool
    Preconditions: xs, ys, and side are non-negative
    Returns True if input point is inside square, False if not'''
    x = float(input("Enter a non-negative X parameter of point: "))
    y = float(input("Enter a non-negative Y parameter of point: "))
    return (x>=xs and x<=(xs+side)) and (y>= ys and y<=(ys+side))


#Question 04
def safe(n):
    '''(int) -> bool
    Preconditions: n is non-negative and no more than 2 digits
    Returns True if n doesnt contain 9 and is non-divisible by 9, False otherwise'''
    return n%10 != 9 and n%9 != 0 and n < 90


#Question 05
def quote_maker(quote, name, year):
    '''(str, str, int) -> str
    Returns a sentence containing input strings and integer'''
    return 'In ' + str(year) + ', a person called ' + str(name) + ' said: "' + str(quote) + '"'


#Question 06
def quote_displayer():
    '''() -> None
    Prints a sentence based on input promts and recalls quote_maker(quote, name, year)'''
    x = input("Enter a quote: ")
    y = input("Enter name of person whose quote was mentioned: ")
    z = input("Enter the year said quote was told by person: ")
    print(quote_maker(x,y,z))


#Question 07
def rps_winner():
    '''() -> None
    Prints results for a match of rock, paper, scissors'''
    print("What choice did player 1 make?")
    player1 = input("Type one of the following options: rock, paper, scissors: ")
    print("What choice did player 2 make?")
    player2 = input("Type one of the following options: rock, paper, scissors: ")
    print("player 1 beat player 2?", ((player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock")))
    print("players tied?", player1 == player2)


#Question 08
def fun(x):
    '''(float) -> float
    Preconditions: x is non-negative
    Returns float 'y' based on the equation 10**(4*y) = x + 3'''
    y = math.log((x+3),10) / 4
    return y


#Question 09
def ascii_name_plaque(name):
    '''(str) -> None
    Prints a name plaque varying in size based on input string'''
    star = '*' 
    star = star * (len(name) + 10)
    space = ' ' * (len(name) + 8)
    print(star)
    print('*' + space + '*')
    print("*  __" + name + "__  *")
    print('*' + space + '*')
    print(star)

#Question 10
def draw_bike():
    '''() -> None
    Returns a drawing of a bike'''
    t.penup()
    t.goto(-250, -150)
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(-250, -135.5)
    t.pendown()
    t.circle(85)
    t.penup()
    t.goto(-250, -70)
    t.pendown()
    t.circle(20)
    t.penup()
    t.goto(-112,-110)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(-112,-94.5)
    t.pendown()
    t.circle(25)
    t.penup()
    t.goto(175, -150)
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(175, -135.5)
    t.pendown()
    t.circle(85)
    t.penup()
    t.goto(175, -70)
    t.pendown()
    t.circle(20)
    t.penup()
    t.goto(-175,100)
    t.pendown()
    t.goto(135, 100)
    t.penup()
    t.goto(-180,115)
    t.pendown()
    t.goto(135, 115)
    t.penup()
    t.goto(135, 150)
    t.pendown()
    t.goto(135, 115)
    t.penup()
    t.goto(150, 143)
    t.pendown()
    t.goto(150, -15)
    t.penup()
    t.goto(135, 100)
    t.pendown()
    t.goto(135, -15)
    t.penup()
    t.goto(150, -15)
    t.pendown()
    t.goto(165, -34)
    t.penup()
    t.goto(135, -15)
    t.pendown()
    t.goto(157,-42)
    t.penup()
    t.goto(-125,-32)
    t.pendown()
    t.goto(-175, 100)
    t.penup()
    t.goto(-138,-38)
    t.pendown()
    t.goto(-190, 100)
    t.penup()
    t.goto(-190, 100)
    t.pendown()
    t.goto(-235,-40)
    t.penup()
    t.goto(-200, 115)
    t.pendown()
    t.goto(-247,-30)
    t.goto(-200, 115)
    t.pendown()
    t.goto(-210, 140)
    t.goto(-165, 140)
    t.goto(-165, 160)
    t.goto(-250, 160)
    t.goto(-250, 140)
    t.goto(-190, 140)
    t.goto(-180, 115)
    t.penup()
    t.goto(180, 130)
    t.pendown()
    t.goto(180, 150)
    t.goto(115, 180)
    t.goto(115, 160)
    t.goto(180, 130)
    t.penup()
    t.goto(-232,-41)
    t.pendown()
    t.goto(-150,-55)
    t.penup()
    t.goto(-233,-57)
    t.pendown()
    t.goto(-150, -70)
    t.penup()
    t.goto(-120,-93)
    t.pendown()
    t.goto(-130,-145)
    t.penup()
    t.goto(-130,-88)
    t.pendown()
    t.goto(-140,-145)
    t.penup()
    t.goto(-155,-145)
    t.pendown()
    t.goto(-115,-145)
    t.goto(-115,-150)
    t.goto(-155,-150)
    t.goto(-155,-145)
    t.penup()
    t.goto(-70,0)
    t.pendown()
    t.goto(-85,-43)
    t.penup()
    t.goto(-80,0)
    t.pendown()
    t.goto(-95,-32)
    t.penup()
    t.goto(-80,0)
    t.pendown()
    t.goto(-100,0)
    t.goto(-100,5)
    t.goto(-65, 5)
    t.goto(-65, 0)
    t.goto(-80,0)


#Question 11
def alogical(n):
    '''(float) -> int
    Preconditions: n is bigger or equal to 1
    Returns the minimum number of times n has to be divided to be equal or less than 1'''
    return math.ceil(math.log(n,2))


#Question 12
def time_format(h,m):
    '''(int, int) -> str
    Preconditions: h is non-negative and less than or equal to 24, m is non-negative and less than or equal to 59
    Returns the time as a descriptive string'''
    hours = h
    second_digit_minute = 0
    if (m%10) >= 3 and (m%10) <= 7:
        first_digit_minute = 5
    else:
        first_digit_minute = 0
        if (m%10) >= 7:
            second_digit_minute = 1
    minute_count = (m//10 + second_digit_minute)*10 + first_digit_minute
    if minute_count == 30:
        minutes = 'half past '
    elif minute_count > 30:
        minutes = str(60 - minute_count) + ' to '
        hours = (h + 1)%24
    elif minute_count >= 59:
        minute_count = 0
    else:
        minutes = str(m) + ' past '
    if m == 0:
        return str(hours) + " o'clock"
    else:
        return minutes + str(hours) + " o'clock"


#Question 13
def cad_cashier(price,payment):
    '''(float, float) -> float
    Preconditions: price and payment are non-negative numbers, payment is equal or larger than price,
        both are limited to two decimal places
    Returns a real non-negative number that's the difference between price and payment'''
    change = payment - price
    change_rounded = round(0.05*round(change/0.05), 2)
    return change_rounded


#Question 14
def min_CAD_coins(price, payment):
    '''(float, float) -> (int, int, int, int, int)
    Preconditions: price and payment are non-negative numbers, payment is equal or larger than price,
        both are limited to two decimal places
    Returns amount of toonies, loonies, quarters, dimes and nickles required to pay off change'''
    change = cad_cashier(price, payment)
    t = int(change//2)
    l = int((change%2)//1)
    q = int((change%1)//0.25)
    d = int((change%0.25)//0.10)
    n = int(round((change%0.10), 2)//0.05)
    return (t, l, q, d, n)
    


    

    
