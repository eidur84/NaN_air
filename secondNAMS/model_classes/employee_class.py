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
		self.__ssn = ssn_check(attribute_dict["ssn"])
		self.__name = name_check(attribute_dict["name"])
		self.__job = job_check(attribute_dict["job"])
		self.__home = home_check(attribute_dict["home"])
		self.__landline = landline_check(attribute_dict["landline"])
		self.__gsm = gsm_check(attribute_dict["gsm"])
		self.__email = email_check(attribute_dict["email"])
		self.__license = license_check(attribute_dict["license"])

	def name_check(self):
		if self.__name == "":
			return self.__name
		elif self.__name.replace(" ", "").isalpha():
			return self.__name
		else:
			return "Nafn er ekki viðurkennt"

	def ssn_check(self):
		ssn_str = self.__ssn
		if ssn_str.isdecimal() and len(ssn_str) == 10:

			if int(ssn_str[2:4]) <= 12:

				if ssn_str[2:4] == "02":  # February

					if int(ssn_str[:2]) <= 29:
						return self.__ssn

				elif ssn_str[2:4] in ["04", "06", "09", "11"]:

					if int(ssn_str[:2]) <= 30:
						return self.__ssn

				else:
					if int(ssn_str[:2]) <= 31:
						return self.__ssn
		return "Kennitala er ekki viðurkennd"

	def job_check(self):
		if self.__job in ["Flugmaður", "Flugþjónn", ""]:
			return self.__job
		elif self.__job == "ERROR":
			return "Starfsheiti er ekki þekkt"
		else:
			return "Starfsheiti er ekki þekkt"

	def home_check(self):
		if self.__home == "":
			return self.__home
		elif self.__home.replace(" ", "").isalpha():
			return self.__home
		else:
			return "Heimili er ekki þekkt"

	def landline_check(self):
		if self.__landline == "":
			return self.__landline
		try:
			int(self.__landline)
		except ValueError:
			return "Símanúmer má aðeins innihalda tölustafi"

	def gsm_check(self):
		if self.__gsm == "":
			return self.__gsm
		elif self.__gsm.isnumeric():
			return self.__gsm
		else:
			return"Símanúmer má aðeins innihalda tölustafi"

	def email_check(self):
		if self.__email == "":
			return self.__email
		elif "@" in self.__email and "." in self.__email and len(self.__email.replace("@", "").replace(".", "")) >= 4:
			return self.__email
		else:
			"Tölvupóstfang er ekki þekkt"

	def license_check(self):
		if self.__license == "":
			return self.__license
		elif len(self.__license) >= 4:
			return self.__license
		else:
			"Flugvélaleyfi er ekki þekkt"

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
		#first_half = f"{self.__ssn}, {self.__name}. {self.__job}, {self.__license}. {self.__landline}, {self.__gsm}."
		first_half = "{},{}.{},{}.{},{}.".format(self.__ssn, self.__name, self.__job, self.__license, self.__landline, self.__gsm)
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
