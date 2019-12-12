
import datetime as dt

class FlightDate:
	"""
	Class for handling dates. Recieves datetime object at initializion.
	"""

	def __init__(self, datetime_obj):
		self.__datetime_obj = datetime_obj
		self.__isodate = datetime_obj.isoformat()

	def short_display(self, with_time=True, with_title=True):
		weekday_list = ["Sun", "Mán", "Þri", "Mið", "Fim", "Fös", "Lau"]
		weekday = weekday_list[int(self.__datetime_obj.strftime("%w"))]

		month_day = self.__datetime_obj.strftime("%d").lstrip("0")

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
		month = month_list[int(self.__datetime_obj.strftime("%m")) - 1]

		year = self.__datetime_obj.strftime("%Y")
		if with_time and with_title:
			first_half = f"Tími: {time}. Dagsetning: {weekday}. {month_day}. {month} {year}."
		elif not with_title and not with_time:
			first_half = f"{weekday}. {month_day}. {month} {year}."
		else:
			first_half = f"Dagsetning: {weekday}. {month_day}. {month} {year}."
		return first_half



	def get_datetime(self):
		return self.__datetime_obj

	def get_isodate(self):
		return self.__isodate
