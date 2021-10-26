# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""
class Vehicle:
    """ A class to represent an animal"""
    def __init__(self, name: str, max_speed: int, capacity: int) -> None:
        """ Vehicle

                Args:
                    name: str
                        The name of the vehicle
                    max_speed: int
                        the max speed of the vehicle
                    capacity: int
                        capacity of the vehicle
                Returns:
                    None
                """

        self.name = " "
        self.max_speed = max_speed
        self.capacity = capacity

    def vroom(self) -> None:
        """ Prints "Vroom" max_speed times"""
        for i in range(self.max_speed):
            print("Vroom")

class Bus(Vehicle):
    """Represents a bus"""

    def __init__(self, age: float) -> None:
        """ Bus
                Args:
                    age: float
                        The age of the bus rider

                Returns:
                    None
                """

        self.age = age

    def fare(self) -> None:
        if int(self.age) <= 17 or int(self.age) >= 61:
            print("You can ride for free!")
        else:
            print("The fare is $5!")

Car = Vehicle("Car", 9, 5)
Car.vroom()

Bus = Bus("60")
Bus.fare()


