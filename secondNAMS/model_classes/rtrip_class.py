# -*- coding: utf-8 -*-

class RTrip:

	def __init__(self, departure, returnflight):
		self.__display1 = departure.short_display()
		self.__display2 = returnflight.short_display()

	def display1(self):
		return self.__display1

	def display2(self):
		return self.__display2

