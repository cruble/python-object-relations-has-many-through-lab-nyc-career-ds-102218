from query import Query

class Passenger:

    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.add_passenger(self)

    @property
    def name(self):
    	return self._name
    
    @name.setter
    def name(self, name):
    	self._name = name 

    @property
    def age(self):
    	return self._age
    
    @age.setter
    def age(self, age):
    	self._age = age

    @classmethod
    def add_passenger(cls, passenger):
    	cls._all.append(passenger)

    def trips(self):
        return Query(self.name).trips()

    def drivers(self):
        return list(map(lambda trip: trip.driver, self.trips()))

    def trip_count(self):
        return Query(self.name).trip_count()


