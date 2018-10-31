#from passenger import Passenger 
#from driver import Driver
from trip import Trip 

class Query: 

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def trips(self):
        trips = []
        for trip in Trip.all():
            if (trip.passenger.name == self.name or trip.driver.name == self.name):
                trips.append(trip)
        return trips
    
    def trip_count(self):
        return len(self.trips())