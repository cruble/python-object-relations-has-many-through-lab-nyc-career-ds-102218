#from passenger import Passenger 
#from driver import Driver
from trip import Trip 

class Query: 

	def __init__(self, person):
		self._person = person

	@property
	def person(self):
		return self._person

	def query_passengers(self):
		driver = self.person
		passengers = []
		for trip in Trip.all():
			if (trip.driver == driver):
				passengers.append(trip.passenger)
		return passengers


	def query_drivers(self):
		passenger = self.person
		drivers = []
		for trip in Trip.all():
			if (trip.passenger == passenger):
				drivers.append(trip.driver)
		return drivers

	
	def query_trips(self):
		trips = []
		for trip in Trip.all():
			if (trip.passenger = self.person or trip.driver == self.person):
				trips.append(self.person)
		return trips





	# @staticmethod
	# def trips(person, trips):
	# 	person_trips = list(filter(lambda trip: trip.passenger == person or trip.driver == person, trips))
	# 	return person_trips

	# @staticmethod
	# def trip_count(person, trips):

	# Drivers.all()
	# Passengers.all
	# # 	

	# def __init__(self, name, l):
	# 	self._name = name
	# 	self._l = l 

	# def query_by_name(self):
	# 	return [x for x in self._l if x.name == self._name]

