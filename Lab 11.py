#----------------------------------------------------------
# Name: Aland Adili
# E-mail Address: ava6698@psu.edu
# Class: CMPSC 131 Section
# Lab #11
#----------------------------------------------------------
def linear_search(tickets, winnums):
    for i in tickets:
        if i == winnums:
            return True
    return False


tickets = [13579, 26791, 26792, 33445, 55555, 62483, 77777, 79422, 85647, 93121]
winnums = int(input("Enter this week's winning 5-digit number: "))
win = linear_search(tickets, winnums)


if win:
    print("You Won The Lottery!")
else:
    print("You did not win this week.")