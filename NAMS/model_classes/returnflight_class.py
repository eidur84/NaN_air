class Returnflight:
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
