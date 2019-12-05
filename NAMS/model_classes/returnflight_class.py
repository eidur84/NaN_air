<<<<<<< HEAD
<<<<<<< HEAD
class Returnflight:

	Klasabreytur

	__start_time_str = ""
	__end_time_str = ""

	# Constructor
	# Þurfum að spá í hvernig við útfærum þetta.. Þetta er auðvitað alltaf tengt departure þannig constructor er mögulega ekki nauðsynlegur
	# Jafnvel kanski óþarfa klasi?

	def __init__(self, start_time):
		self.__start_time_str = start_time
=======
class Returnflight(Rtrip):
	def __init__(self):
		self.__start_time = 0
		self.__end_time = 0
>>>>>>> 6a82a579c2d1da4198142fb7d453c8a7ce7fadc8
=======
from model_classes.rtrip_class import Rtrip


class Returnflight(Rtrip):
	def __init__(self):
		self.__ret_start_str = ""
		self.__ret_end_str = ""

	def initialize():
		pass
		#### BÚA BARA TIL DEPARTURE KLASA OG SLEPPA RTRIP? REIKNA RETURN FLIGHT UTFRA ÞVI ####
>>>>>>> 72ddcbf3d83a7d3022f0efd1f2a68223614eef12

	def set_start_time(self, number_int):
		self.__start_time += number_int

	def get_start_time(self):
		return self.__start_time

	def set_end_time(self, number_int):
		self.__end_time += number_int

	def get_end_time(self):
		return self.__end_time

	def getattributes(self):
		column_names = ["valid", "past", "direction", "flightID", "departingFrom", "arrivingAt", "departure", "arrival", "aircraft_name"]
		attributes = [
			self.__valid_bool,
			False,
			"inbound",
			100,
			self.__dest_str,
			"KEF",
			self.__ret_start_str,
			self.__ret_end_str,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
