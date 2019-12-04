<<<<<<< HEAD
class Departure():

	__start_time_str = ""
	__end_time_str = ""

	def __init__(self,start,end):
		self.set_start_time(start)
=======
class Departure(Rtrip):
	def __init__(self):
		self.__start_time_int = 0
		self.__end_time_int = 0
>>>>>>> 6a82a579c2d1da4198142fb7d453c8a7ce7fadc8
	
	def set_start_time(self, start_time)
		if start_time.isdecimal():
			self.__start_time_str = start_time
			return True
		else:
			return False
	
	def get_start_time(self):
		return self.__start_time_str

	# Sennilega óþarft fall þar sem end time ákvarðast af destination.. Þarf að útfæra automatic end time fall út frá destination
	
	def set_end_time(self, end_time_int):
		if end_time_int.isdecimal():
			self.__end_time_int = end_time_int
			return True
		else:
			return False

<<<<<<< HEAD
	def get_end_time(self):
		return self.__end_time_int
=======
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
			self.__start_time_str,
			self.__return_time_str,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
		
>>>>>>> 6a82a579c2d1da4198142fb7d453c8a7ce7fadc8
