#Write a class named Car that has the following data attributes:
#make, year and speed.
#The Car class should have an _ _init_ _ method that accepts the car’s year and make as arguments. These values should be assigned to the object’s year and make data attributes. It should also assign 0 to the speed data attribute.
#Have your class contain the following methods:
#accelerate(self): method should add 5 to the speed data attribute each time it is called.
#brake(self): method should subtract 5 from the speed data attribute each time it is called.
#get_speed(self) method should return the current speed.
#Have your program designed such that is creates a Car object then calls the accelerate method five times.
#After each call to the accelerate method, get the current speed of the car and display it.
#Then call the brake method five times.
#After each call to the brake method, get the current speed of the car and display it.

#Define a class named Car:
class Car:
    def __init__(self, make, year, speed):
        self.speed = 0
        self.make = make
        self.year = year

    def accelerate(self):
        self.speed += 5

    def breake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

#Main function to call all functions in this python script:
def main():
    car = Car("Toyota", 2020, 0)
    for i in range(5):
        car.accelerate()
        print("The current speed is:", car.get_speed())

    for i in range(5):
        car.breake()
        print("The car breakes and the current speed is:", car.get_speed())

#Call all functions in this python script:
main()
