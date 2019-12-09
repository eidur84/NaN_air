# -*- coding: utf-8 -*-


class Employee:
	empty_attribute_dict = {
		"valid": False,
		"ssn": "",
		"name": "",
		"job": "",
		"home": "",
		"landline": "",
		"gsm": "",
		"email": "",
		"license": ""
	}

	def __init__(self, attribute_dict = empty_attribute_dict):

		self.__valid = attribute_dict["valid"]
		self.__ssn = attribute_dict["ssn"]
		self.__name = attribute_dict["name"]
		self.__job = attribute_dict["job"]
		if self.__job not in ["Flugmaður", "Flugþjónn", ""]:
			self.__job = "ERROR"
		self.__home = attribute_dict["home"]
		self.__landline = attribute_dict["landline"]
		self.__gsm = attribute_dict["gsm"]
		self.__email = attribute_dict["email"]
		self.__license = attribute_dict["license"]

	def name_check(self,name):
		if name == "":
			return name
		elif name.remove(" ","").isalpha():
			return name
		else:
			return "Nafn er ekki viðurkennt"

	def get_attributes(self):
		""" Returns dictionary of instances attributes."""
		attribute_dict = {
			"valid": self.__valid,
			"ssn": self.__ssn,
			"name": self.__name,
			"job": self.__job,
			"home": self.__home,
			"landline": self.__landline,
			"gsm": self.__gsm,
			"email": self.__email,
			"license": self.__license
		}

		return attribute_dict


	def attribute_translation(self):
		return [
			("Kennitala", self.__ssn),
			("Nafn", self.__name),
			("Starf", self.__job),
			("Heimilisfang", self.__home),
			("Heimasími", self.__landline),
			("GSM sími", self.__gsm),
			("Tölvupóstur", self.__email),
			("Leyfi", self.__license)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		return ["valid", "ssn", "name", "job", "home", "landline", "gsm", "email", "license"]

	def short_display(self):
		first_half = f"{self.__ssn}, {self.__name}. {self.__job}, {self.__license}. {self.__landline}, {self.__gsm}."
		return first_half

	def __str__(self):

		first_half = f"{self.__ssn}, {self.__name}. Starf: {self.__job}. Leyfi: {self.__license}. "
		if self.__landline == "":
			second_half = f"Farsími: {self.__gsm}. Tölvupóstur: {self.__email}"
		elif self.__gsm == "":
			second_half = f"Heimasími: {self.__landline}. Tölvupóstur: {self.__email}"
		else:
			second_half = f"Símanúmer: {self.__landline}, {self.__gsm}. Tölvupóstur: {self.__email}"
		return first_half + second_half
