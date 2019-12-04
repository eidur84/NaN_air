
class Airplane:
	"""
	Model class for airplanes.
	"""

	# __valid_bool = False
	# __PlaneID_int = 0
	# __PlaneName_str = ""
	# __seat_count_int = 0
	# __type_str = ""
	# __manuf_str = ""

	def __init__(self, name, seats, planetype, manufacturer):
		self.__PlaneName_str = name
		self.__seat_count_int = seats
		self.__type_str = planetype
		self.__manuf_str = manufacturer
		self.set_valid(self)

	def set_valid(self):
		self.__valid_bool = True


	def set_name(self, name):
		if name.replace(" ", "").isalpha() and len(name) == 6:
			self.__PlaneName_str = name
			return True
		else:
			return false

	def set_seat_count(self, seat_count):
		if seat_count.isdecimal:
			self.__seat_count_int = seat_count
			return True
		else:
			return False

	def get_seat_count(self):
		return self.__seat_count_int

	def set_type(self, type_str):
		if type_str.replace(" ", "").isalpha():
			self.__type_str = type_str
			return True
		else:
			return False

	def get_type(self):
		return self.__type_str

	def set_manuf(self, manuf_str):
		if manuf_str.replace(" ", "").isalpha():
			self.__manuf_str = manuf_str
			return True
		else:
			return False

	def get_manuf(self):
		return self.__manuf_str
