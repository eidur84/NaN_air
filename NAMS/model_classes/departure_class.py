# -*- coding: utf-8 -*-
import datetime as dt

class Departure:
	"""
	Class for handling information regarding outbound flights. Return flights are generated automatically in logic layer.
	"""

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
		self.__manned = False
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
			self.__year = Departure.check_year(str(attribute_dict["year"]))
			self.__month = Departure.check_month(str(attribute_dict["month"]))
			self.__day = Departure.check_day(str(attribute_dict["day"]))
			self.__hour = Departure.check_hour(str(attribute_dict["hour"]))
			self.__minute = Departure.check_minute(str(attribute_dict["minute"]))

			if self.__year.isdecimal() and self.__month.isdecimal() and self.__day.isdecimal() and self.__hour.isdecimal() and self.__minute.isdecimal():
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




	#----------------------- Basic check functions end

	def check_year(year):
		if year.isdecimal() and len(year) < 5 or year == "":
			return year
		else:
			return "Villa"

	def check_month(month):
		if month.isdecimal() and 0 < int(month) < 13  or month == "":
			return month
		else:
			return "Villa"

	def check_day(day):
		if day.isdecimal() and 0 < int(day) < 32  or day == "":
			return day
		else:
			return "Villa"

	def check_hour(hour):
		if hour.isdecimal() and 0 <= int(hour) < 24  or hour == "":
			return hour
		else:
			return "Villa"

	def check_minute(minute):
		if minute.isdecimal() and 0 <= int(minute) < 60  or minute == "":
			return minute
		else:
			return "Villa"

	def arrivingAt_check(dest_id):
		if len(dest_id) == 3 and dest_id.isupper() or dest_id == "":
			return dest_id
		else:
			return "Villa"

	def aircraft_name_check(name):
		if len(name) >= 4 or name == "":
			return name.upper()
		else:
			return "Villa"

	#----------------------- Basic check functions end

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

	def set_manned(self, boolean):
		self.__manned = boolean

	def dict_keys(self):
		return ["valid", "arrivingAt", "year", "month", "day", "hour", "minute", "aircraft_name"]

	def short_display(self, show_manned=True):
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
		if show_manned is True:
			if self.__manned is True:
				first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Brottför: {time}, {weekday}. {month_day}. {month} {year}. {self.__aircraft_name}. Mannað"
			else:
				first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Brottför: {time}, {weekday}. {month_day}. {month} {year}. {self.__aircraft_name}. Ómannað"
		else:
			first_half = f"{self.__departingFrom} til {self.__arrivingAt}. Brottför: {time}, {weekday}. {month_day}. {month} {year}. {self.__aircraft_name}."
		return first_half


