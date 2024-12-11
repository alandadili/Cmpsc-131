#----------------------------------------------------------
# Name: Aland Adili
# E-mail Address: ava6698@psu.edu
# Class: CMPSC 131 Section
# Lab #13
#----------------------------------------------------------

import random

class Die:
    def __init__(self):
        self.die_value = 1

    def roll(self):
        self.die_value = random.randint(1, 6)

    def get_value(self):
        return self.die_value


def main():

    dice_roll = Die()


    for i in range(5):
        dice_roll.roll()
        print("Roll",i + 1,":", dice_roll.get_value())

main()