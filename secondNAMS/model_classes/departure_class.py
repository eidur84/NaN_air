# -*- coding: utf-8 -*-
import datetime as dt

class Departure:
	empty_attribute_dict = {
		"valid": False,
		"past": False,
		"flightID": "",
		"arrivingAt": "",
		"year": "",
		"month": "",
		"day": "",
		"hour": "",
		"minute": "",
		"departure": "",
		"arrival": "",
		"aircraft_name": ""
	}

	def __init__(self, attribute_dict = empty_attribute_dict, from_csv=False):

		self.__valid = attribute_dict["valid"]
		self.__flightID = attribute_dict["flightID"]
		self.__past = False
		self.__direction = "outbound"
		self.__departingFrom = "KEF"
		self.__departure = ""
		self.__arrivingAt = Departure.arrivingAt_check(attribute_dict["arrivingAt"])

		if from_csv:
			self.__departure = dt.datetime.strptime(attribute_dict["departure"], "%Y-%m-%dT%H:%M:%S")

			self.__year = self.__departure.year
			self.__month = self.__departure.month
			self.__day = self.__departure.day
			self.__hour = self.__departure.hour
			self.__minute = self.__departure.minute

			self.__past = dt.datetime.today() > self.__departure
			self.__departure = self.__departure.isoformat()

		else:
			self.__year = str(attribute_dict["year"])
			self.__month = str(attribute_dict["month"])
			self.__day = str(attribute_dict["day"])
			self.__hour = str(attribute_dict["hour"])
			self.__minute = str(attribute_dict["minute"])

			if self.__year != "" and self.__month != "" and self.__day != "" and self.__hour != "" and self.__minute != "":
				self.__departure = dt.datetime(
					int(self.__year),
					int(self.__month),
					int(self.__day),
					int(self.__hour),
					int(self.__minute)
				)
				self.__past = dt.datetime.today() > self.__departure
				self.__departure = self.__departure.isoformat()



		self.__arrival = attribute_dict["arrival"]
		self.__aircraft_name = Departure.aircraft_name_check(attribute_dict["aircraft_name"])


	def arrivingAt_check(arrival):
		if len(arrival) == 3 and arrival.isupper() or arrival == "":
			return arrival
		else:
			return "Óþekkur aðkomustaður"

	def aircraft_name_check(name):
		if len(name) >= 4 or name == "":
			return name
		else:
			return "Óþekkt flugvélanafn"

	def get_attributes(self, for_csv=False):
		""" Returns dictionary of instances attributes."""
		if for_csv:
			attribute_dict = {
				"valid": self.__valid,
				"past": self.__past,
				"direction": "outbound",
				"flightID": self.__flightID,
				"departingFrom": self.__departingFrom,
				"arrivingAt": self.__arrivingAt,
				"departure": self.__departure,
				"arrival": self.__arrival,
				"aircraft_name": self.__aircraft_name
			}

		else:
			attribute_dict = {
				"valid": self.__valid,
				"past": self.__past,
				"direction": "outbound",
				"flightID": self.__flightID,
				"departingFrom": self.__departingFrom,
				"arrivingAt": self.__arrivingAt,
				"departure": self.__departure,
				"year": self.__year,
				"month": self.__month,
				"day": self.__day,
				"hour": self.__hour,
				"minute": self.__minute,
				"arrival": self.__arrival,
				"aircraft_name": self.__aircraft_name
			}

		return attribute_dict


	def attribute_translation(self):
		return [
			("Auðkenni áfangastaðar", self.__arrivingAt),
			("Ár", str(self.__year)),
			("Mánuður", str(self.__month)),
			("Dagur", str(self.__day)),
			("Klukkustund", str(self.__hour)),
			("Mínútur", str(self.__minute)),
			("Nafn flugvélar", self.__aircraft_name)
		]

	def set_valid(self):
		self.__valid = True

	def dict_keys(self):
		return ["valid", "arrivingAt", "year", "month", "day", "hour", "minute", "aircraft_name"]

	def short_display(self):
		first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Kl: {self.__departure}"
		return first_half

	def __str__(self):
		first_half = f"Flugnúmer: {self.__flightID}. Frá {self.__departingFrom} til {self.__arrivingAt}. "
		second_half = f"Brottför: {self.__departure}. Lending: {self.__arrival}. Flugvél: {self.__aircraft_name}"
		return first_half + second_half
