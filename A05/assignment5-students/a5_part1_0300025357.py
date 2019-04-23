def largest_34(a):
    '''(list) -> num
    Preconditions: numbers in list a are all distinct and a has at least 4 elements
    Returns the sum of the 3rd and 4th largest values in a'''
    a.sort()
    return a[-3] + a[-4]

def largest_third(a):
    '''(list) -> num
    Preconditions: numbers in list a are all distinct and a has at least 3 elements
    Returns the sum of the last third of the list'''
    a.sort()
    return sum(a[len(a)-len(a)//3:len(a)])

def third_at_least(a):
    '''(list) -> element of list or None
    Preconditions: a has at least 4 elements
    Returns a value in a that occurs len(a)//3 + 1 in a'''
    for i in range(len(a)):
        count = 1
        for j in range(len(a)-i):
            if a[i] == a[j]:
                count +=1
        if count >= len(a)//3+1:
            return a[i]
    return None

def sum_tri(a,x):
    '''(list, int) -> bool
    Preconditions: a is a list of integers with at leas 3 values
    Returns True if sum of any three values of a is equal to x'''
    for i in range(len(a)):
        for j in range(len(a)-i):
            for k in range(len(a)-j):
                if a[i] + a[j] + a[k] == x:
                    return True
    return False

