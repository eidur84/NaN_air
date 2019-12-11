# -*- coding: utf-8 -*-

class RTrip:
	"""
	Class for handling connected instances of Departure and ReturnFlight.
	"""

	def __init__(self, departure, returnflight):
		self.__departure = departure
		self.__returnflight = returnflight


	def get_departure(self):
		return self.__departure

	def get_returnflight(self):
		return self.__returnflight

	def display1(self, show_manned=True):
		return self.__departure.short_display(show_manned)

	def display2(self, schedule_view=False):
		return self.__returnflight.short_display(schedule_view)

