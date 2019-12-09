# -*- coding: utf-8 -*-

class Airplane:

	empty_attribute_dict = {
		"valid": False,
		"name": "",
		"manufacturer": "",
		"type": "",
		"seat_count": ""
	}
<<<<<<< HEAD
	
=======


>>>>>>> c897b671af41d53b9444e538f12beccbddfcde5f
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
		return [
			("Nafn", self.__name),
			("Framleiðandi", self.__manufacturer),
			("Tegund", self.__type),
			("Sætisfjöldi", self.__seat_count)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		return ["valid", "name", "manufacturer", "type", "seat_count"]


	def short_display(self):
		return f"Nafn: {self.__name}. Tegund: {self.__manufacturer} {self.__type}. Sætafjöldi: {self.__seat_count}."

	def name_check(name):
		if name.replace("-", "").isalpha() and len(name) == 6:
			return name
		else:
			return "error name not valid"

	def seat_count_check(seat_count):
		if seat_count.isdecimal():
			return seat_count
		else:
			return "Seat count not valid"

	def type_check(type_str):
		if type_str.replace(" ", "").isalnum():
			return type_str
		else:
			return "Type is not valid"

	def manufacturer_check(manuf_str):
		if manuf_str.replace(" ", "").isalnum():
			return manuf_str
		else:
			return "Manufacturer not valid"