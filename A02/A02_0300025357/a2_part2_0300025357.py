#####################################
#2.01
#####################################
def min_enclosing_rectangle(radius, x, y):
    '''(float, float, float) -> tuple
    Preconditions: radius and x and y are non-negative numbers
    Return coordinates of bottom-left corner of triangle containing the circle'''
    if radius <= 0 or x <= 0 or y <= 0:
        return None
    else:
        return(x-radius,y-radius)

#####################################
#2.02
#####################################
def series_sum():
    '''Returns the sum of a given series'''
    n = int(input("Please enter a non-negative integer: "))
    base = 1000
    denomenator = 1
    if n >= 0:
        for i in range(1, n):
            base = base + (1/i)**2
        return base
    elif n < 1:
        return None
    
#####################################
#2.03
#####################################
def pell(n):
    '''(int) -> int
    Preconditions: n is non-negative
    Returns the nth number in the Pell sequence'''
    if n == 0 or n == 1:
        return n
    if n < 0:
        return None
    else:
        return 2*pell(n-1) + pell(n-2)
    
#####################################
#2.04
#####################################
def countMembers(s):
    '''(str) -> int
    Returns number of occurences of specific characters in s'''
    count = 0
    incl = "efghijFGHIJKLMNOPQRSTUVWX23456!,\\"
    for char in s:
        for i in incl:
            if char == i:
                count = count + 1
    return count
                
#####################################
#2.05
#####################################
def casual_number(s):
    '''(str) -> int
    Preconditions: three digit gap must exist between commas, ',', if the number is to be processed
    Returns integer representing the number in s'''
    incl = "0123456789,-"
    new_build = ''
    for i in range(len(s)):
        if (s[i] in incl):
            if (s[i] == '-' and s[i+1] != s[i] and i == 0):
                new_build = new_build + s[i]
            if s[i] == ',' and s[i+1] != s[i] and s[i-1] != '-' and i != 0:
                new_build = new_build  
            else:
                new_build = new_build + s[i]
        else:
            return None
    return int(new_build)

#####################################
#2.06
#####################################
def alienNumbers(s):
    '''(str) -> int
    Preconditions: s cannot contain other than T y ! a N U
    Returns an integer translation of the alien string'''
    return s.count("T")*1024 + s.count("y")*598 + s.count("!")*121 + s.count("a")*42 + s.count("N")*6 + s.count("U")*1

#####################################
#2.07
#####################################
def alienNumbersAgain(s):
    '''(str) -> int
    Preconditions: s cannot contain other than T y ! a N U
    Returns an integer translation of the alien string'''
    count = 0
    incl = 'Ty!aNU'
    for char in s:
        for i in incl:
            if char == i:
                if i == 'T':
                    count = count + 1024
                elif i == 'y':
                    count = count + 597
                elif i == '!':
                    count = count + 121
                elif i == 'a':
                    count = count + 42
                elif i == 'N':
                    count = count + 6
                elif i == 'U':
                    count = count + 1
    return count

#####################################
#2.8
#####################################
def encrypt(s):
    '''(str) -> str
    Returns an encrypted string'''
    s = s[::-1]
    no_char = ''
    num = ''
    symb = ''
    for char in s:
        if char.isalpha() == True:
            no_char = no_char + char
        elif char in '0123456789':
            num = num + char
        else:
            symb = symb + char        
    encryption = ''
    numb = ''
    for i in range(len(no_char)):
        encryption = encryption + no_char[i] + no_char[-(i+1)]
    for i in range(len(num)):
        numb = numb + num[i] + num[-(i+1)]
    return encryption[0:int(len(encryption)/2)] + numb[0:int(len(numb)/2)] + symb
        
#####################################
#2.09
#####################################
def oPify(s):
    '''(str) -> str
    Returns a string with 'op' inserted between every two consecutive alphabets'''
    
    new_build = ''
    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i].isalpha() == True and s[i+1].isalpha() == True:
                if s[i].isupper() == True:
                    new_build = new_build + s[i] + 'O'
                else:
                    new_build = new_build + s[i] + 'o'
                if s[i+1].isupper() == True:
                    new_build = new_build + 'P'
                else:
                    new_build = new_build + 'p'
            else:
                new_build = new_build + s[i]
        else:
            new_build = new_build + s[i] 
    return new_build

#####################################
#2.10
#####################################
def nonrepetitive(s):
    '''(str) -> bool
    Preconditions: s is strictly alphabetical (lower-case preferred)'''
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if (s[i:j]) == s[j:j+len(s[i:j])]:
                return False
    return True
