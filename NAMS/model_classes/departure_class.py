'''
<<<<<<< HEAD
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
=======
'''

class Departure:

	def __init__(self):

		self.__valid_bool = False
		self.__past = False
		self.__dest_str = ""
		self.__airplane_name = ""

		self.__dep_departure = ""
		self.__dep_arrival = ""


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
			self.__dep_departure = departure
			return True
		else:
			return False

	def get_departure(self):
		return self.__dep_departure



	#def set_arrival(self, arrival):
	#	self.__dep_arrival =



	def get_arrival(self):
		return self.__dep_arrival



	def set_airplane(self, airplane_str):
		if airplane_str.replace("-", "").isalpha():
			self.__airplane_name = airplane_str
			return True
		else:
			return False


	def get_end_time(self):
		return self.__end_time_int

	def get_end_time_int(self):
		return self.__end_time_int

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
			100,
			"KEF",
			self.__dest_str,
			self.__dep_departure,
			self.__dep_arrival,
			self.__airplane_type,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict


