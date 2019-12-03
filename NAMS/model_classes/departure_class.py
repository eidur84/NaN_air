class Departure():

	__start_time_str = ""
	__end_time_str = ""

	def __init__(self,start,end):
		self.set_start_time(start)
	
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

	def get_end_time(self):
		return self.__end_time_int