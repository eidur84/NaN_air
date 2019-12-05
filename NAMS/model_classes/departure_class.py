
from model_classes.rtrip_class import Rtrip


class Departure:

	def __init__(self):

		self.__valid_bool = False
		self.__past = False
		self.__dest_str = ""
		self.__airplane_name = ""

		self.__dep_start_str = ""
		self.__dep_end_str = ""

	def set_valid(self):
		self.__valid_bool = True
		return True


	def set_destination(self, dest_str):
		if dest_str.isalpha():
			self.__dest_str = dest_str
			return True
		else:
			return False

	def get_destination(self):
		return self.__dest_str

	def set_departure(self, departure):
		if departure.replace("-", "").replace(":", "").isalnum():
			self.__dep_start_str = departure
			return True
		else:
			return False

	def get_departure(self):
		return self.__dep_start_str

	def calc_arrival(self, arrival):
		pass
	## VANTAR CALL I DB READ() FINNA TIMA TIL AFANGASTAÐAR


	def get_arrival(self):
		return self.__dep_end_str

	def set_airplane(self, airplane_str):
		if airplane_str.replace("-", "").isalpha():
			self.__airplane_name = airplane_str
			return True
		else:
			return False

	def get_airplane(self):
		return self.__airplane_name

	def getattributes(self):
		column_names = [
			"valid",
			"past",
			"direction",
			"flightID",
			"departingFrom",
			"arrivingAt",
			"departure",
			"arrival",
			"aircraft_name"
		]

		attributes = [
			self.__valid_bool,
			False,
			"outbound",
			10,
			"KEF",
			self.__dest_str,
			self.__dep_start_str,
			self.__dep_end_str,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict

