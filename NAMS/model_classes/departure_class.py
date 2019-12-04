from model_classes.rtrip_class import Rtrip


class Departure(Rtrip):
	def __init__(self):
		self.__dep_start_str = ""
		self.__dep_end_str = ""

	def set_start_time_int(self, start_time_int):
		if start_time_int.isdecimal():
			self.__start_time_int = start_time_int
			return True
		else:
			return False

	def get_start_time_int(self):
		return self.__start_time_int

	def set_end_time_int(self, end_time_int):
		if end_time_int.isdecimal():
			self.__end_time_int = end_time_int
			return True
		else:
			return False

	def get_end_time_int(self):
		return self.__end_time_int

	def getattributes(self):
		column_names = ["valid", "past", "direction", "flightID", "departingFrom", "arrivingAt", "departure", "arrival", "aircraft_name"]
		attributes = [
			self.__valid_bool,
			False,
			"outbound",
			10,
			self.__rtime_int,
			"KEF",
			self.__dest_str,
			self.__dep_start_str,
			self.__dep_end_str,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict

