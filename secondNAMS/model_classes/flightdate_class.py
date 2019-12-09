import datetime as dt


class FlightDate:

	def __init__(self, datetime):
		self.datetime = datetime.isoformat()

	def short_display(self):
		printobject = f"{self.datetime}"
		return printobject

	def get_datetime(self):
		return self.datetime
