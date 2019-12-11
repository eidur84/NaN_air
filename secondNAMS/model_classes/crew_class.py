
class Crew:
	"""
	Class containing information for a row in crew csv file.
	"""

	def __init__(self, attribute_dict):
		self.__valid = True
		self.__flightID = attribute_dict["flightID"]
		self.__ssn = attribute_dict["ssn"]
		self.__role = attribute_dict["role"]
		self.__rank = attribute_dict["rank"]


	def get_attributes(self):
		return {
			"valid": self.__valid,
			"flightID": self.__flightID,
			"ssn": self.__ssn,
			"role": self.__role,
			"rank": self.__rank
		}


	def get_rank(self):
		return self.__rank


	def __str__(self):
		return f"{self.__flightID}, {self.__ssn}: {self.__rank}"

