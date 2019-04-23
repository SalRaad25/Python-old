import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    random.shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of int, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    for i in range(len(original_board)):
        if i == p1 or i == p2 or discovered.count(i) > 0:
            print('{0:4}'.format(original_board[i]), end=' ')
        else:
            print('{0:4}'.format('*'), end=' ')
    print()
    for i in range(len(original_board)):
        print('{0:4}'.format(str(i+1)), end=' ')

def hidden_board(discovered, a):
    '''(list of int, list of str)->None
       Prints the current board in hidden manner
    '''
    for i in range(len(a)):
        if discovered.count(i) > 0:
            print('{0:4}'.format(a[i]), end=' ')
        else:
            print('{0:4}'.format('*'), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE
    try:
        for i in range(len(l)):
            counter = 1
            for e in range(len(l)):
                if l[i] == l[e] and i != e:
                    counter = counter + 1
            if counter%2 == 0:
                playable_board.append(l[i])
            else:
                l.pop(i)
    except:
        pass

    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    # YOUR CODE GOES HERE
    if len(l) != 0:
        for i in range(len(l)):
            counter = 1
            for e in range(len(l)):
                if l[i] == l[e] and i != e:
                    counter = counter + 1
            return counter == 2
    else:
        return True
 
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    # this is the funciton that plays the game
    # YOUR CODE GOES HERE

    print("Ready to play ...\n")
    game_run = True
    discovered = []
    guessCTR=0
    while game_run:
        hidden_board(discovered, board)
        print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board)) + "]")
        p1 = int(input("Enter position 1: ")) - 1
        while p1 < 0 or p1 > len(board)-1:
            p1 = int(input("Enter position 1: ")) - 1
        p2 = int(input("Enter position 2: ")) - 1
        while p2 < 0 or p2 > len(board)-1 or p1 == p2:
            p2 = int(input("Enter position 2: ")) - 1
        print_revealed(discovered, p1, p2, board)
        print("\n")
        if(board[p1]==board[p2]):
            discovered.append(p1)
            discovered.append(p2)
            print('Pair Found!')
        guessCTR = guessCTR+1
        if(len(discovered)==len(board)):
            game_run=False;
    print("Game completed in", guessCTR, "Guesses. Minimum possible is", len(board)//2, "guesses.")
        
            
        
    




#main
run = True

print("******************************************")
print("*                                        *")
print("*  __Welcome to my Concentration game__  *")
print("*                                        *")
print("******************************************")
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
choice = input("Would you like (enter 1 or 2 to indicate your choice): \n(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file? \n")
while (choice != '1') and (choice != '2'):
    choice = input(str(choice) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice \n")
        
# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)
if choice == '1':
    print("You chose to have a rigorous deck generated for you")
    print("\nHow many cards do you want to play with?")
    card_count = int(input("Enter an even number between 0 and 52: "))
    while (card_count%2 != 0) or (card_count < 0) or (card_count > 52):
        card_count = int(input("Enter an even number between 0 and 52: "))
    board = create_board(card_count)
    shuffle_deck(board)
    play_game(board)
                
                
            
        

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
if choice == '2':
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    play_game(board)


    

