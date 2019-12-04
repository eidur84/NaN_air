
class Airplane:
	"""
	Model class for airplanes.
	"""

	def __init__(self):
		self.__PlaneName_str = ""
		self.__seat_count_int = 0
		self.__type_str = ""
		self.__manuf_str = ""
		self.__valid_bool = False


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

	def getattributes(self):
		column_names = ["airplaneID", "manufacturer", "name", "type", "seat_count", "valid"]
		attributes = [
			10,
			self.__manuf_str,
			self.__PlaneName_str,
			self.__type_str,
			self.__seat_count_int,
			self.__valid_bool,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
