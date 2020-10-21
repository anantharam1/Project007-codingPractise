from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

# This function is for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This function is for placing beepers
def place_beepers():
    while left_is_blocked():
        put_beeper()
        move()

# This function is for moving left
def left_move():
    place_beepers()
    turn_left()
    move()

# This function is for moving right
def right_move():
    place_beepers()
    turn_right()
    put_beeper()
    move()

# the main program starts here
def main():
    left_move()
    left_move()
    right_move()
    left_move()
    left_move()
    right_move()
    left_move()
    left_move()
    place_beepers()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
