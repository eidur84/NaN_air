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
		self.__license = Employee.license_check(attribute_dict["license"])

	def name_check(name):
		if name == "":
			return name
		elif name.replace(" ", "").isalpha():
			return name
		else:
			return "Nafn er ekki viðurkennt"

	def ssn_check(ssn):
		if ssn.isdecimal() and len(ssn) == 10:

			if int(ssn[2:4]) <= 12:

				if ssn[2:4] == "02":  # February

					if int(ssn[:2]) <= 29:
						return ssn

				elif ssn[2:4] in ["04", "06", "09", "11"]:

					if int(ssn[:2]) <= 30:
						return ssn

				else:
					if int(ssn[:2]) <= 31:
						return ssn
		return "Kennitala er ekki viðurkennd"

	def job_check(job):
		if job in ["Flugmaður", "Flugþjónn", ""]:
			return job
		elif job == "ERROR":
			return "Starfsheiti er ekki þekkt"
		else:
			return "Starfsheiti er ekki þekkt"

	def home_check(home):
		if home == "":
			return home
		elif home.replace(" ", "").isalpha():
			return home
		else:
			return "Heimili er ekki þekkt"

	def landline_check(landline):
		if landline == "":
			return landline
		elif landline.isnumeric():
			return landline
		else:
			return "Símanúmer má aðeins innihalda tölustafi"

	def gsm_check(gsm):
		if gsm == "":
			return gsm
		elif gsm.isnumeric():
			return gsm
		else:
			return"Símanúmer má aðeins innihalda tölustafi"

	def email_check(email):
		if email == "":
			return email
		elif "@" in email and "." in email and len(email.replace("@", "").replace(".", "")) >= 4:
			return email
		else:
			"Tölvupóstfang er ekki þekkt"

	def license_check(license):
		if license == "":
			return license
		elif len(license) >= 4:
			return license
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
		first_half = "{}, {}. {}, {}. {}, {}.".format(self.__ssn, self.__name, self.__job, self.__license, self.__landline, self.__gsm)
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
