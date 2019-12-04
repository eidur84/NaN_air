class Destination:
<<<<<<< HEAD
    """
    Model class for destinations.
    """

    # Klasabreytur

    __valid_bool = False
    __country_name_str = ''
    __city_name_str = ''
    __airport_name_str = ''
    __distance_int = 0
    __flight_time_int = 0
    __contact_name_str = ''
    __contact_phone_str = ''

    # Constructor

    def __init__(self, country, city, airport, distance, flight_time, contact_name, contact_phone):
        self.__country_name_str = set_country
        self.__city_name_str = city
        self.__airport_name_str = airport
        self.__distance_int = distance
        self.__flight_time_int = flight_time
        self.__contact_name_str = contact_name
        self.__contact_phone_str = contact_phone
        self.set_valid(self)

    # Tjekk hvort öll helstu attribute seu sett og innan lengar-/staerdartakmarkana áður en þau eru acceptuð inn í database

    def set_valid(self):
        if self.__country_name_str.isalpha() == True and len(country_name_str) <= 60 and len(country_name_str) > 0 \
		and self.__city_name_str.isalpha() == True and len(city_name_str) <= 60 and len(city_name_str) > 0 \
		and self.__airport_name_str.isalpha() == True and len(airport_name_str) <= 60 and len(airport_name_str) > 0 \
		and isinstance(__distance_int,int) and __distance_int > 0 \
        and isinstance(__flight_time_int,int) and __flight_time_int > 0:	
        	self.__valid_bool = True
=======
	"""
	Model class for destinations.
	"""

	def __init__(self):
		self.__country_name_str = ""
		self.__city_name_str = ""
		self.__ID_str = ""
		self.__airport_name_str = ""
		self.__distance_int = ""
		self.__flight_time_int = ""
		self.__contact_name_str = ""
		self.__contact_phone_str = ""
		self.__valid_bool = False

	# Tjekk hvort öll helstu attribute seu sett og innan lengar-/staerdartakmarkana áður en þau eru acceptuð inn í database

	def set_valid(self):
		self.__valid_bool = True
		return True

	def get_valid(self):
		return self.__valid_bool

	def set_country_name(self, name_str):
		if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
			self.__country_name_str = name_str
			return True
>>>>>>> 6a82a579c2d1da4198142fb7d453c8a7ce7fadc8
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

	def set_ID(self, id_str):
		if len(id_str) == 3 and id_str.isalpha():
			self.__ID_str = id_str
			return True
		else:
			return False

	def get_ID(self):
		return self.__ID_str

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

	def getattributes(self):
		column_names = ["valid", "ID", "country", "city", "airport", "flight_time", "distance", "contact_name", "contact_phone"]
		attributes = [
			self.__valid_bool,
			self.__ID_str,
			self.__country_name_str,
			self.__city_name_str,
			self.__airport_name_str,
			self.__flight_time_int,
			self.__distance_int,
			self.__contact_name_str,
			self.__contact_phone_str,
		]

		attribute_dict = dict(zip(column_names, attributes))
		return attribute_dict
