from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

# This function is for turing right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This is the main function
def main():
    # traversing up
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_left()
            move()
            turn_right()
    turn_right()

    # traversing down
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
