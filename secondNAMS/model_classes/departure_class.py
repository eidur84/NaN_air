
import datetime as dt

class Departure:
	empty_attribute_dict = {
		"valid": False,
		"past": False,
		"flightID": "",
		"arrivingAt": 0,
		"year": 1,
		"month": 1,
		"day": 1,
		"hour": 0,
		"minute": 0,
		"departure": "",
		"arrival": "",
		"aircraft_name": ""
	}

	def __init__(self, attribute_dict = empty_attribute_dict):
		self.__valid = attribute_dict["valid"]
		self.__flightID = attribute_dict["flightID"]
		self.__departingFrom = "KEF"
		self.__arrivingAt = attribute_dict["arrivingAt"]
		self.__year = int(attribute_dict["year"])
		self.__month = int(attribute_dict["month"])
		self.__day = int(attribute_dict["day"])
		self.__hour = int(attribute_dict["hour"])
		self.__minute = int(attribute_dict["minute"])
		try:
			self.__departure = dt.datetime(self.__year, self.__month, self.__day, self.__hour, self.__minute).isoformat()
			self.__past = dt.datetime.today() > self.__departure
		except ValueError:
			self.__departure = "ERROR"
			self.__past = False


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
			"year": self.__year,
			"month": self.__month,
			"day": self.__day,
			"hour": self.__hour,
			"minute": self.__minute,
			"departure": self.__departure,
			"arrival": self.__arrival,
			"aircraft_name": self.__aircraft_name
		}

		return attribute_dict


	def attribute_translation(self):
		return [
			("Auðkenni áfangastaðar", self.__arrivingAt),
			("Ár", self.__year),
			("Mánuður", self.__month),
			("Dagur", self.__day),
			("Klukkustund", self.__hour),
			("Mínútur", self.__minute),
			("Nafn flugvélar", self.__aircraft_name)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		return ["valid", "arrivingAt", "year", "month", "day", "hour", "minute", "aircraft_name"]

	def short_display(self):
		first_half = f"{self.__departingFrom} til {self.__arrivingAt}. {self.__departure}"
		return first_half

	def __str__(self):
		first_half = f"Flugnúmer: {self.__flightID}. Frá {self.__departingFrom} til {self.__arrivingAt}. "
		second_half = f"Brottför: {self.__departure}. Lending: {self.__arrival}. Flugvél: {self.__aircraft_name}"
		return first_half + second_half
