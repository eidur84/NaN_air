
class Airplane:
	"""
	Model class for airplanes.
	"""
	def __init__(self):
		self.__seat_count_int = 0
		self.__type_str = ""
		self.__manuf_str = ""

	def set_seat_count_int(self, seat_count_int):
		if seat_count_int.isdecimal:
			self.__seat_count_int = seat_count_int
			return True
		else:
			return False

	def get_seat_count_int(self):
		return self.__seat_count_int

	def set_type_str(self, type_str):
		if type_str.replace(" ", "").isalpha():
			self.__type_str = type_str
			return True
		else:
			return False

	def get_type_str(self):
		return self.__type_str

	def set_manuf_str(self, manuf_str):
		if manuf_str.replace(" ", "").isalpha():
			self.__manuf_str = manuf_str
			return True
		else:
			return False

	def get_manuf_str(self):
		return self.__manuf_str
