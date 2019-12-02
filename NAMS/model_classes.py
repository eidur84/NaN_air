class Rtrip:
	"""
	Model class for round trips (flight from Iceland and flight back to Iceland).
	"""
	def __init__(self):
		self.__valid_bool = True
		self.__dest_str = ""
		self.__rtime_int = ""
		self.__passenger_count_int = ""
		self.__start_time_str = ""
		self.__return_time_str = ""
		self.__start_date_str = ""
		self.__return_date_str = ""

	def set_valid(self):
		pass  # a eftir að klára

	def set_dest_str(self, dest_str):
		if dest_str.replace(" ", "").isalpha():
			self.__dest_str = dest_str
			return True
		else:
			return False

	def get_dest_str(self):
		return self.__dest_str

	def set_rtime_int(self, rtime_int):  # Viljum við ekki reikna Rtrip time utfra destination og biðtíma?
		if rtime_int.isdecimal:
			self.__rtime_int = rtime_int
			return True
		else:
			return False

	def get_rtime_int(self):
		return self.__rtime_int

	def set_passenger_count_int(self, passenger_count_int):
		if passenger_count_int.isdecimal():				# random? og má ekki vera fleiri en sætisfjöldi flugvélarinnar
			self.__passenger_count_int = passenger_count_int
			return True
		else:
			return False

	def get_passenger_count_int(self):
		return self.__passenger_count_int

	def set_start_time_str(self, start_time_str):
		if start_time_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__start_time_str = start_time_str       #lika hægt að setja start time og date saman i eitt attribute, sama f. return
			return True
		else:
			return False

	def get_start_time_str(self):
		return self.__start_time_str

	def set_return_time_str(self, return_time_str):
		if return_time_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__return_time_str = return_time_str
			return True
		else:
			return False

	def get_return_time_str(self):
		return self.__return_time_str

	def set_start_date_str(self, start_date_str):
		if start_date_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__start_date_str = start_date_str
			return True
		else:
			return False

	def get_start_date_str(self):
		return self.__start_date_str

	def set_return_date_str(self, return_date_str):
		if return_date_str.replace(" ", "").isalpha():	 # Checka lika hvort það sé í samræmi við ISO formattið
			self.__return_date_str = return_date_str
			return True
		else:
			return False

	def get_return_date_str(self):
		return self.__return_date_str


class Destination:
	"""
	Model class for destinations.
	"""
	def __init__(self):
		self.__valid_bool = False
		self.__country_name_str = ''
		self.__city_name_str = ''
		self.__airport_name_str = ''
		self.__distance_int = 0
		self.__flight_time_int = 0
		self.__contact_name_str = ''
		self.__contact_phone_str = ''

	#def set_valid(self):
		#if self.__country_name_str.isalpha() == True.......
			#self.__valid_bool = True
		#else:
			#self.__valid_bool = False

	def get_valid(self):
		return self.__valid_bool

	def set_country_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
			self.__country_name_str = name_str
			return True
		else:
			return False

	def get_country_name(self):
		return self.__country_name_str

	def set_city_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
			self.__city_name_str = name_str
			return True
		else:
			return False

	def get_city_name(self):
		return self.__city_name_str

	def set_airport_name(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__airport_name_str = name_str
			return True
		else:
			return False

	def get_airport_name(self):
		return self.__airport_name_str

	def set_distance(self, km_count_int):
		if km_count_int.isdecimal():
			self.__distance_int = km_count_int
			return True
		else:
			return False

	def get_distance(self):
		return self.__distance_int

	def set_flight_time(self, min_count_int):
		if min_count_int.isdecimal():
			self.__flight_time_int = min_count_int
			return True
		else:
			return False

	def get_flight_time(self):
		return self.__flight_time_int

	def set_contact_name(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__contact_name_str = name_str
			return True
		else:
			return False

	def get_contact_name(self):
		return self.__contact_name_str

	def set_contact_number(self, phone_str):
		if phone_str.isalpha():
			self.__contact_phone_str = phone_str
			return True
		else:
			return False

	def get_contact_number(self):
		return self.__contact_phone_str


class Employee:
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
		self.__allowed_planes_list = []

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

	def set_ssn(self, ssn_str):  # INCOMPLETE
		if ssn_str.isdecimal():
			pass


class Crew:
	"""
	Model class containing staff members for a particular flight.
	"""

	def __init__(self):
		self.__flightID_str = ""		# vantar get/set methods
		self.__headpilot = ''
		self.__copilot = ''
		self.__headsteward = ''
		self.__otherstewards = []

	def set_headpilot(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__headpilot = name_str
			return True
		else:
			return False

	def get_headpilot(self):
		return self.__headpilot

	def set_copilot(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__copilot = name_str
			return True
		else:
			return False

	def get_copilot(self):
		return self.__copilot

	def set_headsteward(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__headsteward = name_str
			return True
		else:
			return False

	def get_headsteward(self):
		return self.__headsteward

	def set_stewards(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__otherstewards.append(name_str)
			return True
		else:
			return False


class Airplane:
	"""
	Model class for airplanes.
	"""
	def __init__(self):
		self.__seat_count_int = ""
		self.__type_str = ""
		self.__manuf_str = ""

	def set_seat_count_int(self, seat_count_int):
		if seat_count_int.isdecimal:
			self.__seat_count_int = seat_count_int
			return True
		else:
			return False

	def get_seat_count_int(self):
		return self.__seat_count_int

	def set_type_str(self, type_str):
		if type_str.replace(" ", "").isalpha():
			self.__type_str = type_str
			return True
		else:
			return False

	def get_type_str(self):
		return self.__type_str

	def set_manuf_str(self, manuf_str):
		if manuf_str.replace(" ", "").isalpha():
			self.__manuf_str = manuf_str
			return True
		else:
			return False

	def get_manuf_str(self):
		return self.__manuf_str
