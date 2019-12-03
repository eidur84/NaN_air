class Departure():
	def __init__(self):
		self.__start_time_int = 0
		self.__end_time_int = 0
	
	def set_start_time_int(self, start_time_int)
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