class Person:

    # YOUR CODE GOES HERE
    def __init__(self, id, name):
        '''(Person, int, str) -> None'''
        self.id = id
        self.name = name
        self.friends = []

    def add_friends(self, friend):
        '''(Person, str) -> None'''
        self.friends.append(friend)

    def get_friends(self):
        '''(Person) -> list'''
        return self.friends

    def __repr__(self):
        '''(Person) -> str'''
        return "Person({}, {}, {})".format(self.id, self.name, self.friends)

    def __str__(self):
        '''(Person) -> str'''
        return "Person({}, {}, {})".format(self.id, self.name, self.friends)


class Network:
    # YOUR CODE GOES HERE
    def __init__(self,file1,file2):
        '''(Network, str, str) -> None'''
        self.network = []
        for i in open(file1).read().splitlines():
            tmp = i.split("\t")
            self.network.append(Person(int(tmp[0]),tmp[1]))
        for i in open(file2).read().splitlines():
            if(len(i.split(" "))<2): continue
            temp = i.split(" ")
            temp[0] = int(temp[0])
            temp[1] = int(temp[1])
            for j in self.network:
                if j.id == temp[0]:
                    j.friends.append(temp[1])
                    break
            for j in self.network:
                if j.id == temp[1]:
                    j.friends.append(temp[0])
                    break
        for i in self.network:
            i.friends.sort()

    def __repr__(self):
        '''(Network) -> str'''
        return 'Network({})'.format(self.network)

    def __str__(self):
        '''(Network) -> str'''
        return 'Network({})'.format(self.network)

    def __len__(self):
        '''(Network) -> int'''
        return len(self.network)

    def get_uid(self):
        '''(2Dlist)->int'''
        while True:
            try:
                id = int(input("Enter an integer for a user ID: "))
                for i in self.network:
                    if i.id == id:
                        return id
                print("That user ID does not exist. Try again.")
            except:
                print("That was not an integer. Please try again.")

    def recommend(self, user):
        '''(int, 2Dlist)->int or None
        Given a 2D-list for friendship network, returns None if there is no other person
        who has at least one neighbour in common with the given user and who the user does
        not know already.

        Otherwise it returns the ID of the recommended friend. A recommended friend is a person
        you are not already friends with and with whom you have the most friends in common in the whole network.
        If there is more than one person with whom you have the maximum number of friends in common
        return the one with the smallest ID. '''

        # YOUR CODE GOES HERE
        max = None
        max_count = 0
        for i in self.network:
            if i.id == user:
                for j in self.network:
                    if j.id != i.id and j.id not in i.friends:
                        tmp = len(self.getCommonFriends(i.id, j.id))
                        if tmp > max_count:
                            max_count = tmp
                            max = j.id
                        elif tmp == max_count and max != None:
                            max = min(j.id, max)
        return max

    def getCommonFriends(self, user1, user2):
        '''(int, int, 2D list) -> list
        Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
        and friends of user 1 and user 2 sorted
        Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
        '''
        common = []

        # YOUR CODE GOES HERE
        for i in self.network:
            if i.id == user1:
                for j in self.network:
                    if j.id == user2:
                        for k in i.friends:
                            if k in j.friends:
                                common.append(k)

        return common


def get_int():
    '''None->int or None'''
    num = None
    try:
        num=int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num           

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name





##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1=get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2=get_file_name()


net=Network(file_name1,file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net)<=20:
    print(net)


print("\nLet's recommend a friend for a user you specify.")
uid=net.get_uid()
rec=net.recommend(uid)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(net.getCommonFriends(uid,rec)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=net.get_uid()
print("About 2st user ...")
uid2=net.get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=net.getCommonFriends(uid1,uid2)
for item in common:
    print(item, end=" ")



    
