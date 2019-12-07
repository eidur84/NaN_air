


class Destination:
	empty_attribute_dict = {
		"valid": False,
		"ID": "",
		"country": "",
		"city": "",
		"airport": "",
		"flight_time": 0,
		"distance": 0,
		"contact_name": "",
		"contact_phone": ""
	}

	def __init__(self, attribute_dict = empty_attribute_dict):
		"""
		Constructor for class. Initialize attributes with dictionary, default values are empty.
		"""

		self.__valid = attribute_dict["valid"]
		self.__id = attribute_dict["ID"]
		self.__country = attribute_dict["country"]
		self.__city = attribute_dict["city"]
		self.__airport = attribute_dict["airport"]
		self.__flight_time = attribute_dict["flight_time"]
		self.__distance = attribute_dict["distance"]
		self.__contact_name = attribute_dict["contact_name"]
		self.__contact_phone = attribute_dict["contact_phone"]

	def get_attributes(self):
		""" Returns dictionary of instances attributes."""
		attribute_dict = {
			"valid": self.__valid,
			"ID": self.__id,
			"country": self.__country,
			"city": self.__city,
			"airport": self.__airport,
			"flight_time": self.__flight_time,
			"distance": self.__distance,
			"contact_name": self.__contact_name,
			"contact_phone": self.__contact_phone
		}

		return attribute_dict

	def attribute_translation(self):
		return [
			("Auðkenni", self.__id),
			("Land", self.__country),
			("Borg", self.__city),
			("Flugvöllur", self.__airport),
			("Flugtími", self.__flight_time),
			("Fjarlægð", self.__distance),
			("Tengiliður", self.__contact_name),
			("Sími tengiliðs", self.__contact_phone)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		return ["valid", "ID", "country", "city", "airport", "flight_time", "distance", "contact_name", "contact_phone"]

	def short_display(self):
		first_half = f"{self.__id}: {self.__airport}, {self.__city}, {self.__country}. "
		second_half = f"{self.__flight_time} min. {self.__distance} km. {self.__contact_name}, {self.__contact_phone}"
		return first_half + second_half

	def __str__(self):

		first_half = f"Auðkenni: {self.__id}. Flugvöllur: {self.__airport}, {self.__city}, {self.__country}. "
		second_half = f"Flugtími: {self.__flight_time} min. "
		third_half = f"Fjarlægð: {self.__distance} km. Tengiliður: {self.__contact_name}, {self.__contact_phone}"
		return first_half + second_half + third_half