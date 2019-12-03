class Rtrip:
	"""
	Model class for round trips (flight from Iceland and flight back to Iceland).
	"""

	__valid_bool = False
	__dest_str = ""
	__rtime_int = 0
	__passenger_count_int = 0
	__airplane_type = ""		# Instance of class Airplane
	__passenger_count_int = 0
	__start_time_str = ""
	__return_time_str = ""

	# Ekki alveg klár á því hvernig við útfærum þennan constructor þar sem 

	def __init__(self):
		self.__valid_bool = False
		self.__dest_str = ""
		self.__rtime_int = 0
		self.__passenger_count_int = ""  # Tvö passenger count.. Þurfum við passenger count yfir höfuð þar sem við erum með flug fram og til baka? Sitthvor farþegafjöldi og flugvélin gefur upp passenger capacity.
		self.__airplane_type = ""		# Instance of class Airplane
		self.__passenger_count_int = 0
		self.__start_time_str = ""
		self.__return_time_str = ""

	def set_valid(self):
		if self.__dest_str != "" and self.__rtime_int != 0 and self.__start_time_str != "":
			self.__valid_bool = True
			return True
		else:
			return False

	def set_dest_str(self, dest_str):
		if dest_str.replace(" ", "").isalpha():
			self.__dest_str = dest_str
			return True
		else:
			return False

	def get_dest_str(self):
		return self.__dest_str

	def set_rtime_int(self, rtime_int):  # Viljum við ekki reikna Rtrip time utfra destination og biðtíma?
		if rtime_int.isdecimal:
			self.__rtime_int = rtime_int
			return True
		else:
			return False

	def get_rtime_int(self):
		return self.__rtime_int

	def set_airplane_type(self, airplane_type_str):
		self.__airplane_type_str = airplane_type_str
		return True

	def get_airplane_type(self):
		return self.__airplane_type_str

	def set_passenger_count_int(self, passenger_count_int):
		if type(passenger_count_int) is int and passenger_count_int < self.__airplane_type.get_seat_count_int():
			self.__passenger_count_int = passenger_count_int
			return True
		else:
			return False

	def get_passenger_count_int(self):
		return self.__passenger_count_int

	def set_start_time_str(self, start_time_str):
		if start_time_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__start_time_str = start_time_str       #lika hægt að setja start time og date saman i einn datetime string, sama f. returndatetime
			return True
		else:
			return False

	def get_start_time_str(self):
		return self.__start_time_str

	def set_return_time_str(self, return_time_str):
		if return_time_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__return_time_str = return_time_str
			return True
		else:
			return False

	def get_return_time_str(self):
		return self.__return_time_str
