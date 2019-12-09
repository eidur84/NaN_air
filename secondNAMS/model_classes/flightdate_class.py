import datetime as dt


class FlightDate:
	"""
	Class for handling dates. Recieves datetime object at initializion.
	"""

	def __init__(self, datetime_obj):
		self.__datetime_obj = datetime_obj
		self.__isodate = datetime_obj.isoformat()

	def short_display(self):
		return f"{self.__datetime.day}, {self.__datetime.month}, {self.__datetime.year}"

	def get_datetime_obj(self):
		return self.__datetime_obj

	def get_isodate(self):
		return self.__isodate
