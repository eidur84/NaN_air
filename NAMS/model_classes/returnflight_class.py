class Returnflight:

	Klasabreytur

	__start_time_str = ""
	__end_time_str = ""

	# Constructor
	# Þurfum að spá í hvernig við útfærum þetta.. Þetta er auðvitað alltaf tengt departure þannig constructor er mögulega ekki nauðsynlegur
	# Jafnvel kanski óþarfa klasi?

	def __init__(self, start_time):
		self.__start_time_str = start_time

	def set_start_time(self, number_int):
		self.__start_time += number_int

	def get_start_time(self):
		return self.__start_time

	def set_end_time(self, number_int):
		self.__end_time += number_int

	def get_end_time(self):
		return self.__end_time
