# Define characters
default mc_name = "Mark"
define m = Character(mc_name)
define s = Character("Sarah")
define d = Character("David")

# Game variables
default love_score = 200
default max_love_score = 200 # Max ceiling for love score
default love_score_tracker = 0 # Tracks total love_score drop for max_love_score reduction
default mark_awareness = 0
default sarah_discontent = 0
default day5_choice = 0
default day6_choice = 0
default day7_choice = 0
default day8_choice = 0
default day9_choice = 0
default day10_choice = 0

init python:
    def update_love_score(amount):
        global love_score
        global max_love_score
        global love_score_tracker

        # Ensure love_score does not exceed max_love_score
        if love_score + amount > max_love_score:
            love_score = max_love_score
        else:
            love_score += amount

        # Update love_score_tracker only if love_score is decreasing
        if amount < 0:
            love_score_tracker += amount # amount is negative, so this adds to the negative total

        # Check if love_score_tracker has dropped by 2 or more
        while love_score_tracker <= -2:
            max_love_score -= 2
            love_score_tracker += 2 # Reset tracker by 2 for each 2-point drop in max_love_score
            # Ensure love_score does not exceed the new max_love_score
            if love_score > max_love_score:
                love_score = max_love_score

    def decrease_mark_awareness(amount):
        global mark_awareness
        global love_score

        # mark_awareness can only decrease
        if amount < 0:
            mark_awareness += amount
            # Each awareness drop reduces love score by 0.5
            update_love_score(-0.5)

label start:
    $ mc_name = renpy.input("What is your name?", default="Mark")
    $ m = Character(mc_name)

    # Initial scene setup, if any, before the main story begins.
    call day1