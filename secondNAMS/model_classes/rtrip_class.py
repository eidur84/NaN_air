# -*- coding: utf-8 -*-

class RTrip:

	def __init__(self, departure, returnflight):
		self.__departure = departure
		self.__returnflight = returnflight
		self.__display1 = departure.short_display()
		self.__display2 = returnflight.short_display()


	def get_departure(self):
		return self.__departure

	def get_returnflight(self):
		return self.__returnflight

	def display1(self):
		return self.__display1

	def display2(self):
		return self.__display2

