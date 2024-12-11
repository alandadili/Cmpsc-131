class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year_model

    def get_speed(self):
        return self.speed

    def __str__(self):
        return f"Current speed: {self.speed}"

# Sample program
def main():
    # Creating a Car object
    my_car = Car(2022, "Toyota")

    # Displaying the car’s year model and make
    print(f"Year Model: {my_car.get_year()}")
    print(f"Make: {my_car.get_make()}")

    # Accelerating the car five times
    for _ in range(5):
        my_car.accelerate()
        print(my_car)

    # Braking the car five times
    for _ in range(5):
        my_car.brake()
        print(my_car)

if __name__ == "__main__":
    main()