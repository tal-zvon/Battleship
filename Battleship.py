import random
import os
import signal
import sys

__author__ = 'tal'
Grid_Size = 10
PC_location = [random.randint(0, Grid_Size - 1), random.randint(0, Grid_Size - 1)]
CHEATING = True  # Shows you what the computer grid looks like


def player_message():
    #Clear screen
    os.system('clear 2>/dev/null')

    #Draw Grids
    draw_grids()

    #Write message to screen what the shot was, and if it was a hit or miss
    print '\n'
    print 'You have shot (%d,%d).' % (player_shot[0], player_shot[1]),
    if Computer_Grid[player_shot[0]][player_shot[1]].ship_here:
        print "HIT!"
    else:
        print "MISS!"
    raw_input("Press enter to continue.")


def signal_handler(signal, frame):
    print "\n"
    print "You sank my battleship!"
    sys.exit(0)


def computer_turn():
    while True:
        rnd = [random.randint(0, Grid_Size - 1), random.randint(0, Grid_Size - 1)]

        #Make sure the computer hasn't shot that spot before
        if not Player_Grid[rnd[0]][rnd[1]].already_tried:
            Player_Grid[rnd[0]][rnd[1]].already_tried = True

            #Clear screen
            os.system('clear 2>/dev/null')

            #Draw Grids
            draw_grids()

            #Write message to screen what the shot was, and if it was a hit or miss
            print '\n'
            print 'Computer has shot (%d,%d).' % (rnd[0], rnd[1]),
            if Player_Grid[rnd[0]][rnd[1]].ship_here:
                print "HIT!"
            else:
                print "MISS!"
            raw_input("Press enter to continue.")
            break


def check_win():
    #Check if player won
    if (Player_Grid[P1_location[0]][P1_location[1]].already_tried is True and
                Player_Grid[P1_location[0] + 1][P1_location[1]].already_tried is True and
                Player_Grid[P1_location[0] + 2][P1_location[1]].already_tried is True and
                Player_Grid[P1_location[0] + 3][P1_location[1]].already_tried is True):
        #Show losing message
        print '\n'
        print '====================='
        print '======YOU LOSE!======'
        print '====================='
        exit(0)

    #Check if computer won
    if (Computer_Grid[PC_location[0]][PC_location[1]].already_tried is True and
                Computer_Grid[PC_location[0] + 1][PC_location[1]].already_tried is True and
                Computer_Grid[PC_location[0] + 2][PC_location[1]].already_tried is True and
                Computer_Grid[PC_location[0] + 3][PC_location[1]].already_tried is True):
        #Clear screen
        os.system('clear 2>/dev/null')

        #Draw Grids
        draw_grids()

        #Show winning message
        print '\n'
        print '===================='
        print '======YOU WIN!======'
        print '===================='
        exit(0)


def draw_x_axes():
    print '  ',
    print '-' * (Grid_Size * 2),
    print '               |               ',
    print '  ',
    print '-' * (Grid_Size * 2)
    print '   ',
    for i in range(0, Grid_Size):
        print i,
    print '                               ',
    print '   ',
    for i in range(0, Grid_Size):
        print i,


def draw_grids():
    #Draw graph labels
    print '          Player                                                 Computer\n'
    #This runs for every horizontal line in the grid
    for y in reversed(range(0, Grid_Size)):

        print y,
        print '|',
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

        print y,
        print '|',
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
    #Drag X axes
    draw_x_axes()


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
            return False

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

#Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#Generate 2 grids
Player_Grid = [[Coordinate(False, False) for i in range(10)] for j in range(10)]
Computer_Grid = [[Coordinate(False, False) for i in range(10)] for j in range(10)]

#Clear screen
os.system('clear 2>/dev/null')

for y in reversed(range(0, Grid_Size)):
    for x in range(0, Grid_Size):
        print "(%d,%d)" % (x, y),
    print

#print '\nPick a coordinate to place your ship: ',
P1_location = raw_input("\nThis is what the grid looks like.\nPick a coordinate to place your ship (ex: 1,4): ")
P1_location = P1_location.replace("(", "")
P1_location = P1_location.replace(")", "")

#Convert to int
P1_location = convert_to_int(P1_location)
if P1_location is False:
    exit(1)

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
    os.system('clear 2>/dev/null')

    #Draw Grids
    draw_grids()

    #Player's turn
    print '\n'
    player_shot = raw_input("Where would you like to shoot? (ex: 1,4): ")
    player_shot = player_shot.replace("(", "")
    player_shot = player_shot.replace(")", "")

    #Convert to int
    player_shot = convert_to_int(player_shot)
    if player_shot is False:
        raw_input("Press enter to continue.")
        continue

    #Check if input is valid
    check_input(player_shot)

    #Check if you've already shot there
    if Computer_Grid[player_shot[0]][player_shot[1]].already_tried:
        print "\nYou've already tried shooting there!"
        raw_input("Press enter to continue.")
        continue
    else:
        Computer_Grid[player_shot[0]][player_shot[1]].already_tried = True
        #Write message to screen to show what you shot, and if it was a hit or miss
        player_message()

    #Check if anyone won
    check_win()

    #Computer's turn
    computer_turn()

    #Check if anyone won
    check_win()