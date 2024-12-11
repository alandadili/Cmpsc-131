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

dice_roll=Die()

for i in range(5):
    print(dice_roll.roll)
    print("Roll {}: {}".format( + 1, dice_roll.get_value()))
if __name__ == "__main__":
    main()