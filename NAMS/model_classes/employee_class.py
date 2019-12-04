
class Employee:
<<<<<<< HEAD
    """
    Model class for employees.
    """

    # Klasabreytur

    __valid_bool = False
    __name_str = ""
    __ssn_str = ""
    __address_str = ""
    __landline_str = ""
    __gsm_str = ""
    __email_str = ""
    __job_str = ""
    __allowed_planes_list = []


    #Constructor
    #Erum við ekki að vinna með eina leyfilega flugvél??

    def __init__(self):
        self.__valid_bool = False
        self.__name_str = ""
        self.__ssn_str = ""
        self.__address_str = ""
        self.__landline_str = ""
        self.__gsm_str = ""
        self.__email_str = ""
        self.__job_str = ""
        self.__allowed_planes_list = []

    def set_valid(self):
        pass

    def set_name(self, name):
        if name.replace(" ", "").isalpha() and len(name) < 60:
            self.__name_str = name
            return True
        else:
            return False

    def get_name(self):
        return self.__name_str

    # Þarf að setja inn löglega kennitölu

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

    def set_address(self, address):
        if len(address) < 60:
            self.__address_str = address
            return True
        else:
            return False

    def get_address(self):
        return self.__address_str

    def set_landline(self, landline:
        if landline.isdecimal():
            self.__landline_str = landline
            return True
        else:
            return False

    def get_landline(self):
        return self.__landline_str

    def set_gsm(self, gsm):
        if gsm.isdecimal():
            self.__gsm_str = gsm
            return True
        else:
            return False

    def get_gsm(self):
        return self.__gsm_str

    # Þarf mögulega að útfæra nákvæmari test á emailið

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

    def set_allowed_planes(self, airplane_type):
        # IMPLEMENT CHECK
        self.__allowed_planes_list.append(airplane_type)
        return True

    def get_allowed_planes(self):
        return self.__allowed_planes_list

=======
	"""
	Model class for employees.
	"""
	def __init__(self):
		self.__valid_bool = False
		self.__name_str = ""
		self.__ssn_str = ""
		self.__address_str = ""
		self.__landline_str = ""
		self.__gsm_str = ""
		self.__email_str = ""
		self.__job_str = ""
		self.__allowed_plane_str = ""

	def set_valid(self):
		pass

	def set_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) < 60:
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

	def set_allowed_planes(self, airplane_type):
		# IMPLEMENT CHECK
		self.__allowed_plane_str = airplane_type
		return True

	def get_allowed_planes(self):
		return self.__allowed_plane_str

	def getattributes(self):
		column_names = ["valid", "ssn", "staffID", "name", "job", "home", "landline", "gsm", "email", "license"]
		attributes = [
			self.__valid_bool,
			self.__ssn_str,
			10,
			self.__name_str,
			self.__job_str,
			self.__address_str,
			self.__landline_str,
			self.__gsm_str,
			self.__email_str,
			self.__allowed_plane_str,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
>>>>>>> 6a82a579c2d1da4198142fb7d453c8a7ce7fadc8
