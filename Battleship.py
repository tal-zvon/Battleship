import random

__author__ = 'tal'
Grid_Size = 10
PC_location = [random.randint(0, Grid_Size - 1), random.randint(0, Grid_Size - 1)]
CHEATING = False  # Shows you what the computer grid looks like


def draw_grids():
    #This runs for every horizontal line in the grid
    for y in reversed(range(0, Grid_Size)):

        #This prints the Player's grid
        for x in range(0, Grid_Size):
            if Player_Grid[x][y].already_tried and Player_Grid[x][y].ship_here:
                print '*',
            elif Player_Grid[x][y].already_tried:
                print 'X',
            elif Player_Grid[x][y].ship_here:
                print '-',
            else:
                print 'O',

        #The separator between the Player's grid and the Computer's grid
        print '               |               ',

        #This prints the Computer's grid
        for x2 in range(0, Grid_Size):
            if Computer_Grid[x2][y].already_tried and Computer_Grid[x2][y].ship_here:
                print '*',
            elif Computer_Grid[x2][y].already_tried:
                print 'X',
            elif Computer_Grid[x2][y].ship_here:
                if CHEATING:
                    print '-',
                else:
                    print 'O',
            else:
                print 'O',
        print ''


def place_ships():
    for i in range(P1_location[0], P1_location[0] + 4):
        Player_Grid[i][P1_location[1]].ship_here = True
    for i in range(PC_location[0], PC_location[0] + 4):
        Computer_Grid[i][PC_location[1]].ship_here = True


def adjust_coord(coord):
    if coord[0] > (Grid_Size - 4):
        coord[0] = (Grid_Size - 4)

    return coord


def convert_to_int(coordinates):
    coordinates = coordinates.split(',')
    for i in range(0, len(coordinates)):
        try:
            coordinates[i] = int(coordinates[i])
        except ValueError:
            print "'%s' is not a number!" % coordinates[i]
            exit(1)

    return coordinates


def check_input(input_coord):
    """Check if input is valid"""
    #Check if list is of proper size:
    if len(input_coord) != 2:
        print 'Improper input detected - too many variables!'
        exit(1)

    if input_coord[0] >= Grid_Size:
        print 'Your x coordinate is out of bounds!'
        exit(1)

    if input_coord[1] >= Grid_Size:
        print 'Your y coordinate is out of bounds!'
        exit(1)


class Coordinate(object):
    def __init__(self, ship_here, already_tried):
        """
        :rtype : None
        :param ship_here: True if part of ship is at these coordinates, False otherwise
        :param already_tried: True if we already bombed these coordinates, False otherwise
        """

        self.ship_here = ship_here
        self.already_tried = already_tried

#Generate 2 grids
Player_Grid = [[Coordinate(False, False) for i in range(10)] for j in range(10)]
Computer_Grid = [[Coordinate(False, False) for i in range(10)] for j in range(10)]

for y in reversed(range(0, Grid_Size)):
    for x in range(0, Grid_Size):
        print "(%d,%d)" % (x, y),
    print

#print '\nPick a coordinate to place your ship: ',
P1_location = raw_input("\nPick a coordinate to place your ship (ex: 1,4): ")

#Convert to int
P1_location = convert_to_int(P1_location)

#Check if input is valid
check_input(P1_location)

#Adjust coordinates
P1_location = adjust_coord(P1_location)
PC_location = adjust_coord(PC_location)

#Place ships on grid
place_ships()

#While loop
while True:
    #Clear screen

    #Draw Grids
    draw_grids()

    #Player's turn

    #Computer's turn

    #Temporary break. Remove later
    break