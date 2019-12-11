# -*- coding: utf-8 -*-
import datetime as dt

class ReturnFlight:
	"""
	Class for flight back from destination to KEF. Created automatically from departure by logic layer.
	"""
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


	def short_display(self, schedule_view=False):
		if schedule_view is True:
			departure_dt = dt.datetime.strptime(self.__arrival, "%Y-%m-%dT%H:%M:%S")
		else:
			departure_dt = dt.datetime.strptime(self.__departure, "%Y-%m-%dT%H:%M:%S")
		time = departure_dt.strftime("%H:%M")
		weekday_list = ["Sun", "Mán", "Þri", "Mið", "Fim", "Fös", "Lau"]
		weekday = weekday_list[int(departure_dt.strftime("%w"))]
		month_day = departure_dt.strftime("%d").lstrip("0")
		month_list = [
			"Janúar",
			"Febrúar",
			"Mars",
			"Apríl",
			"Maí",
			"Júní",
			"Júlí",
			"Ágúst",
			"September",
			"Október",
			"Nóvember",
			"Desember"
		]
		month = month_list[int(departure_dt.strftime("%m")) - 1]
		year = departure_dt.strftime("%Y")
		if schedule_view is True:
			first_half = f"Heimkoma: {time}, {weekday}. {month_day}. {month} {year}."
		else:
			first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Brottför: {time}, {weekday}. {month_day}. {month} {year}."
		return first_half





