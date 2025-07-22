from random import randint
from prac_09.car import Car
class UnreliableCar(Car):
    """A derived version of Car."""
    def __init__(self, name, fuel, reliability:float):
        """Initialize UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car when it's reliable."""
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return super().drive(0)




