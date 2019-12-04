class Returnflight(Rtrip):
	def __init__(self):
		self.__start_time = 0
		self.__end_time = 0

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
			10,
			self.__rtime_int,
			self.__dest_str,
			"KEF",
			self.__start_time_str,
			self.__return_time_str,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
