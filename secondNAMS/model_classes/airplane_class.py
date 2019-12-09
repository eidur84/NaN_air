# -*- coding: utf-8 -*-

class Airplane:

	empty_attribute_dict = {
		"valid": False,
		"name": "",
		"manufacturer": "",
		"type": "",
		"seat_count": ""
	}


	def __init__(self, attribute_dict = empty_attribute_dict):

		self.__valid = attribute_dict["valid"]
		self.__name = Airplane.name_check(attribute_dict["name"])
		self.__manufacturer = Airplane.manufacturer_check(attribute_dict["manufacturer"])
		self.__type = Airplane.type_check(attribute_dict["type"])
		self.__seat_count = Airplane.seat_count_check(attribute_dict["seat_count"])


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

	def attribute_translation(self):
		""" Returns attribute names in Icelandic."""
		return [
			("Nafn", self.__name),
			("Framleiðandi", self.__manufacturer),
			("Tegund", self.__type),
			("Sætisfjöldi", self.__seat_count)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		""" Returns list of keys to attribute dict"""
		return ["valid", "name", "manufacturer", "type", "seat_count"]


	#--------------------- Basic check functions
	def name_check(name):
		if name.replace("-", "").isalpha() and len(name) == 6 or name == "":
			return name
		else:
			return "Villa"

	def seat_count_check(seat_count):
		if seat_count.isdecimal() or seat_count == "":
			return seat_count
		else:
			return "Villa"

	def type_check(type_str):
		if type_str.replace(" ", "").isalnum() or type_str == "":
			return type_str
		else:
			return "Villa"

	def manufacturer_check(manuf_str):
		if manuf_str.replace(" ", "").isalnum() or manuf_str == "":
			return manuf_str
		else:
			return "Villa"
	#--------------------- Basic check functions end


	def short_display(self):
		return f"Nafn: {self.__name}. Tegund: {self.__manufacturer} {self.__type}. Sætafjöldi: {self.__seat_count}."




