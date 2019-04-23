def digit_sum(n):
    '''(int) -> int
    Preconditions: n is a non-negative integer
    Returns the sum of all the digits of the non-negative integer'''
    if n < 10:
        return n
    else:
        return n%10 + digit_sum(n//10)



def digital_root(n):
    '''(int) -> int
    Preconditions: n is a non-negative integer
    Returns digital root of integer number'''
    if n < 10:
        return n
    else:
        return digital_root(digit_sum(n))