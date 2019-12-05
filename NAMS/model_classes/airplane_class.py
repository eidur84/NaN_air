
class Airplane:
	"""
	Model class for airplanes.
	"""

<<<<<<< HEAD
	def __init__(self, name = "", seats = 0, planetype = "", manuf = ""):
		self.__PlaneName_str = self.set_name(name)
		self.__seat_count_int = self.set_seat_count(seats)
		self.__type_str = self.set_type(planetype)
		self.__manuf_str = self.set_manuf(manuf)
		self.__valid_bool = False
=======
	def __init__(self):
		self.__valid_bool = False
		self.__PlaneName_str = ""
		self.__seat_count_int = 0
		self.__type_str = ""
		self.__manuf_str = ""
>>>>>>> 218355e866ad74d96967fcd05864d8b622323c52

	def initialize(self, attribute_dict):
		self.__PlaneName_str = attribute_dict["name"]
		self.__seat_count_int = attribute_dict["seat_count"]
		self.__type_str = attribute_dict["type"]
		self.__manuf_str = attribute_dict["manufacturer"]
		self.__valid_bool = attribute_dict["valid"]
		return self

	def set_valid(self):
		self.__valid_bool = True
		return True

	def set_name(self, name):
		if name.replace("-", "").isalpha() and len(name) == 6:
			self.__PlaneName_str = name
			return True
		else:
			return False

	def set_seat_count(self, seat_count):
		if seat_count.isdecimal:
			self.__seat_count_int = seat_count
			return True
		else:
			return False

	def get_seat_count(self):
		return self.__seat_count_int

	def set_type(self, type_str):
		if type_str.replace(" ", "").isalnum():
			self.__type_str = type_str
			return True
		else:
			return False

	def get_type(self):
		return self.__type_str

	def set_manuf(self, manuf_str):
		if manuf_str.replace(" ", "").isalnum():
			self.__manuf_str = manuf_str
			return True
		else:
			return False

	def get_manuf(self):
		return self.__manuf_str

	def getattributes(self):
		column_names = ["manufacturer", "name", "type", "seat_count", "valid"]
		attributes = [
			self.__manuf_str,
			self.__PlaneName_str,
			self.__type_str,
			self.__seat_count_int,
			self.__valid_bool,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict

	def __str__(self):
		return f"{self.__valid_bool}, {self.__manuf_str}, {self.__PlaneName_str}, {self.__type_str}, {self.__seat_count_int}"
