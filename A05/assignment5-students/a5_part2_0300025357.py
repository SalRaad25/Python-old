class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    'class that represents a 2D rectangle that can be drawn on the plane'

    def __init__(self, bot_left, top_right, color):
        '''(Rectangle, Point, Point, str) -> None
        Initializes the class variables'''
        self.bot_left = bot_left
        self.top_right = top_right
        self.color = color

    def get_bottom_left(self):
        '''(Retangle) -> Point
        Returns Point xy-coordinates of bottom left corner of the Rectangle'''
        return self.bot_left

    def get_top_right(self):
        '''(Retangle) -> Point
        Returns Point xy-coordinates of top right corner of the Rectangle'''
        return self.top_right

    def get_color(self):
        '''(Rectangle) -> str
        Returns Rectangle color'''
        return self.color

    def reset_color(self, color):
        '''(Rectangle, str) -> None
        Sets a different color for Rectangle'''
        self.color = color

    def get_perimeter(self):
        '''(Rectangle) -> number
        Returns the calculated perimeter for Rectangle'''
        return ((self.top_right.x - self.bot_left.x)+(self.top_right.y - self.bot_left.y))*2

    def get_area(self):
        '''(Rectangle) -> number
        Returns the calculated area for Rectangle'''
        return (self.top_right.x - self.bot_left.x)*(self.top_right.y - self.bot_left.y)

    def move(self, x, y):
        '''(Rectangle, number, number) -> None
        Resets Rectangle Point xy-coordinates by moving them'''
        self.bot_left.move(x,y)
        self.top_right.move(x,y)

    def intersects(self, other):
        '''(Rectangle, Rectangle) -> bool
        Returns True if the rectangles intersenct, False if they don't'''
        if self.top_right.x >= other.bot_left.x and self.top_right.y >= other.bot_left.y and self.bot_left.x <= other.top_right.x and self.bot_left.y <= other.top_right.y:
            return True
        elif self.bot_left.x <= other.top_right.x and self.bot_left.y <= other.top_right.y and self.top_right.x >= other.bot_left.x and self.top_right.y >= other.bot_left.y:
            return True
        return False

    def contains(self, x, y):
        '''(Rectangle, number, number) -> bool
        Returns True if the coordinates are withing the rectangle'''
        if (self.bot_left.x <= x <= self.top_right.x) and (self.bot_left.y <= y <= self.top_right.y):
            return True
        return False

    def __eq__(self, other):
        '''(Rectangle, Rectangle)->bool
        Returns True if self and other have the same Point coordinates'''
        return self.bot_left == other.bot_left and self.top_right == other.top_right and self.color == other.color

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(bot_left, top_right, color)'''
        return 'Rectangle(' + str(self.bot_left) + ',' + str(self.top_right) + ','+str(self.color) + ')'

    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Point(x, y).'''
        return 'I am a ' + str(self.color) + ' rectangle with bottom left corner at ' + str(self.bot_left) + ' and top right corner at ' + str(self.top_right)


class Canvas:

    def __init__(self):
        ''' (Canvas) -> None
        initialize canvas' array of rectangles'''
        self.list = []

    def add_one_rectangle(self, rec):
        '''(Canvas, Rectangle) -> None
        Adds rectangle to the Canvas array'''
        self.list.append(rec)

    def count_same_color(self, color):
        '''(Canvas, str) -> int
        Returns repetition of color withing rectangle array Canvas'''
        count = 0
        for i in self.list:
            if i.color == color:
                count +=1
        return count

    def total_perimeter(self):
        '''(Canvas) -> number
        Returns the calculated total perimeter of the rectangles inside Canvas'''
        perimeter = 0
        for i in self.list:
            perimeter = perimeter + i.get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
            '''(Canvas) -> Rectangle
            Returns the smallest rectangle that can enclose all rectangles in the canvas'''
            bot_left = None
            top_right = None
            for i in range(len(self.list)):
                if (i == 0):
                    bot_left = self.list[i].bot_left
                    top_right = self.list[i].top_right
                    continue
                if (bot_left.x > self.list[i].bot_left.x):
                    bot_left.setx(self.list[i].bot_left.x)
                if (bot_left.y > self.list[i].bot_left.y):
                    bot_left.sety(self.list[i].bot_left.y)
                if (top_right.x < self.list[i].top_right.x):
                    top_right.setx(self.list[i].top_right.x)
                if (top_right.y < self.list[i].top_right.y):
                    top_right.sety(self.list[i].top_right.y)
            return Rectangle(bot_left, top_right, "burgundy")

    def common_point(self):
        '''(Canvas) -> bool
        Returns True if all the rectangles in the Canvas intersect, False if not'''
        for i in range(len(self.list)):
            for j in range(i+1, len(self.list)):
                if self.list[i].intersects(self.list[j]) == False:
                    return False
        return True

    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation Canvas()'''
        return 'Canvas({})'.format(self.list)

    def __len__(self):
        '''(Canvas)->str
        Returns length of Canvas array'''
        return len(self.list)