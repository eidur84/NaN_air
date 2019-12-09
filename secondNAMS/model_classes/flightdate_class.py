import datetime as dt


class FlightDate:

	def __init__(self, datetime):
		self.datetime = FlightDate.make_isoformat(datetime)

	def make_isoformat(datetime):
		return datetime.isoformat()

	def short_display(self):
		printobject = f"{self.datetime}"
		return printobject

	def get_datetime(self):
		return self.datetime
