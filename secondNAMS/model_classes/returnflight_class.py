

class ReturnFlight:
	empty_attribute_dict = {
		"valid": False,
		"past": False,
		"flightID": "",
		"departingFrom": "",
		"departure": "",
		"arrival": "",
		"aircraft_name": ""
	}

	def __init__(self, attribute_dict = empty_attribute_dict):

		self.__valid = attribute_dict["valid"]
		self.__past = attribute_dict["past"]
		self.__flightID = attribute_dict["flightID"]
		self.__departingFrom = attribute_dict["departingFrom"]
		self.__arrivingAt = "KEF"
		self.__departure = attribute_dict["departure"]
		self.__arrival = attribute_dict["arrival"]
		self.__aircraft_name = attribute_dict["aircraft_name"]

	def get_attributes(self):
		""" Returns dictionary of instances attributes."""
		attribute_dict = {
			"valid": self.__valid,
			"past": self.__past,
			"flightID": self.__flightID,
			"departingFrom": self.__departingFrom,
			"arrivingAt": self.__arrivingAt,
			"departure": self.__departure,
			"arrival": self.__arrival,
			"aircraft_name": self.__aircraft_name
		}

		return attribute_dict

	def __str__(self):

		first_half = f"Flugnúmer: {self.__flightID}. Frá {self.__departingFrom} til {self.__arrivingAt}. "
		second_half = f"Brottför: {self.__departure}. Lending: {self.__arrival}. Flugvél: {self.__aircraft_name}"
		return first_half + second_half