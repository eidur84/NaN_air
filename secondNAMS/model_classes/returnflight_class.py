# -*- coding: utf-8 -*-
import datetime as dt

class ReturnFlight:
	empty_attribute_dict = {
		"valid": False,
		"past": False,
		"flightID": "",
		"departingFrom": "",
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
		self.__direction = "inbound"
		self.__departingFrom = attribute_dict["departingFrom"]
		self.__arrivingAt = "KEF"
		self.__departure = dt.datetime.strptime(attribute_dict["departure"], "%Y-%m-%dT%H:%M:%S")

		self.__year = self.__departure.year
		self.__month = self.__departure.month
		self.__day = self.__departure.day
		self.__hour = self.__departure.hour
		self.__minute = self.__departure.minute

		self.__past = dt.datetime.today() > self.__departure
		self.__departure = self.__departure.isoformat()

		self.__arrival = attribute_dict["arrival"]
		self.__aircraft_name = attribute_dict["aircraft_name"]


	def get_attributes(self, for_csv=False):
		""" Returns dictionary of instances attributes."""
		if for_csv:
			attribute_dict = {
				"valid": self.__valid,
				"past": self.__past,
				"direction": "inbound",
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
				"direction": "inbound",
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


	def short_display(self):
		first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Kl: {self.__departure}"
		return first_half

	def __str__(self):

		first_half = f"Flugnúmer: {self.__flightID}. Frá {self.__departingFrom} til {self.__arrivingAt}. "
		second_half = f"Brottför: {self.__departure}. Lending: {self.__arrival}. Flugvél: {self.__aircraft_name}"
		return first_half + second_half

