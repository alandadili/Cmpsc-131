#----------------------------------------------------------
# Name: Aland Adili
# E-mail Address: ava6998@psu.edu
# Class: CMPSC 131 Section
# Homework 8
# Due Dec 8
# Brief Project Description
#----------------------------------------------------------
class Car:
    def __init__(self, year_model, make):   #the car characteristics
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):   #sets accelerate to add and save +5
        self.speed += 5

    def brake(self):    #sets brake to subtract and save -5
        self.speed -= 5


    def get_make(self): #type of car
        return self.make

    def get_year(self): #year of car
        return self.year_model

    def get_speed(self):    #obtains car speed
        return self.speed

    def __str__(self):  #converts to string
        return f"Current speed: {self.speed}"

def main():
    new_car = Car(2020, "Honda Acord")
    print("Car info:")
    print("Make:", new_car.get_make())
    print("Year:", new_car.get_year())
    print("car is accelerating:")

    for i in range(5):  #loop that runs 5 times that increases the speed by 5
        new_car.accelerate()
        print(new_car)
    print("")
    print("car is braking:")
    for i in range(5):  #loop that runs 5 times that decreases the speed by 5
        new_car.brake()
        print(new_car)

main()  #runs program
