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
		self.__ssn = Employee.ssn_check(attribute_dict["ssn"])
		self.__name = Employee.name_check(attribute_dict["name"])
		self.__job = Employee.job_check(attribute_dict["job"])
		self.__home = Employee.home_check(attribute_dict["home"])
		self.__landline = Employee.landline_check(attribute_dict["landline"])
		self.__gsm = Employee.gsm_check(attribute_dict["gsm"])
		self.__email = Employee.email_check(attribute_dict["email"])
		self.__license = attribute_dict["license"]


	#--------------------- Basic check functions
	def name_check(name):
		if name == "" or name.replace(" ", "").isalpha():
			return name.title()
		else:
			return "Villa"

	def ssn_check(ssn):
		if ssn.isdecimal() and len(ssn) == 10:

			if int(ssn[2:4]) <= 12:

				if ssn[2:4] == "02":  # February

					if int(ssn[:2]) <= 29:
						return ssn

				elif ssn[2:4] in ["04", "06", "09", "11"]: # April, June, Sept., Nov.

					if int(ssn[:2]) <= 30:
						return ssn

				else:
					if int(ssn[:2]) <= 31:
						return ssn
		elif ssn == "":
			return ssn

		return "Villa"

	def job_check(job):
		if job.title() in ["Flugmaður", "Flugþjónn", ""]:
			return job.title()
		else:
			return "Villa"

	def home_check(home):
		if home == "" or  len(home) > 4:
			return home.title()
		else:
			return "Villa"

	def landline_check(landline):
		if landline == "" or landline.isnumeric() and len(landline) >= 7:
			return landline
		else:
			return "Villa"

	def gsm_check(gsm):
		if gsm == "" or gsm.isnumeric() and len(gsm) == 7:
			return gsm
		else:
			return "Villa"

	def email_check(email):
		if email == "":
			return email
		elif "@" in email and "." in email and len(email) >= 5:
			return email
		else:
			return "Villa"

	#--------------------- Basic check functions end

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
		""" Returns names of attributes in Icelandic."""
		return [
			("Kennitala", self.__ssn),
			("Nafn", self.__name),
			("Starf", self.__job),
			("Heimilisfang", self.__home),
			("Heimasími", self.__landline),
			("GSM sími", self.__gsm),
			("Tölvupóstur", self.__email),
			("Flugvélaleyfi", self.__license)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		""" Returns list of keys in attribute dict"""
		return ["valid", "ssn", "name", "job", "home", "landline", "gsm", "email", "license"]

	def short_display(self):
		first_half = f"{self.__ssn}, {self.__name}. {self.__job}. Leyfi: {self.__license}. {self.__email}. {self.__landline}, {self.__gsm}."
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
