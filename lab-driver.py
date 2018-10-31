from driver import Driver
from passenger import Passenger
from trip import Trip


daniel = Driver("Daniel", "fast and furious")
alice = Driver("Alice", "faster and furiouser")
jeff = Driver("Jeff", "defensive")

jake = Passenger("Jake", 29)
anna = Passenger("Anna", 25)
katie = Passenger("Katie", 20)


trip_one = Trip(daniel, jake)
trip_two = Trip(alice, anna)
trip_three = Trip(jeff, katie)
trip_four = Trip(daniel, anna)