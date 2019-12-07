class Destination:
	"""
	Model class for destinations.
	"""

	def __init__(self):
		self.__country_name_str = ""
		self.__city_name_str = ""
		self.__ID_str = ""
		self.__airport_name_str = ""
		self.__distance_int = 0
		self.__flight_time_int = 0
		self.__contact_name_str = ""
		self.__contact_phone_str = ""
		self.__valid_bool = False

	def initialize(self, attribute_dict):
		self.__country_name_str = attribute_dict["country"]
		self.__city_name_str = attribute_dict["city"]
		self.__ID_str = attribute_dict["ID"]
		self.__airport_name_str = attribute_dict["airport"]
		self.__distance_int = int(attribute_dict["distance"])
		self.__flight_time_int = int(attribute_dict["flight_time"])
		self.__contact_name_str = attribute_dict["contact_name"]
		self.__contact_phone_str = attribute_dict["contact_phone"]
		self.__valid_bool = attribute_dict["valid"]
		return self

	def set_valid(self):
		self.__valid_bool = True
		return True

	def get_valid(self):
		return self.__valid_bool

	def set_country_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
			self.__country_name_str = name_str
			return True
		else:
			return False

	def get_country_name(self):
		return self.__country_name_str

	def set_city_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
			self.__city_name_str = name_str
			return True
		else:
			return False

	def get_city_name(self):
		return self.__city_name_str

	def set_ID(self, id_str):
		if len(id_str) == 3 and id_str.isalpha():
			self.__ID_str = id_str
			return True
		else:
			return False

	def get_ID(self):
		return self.__ID_str

	def set_airport_name(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__airport_name_str = name_str
			return True
		else:
			return False

	def get_airport_name(self):
		return self.__airport_name_str

	def set_distance(self, km_count_int):
		if km_count_int.isdecimal():
			self.__distance_int = km_count_int
			return True
		else:
			return False

	def get_distance(self):
		return self.__distance_int

	def set_flight_time(self, min_count_int):
		if min_count_int.isdecimal():
			self.__flight_time_int = min_count_int
			return True
		else:
			return False

	def get_flight_time(self):
		return self.__flight_time_int

	def set_contact_name(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__contact_name_str = name_str
			return True
		else:
			return False

	def get_contact_name(self):
		return self.__contact_name_str

	def set_contact_number(self, phone_str):
		if phone_str.isalpha():
			self.__contact_phone_str = phone_str
			return True
		else:
			return False

	def get_contact_number(self):
		return self.__contact_phone_str

	def getattributes(self):
		column_names = ["valid", "ID", "country", "city", "airport", "flight_time", "distance", "contact_name", "contact_phone"]
		attributes = [
			self.__valid_bool,
			self.__ID_str,
			self.__country_name_str,
			self.__city_name_str,
			self.__airport_name_str,
			self.__flight_time_int,
			self.__distance_int,
			self.__contact_name_str,
			self.__contact_phone_str,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict

	def __str__(self):
		a = f"{self.__valid_bool}, {self.__ID_str}, {self.__country_name_str}, {self.__city_name_str}, {self.__airport_name_str}, "
		b = f"{self.__flight_time_int}, {self.__distance_int}, {self.__contact_name_str}, {self.__contact_phone_str}"
		return a + b


