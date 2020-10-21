from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
# This is an editor! Write your solution here.
# Make karel create four columns of beepers
# This function is for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this function is for building a column
def build_column():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if front_is_blocked() and no_beepers_present():
        put_beeper()

# this function is for going down a column
def go_down():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

# this function is to move to the next column
def go_to_next_column():
    move()
    move()
    move()
    move()
    turn_left()

# the main program starts here
def main():
    #  put_beeper()
    turn_left()
    build_column()
    go_down()
    #   while front_is_clear():
    go_to_next_column()
    build_column()
    #   if beepers_present():
    #      go_down()
    #   else:
    #      put_beeper()
    go_down()
    go_to_next_column()
    build_column()
    go_down()
    go_to_next_column()
    build_column()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
