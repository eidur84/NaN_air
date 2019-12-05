
class Employee:
	"""
	Model class for employees.
	"""
	def __init__(self, name = "", ssn = "", address = "", landline = "", gsm = "", email = "", job = "", allowed = ""):
		self.__valid_bool = False
<<<<<<< HEAD
		self.__name_str = self.set_name(name)
		self.__ssn_str = self.set_ssn(ssn)
		self.__address_str = self.set_address(address)
		self.__landline_str = self.set_landline(landline)
		self.__gsm_str = self.set_gsm(gsm)
		self.__email_str = self.set_email(email)
		self.__job_str = self.set_job(job)
		self.__allowed_plane_str = self.set_allowed_plane
=======
		self.__name_str = ""
		self.__ssn_str = ""
		self.__address_str = ""
		self.__landline_str = ""
		self.__gsm_str = ""
		self.__email_str = ""
		self.__job_str = ""
		self.__license_str = ""

	def initialize(self, attribute_dict):
		self.__valid_bool = attribute_dict["valid"]
		self.__name_str = attribute_dict["name"]
		self.__ssn_str = attribute_dict["ssn"]
		self.__address_str = attribute_dict["home"]
		self.__landline_str = attribute_dict["landline"]
		self.__gsm_str = attribute_dict["gsm"]
		self.__email_str = attribute_dict["email"]
		self.__job_str = attribute_dict["job"]
		self.__license_str = attribute_dict["license"]
		return self

>>>>>>> 218355e866ad74d96967fcd05864d8b622323c52

	def set_valid(self):
		self.__valid_bool = True
		return True

	def set_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) < 60 and len(name_str) > 0:
			self.__name_str = name_str
			return True
		else:
			return False

	def get_name(self):
		return self.__name_str

	def set_ssn(self, ssn_str):  # INCOMPLETE CHECKS~~~~~~~~~~~~~~
		if ssn_str.isdecimal(): 
			if int(ssn_str[2:4]) <= 12:
				if ssn_str[2:4] == "02":  # February
					if int(ssn_str[:2]) <= 29:
						self.__ssn_str = ssn_str
						return True

				elif ssn_str[2:4] in ["04", "06", "09", "11"]:

					if int(ssn_str[:2]) <= 30:
						self.__ssn_str = ssn_str
						return True

				else:
					if int(ssn_str[:2]) <= 31:
						self.__ssn_str = ssn_str
						return True
		return False

	def get_ssn(self):
		return self.__ssn_str

	def set_address(self, address_str):
		if len(address_str) < 60:
			self.__address_str = address_str
			return True
		else:
			return False

	def get_address(self):
		return self.__address_str

	def set_landline(self, landline_str):
		if landline_str.isdecimal():
			self.__landline_str = landline_str
			return True
		else:
			return False

	def get_landline(self):
		return self.__landline_str

	def set_gsm(self, gsm_str):
		if gsm_str.isdecimal():
			self.__gsm_str = gsm_str
			return True
		else:
			return False

	def get_gsm(self):
		return self.__gsm_str

	def set_email(self, email_str):
		if "@" in email_str and "." in email_str:
			if email_str.replace("@", "").replace(".", "").isalpha():
				self.__email_str = email_str
				return True

		return False

	def get_email(self):
		return self.__email_str

	def set_job(self, job_str):
		if job_str.isalpha():
			self.__job_str = job_str
			return True
		else:
			return False

	def get_job(self):
		return self.__job_str

<<<<<<< HEAD
	def set_allowed_plane(self, airplane_type):
=======
	def set_license(self, airplane_type):
>>>>>>> 218355e866ad74d96967fcd05864d8b622323c52
		# IMPLEMENT CHECK
		self.__license_str = airplane_type
		return True

	def get_license(self):
		return self.__license_str

	def getattributes(self):
		column_names = ["valid", "ssn", "name", "job", "home", "landline", "gsm", "email", "license"]
		attributes = [
			self.__valid_bool,
			self.__ssn_str,
			self.__name_str,
			self.__job_str,
			self.__address_str,
			self.__landline_str,
			self.__gsm_str,
			self.__email_str,
			self.__license_str,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict

		def __str__(self):
			a = f"{self.__valid_bool}, {self.__ssn_str}, {self.__name_str}, {self.__job_str}, "
			b = f"{self.__address_str}, {self.__landline_str}, {self.__gsm_str}, {self.__license_str}"
			return a+b



