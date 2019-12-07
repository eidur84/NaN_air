

class Airplane:

	empty_attribute_dict = {
		"valid": False,
		"name": "",
		"manufacturer": "",
		"type": "",
		"seat_count": 0
	}

	def __init__(self, attribute_dict = empty_attribute_dict):

		self.__valid = attribute_dict["valid"]
		self.__name = attribute_dict["name"]
		self.__manufacturer = attribute_dict["manufacturer"]
		self.__type = attribute_dict["type"]
		self.__seat_count = attribute_dict["seat_count"]

	def get_attributes(self):
		""" Returns dictionary of instances attributes."""
		attribute_dict = {
			"valid": self.__valid,
			"name": self.__name,
			"manufacturer": self.__manufacturer,
			"type": self.__type,
			"seat_count": self.__seat_count
		}

		return attribute_dict

	def __str__(self):
		return f"Nafn: {self.__name}. Tegund: {self.__type}. Framleiðandi: {self.__manufacturer}. Sætafjöldi: {self.__seat_count}."
