# remeber to import the Trip class here
from query import Query

class Driver:

    _all = []

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style
        self.add_driver(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def driving_style(self):
        return self._driving_style
    
    @driving_style.setter
    def driving_style(self, driving_style):
        self._driving_style = driving_style

    @classmethod
    def add_driver(cls, driver):
        cls._all.append(driver)
        
    def trips(self):
        return Query(self.name).trips()
         

    def passengers(self):
        return list(map(lambda trip: trip.passenger, self.trips()))

    def trip_count(self):
         return Query(self.name).trip_count()