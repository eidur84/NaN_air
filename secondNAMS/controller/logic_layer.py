
import datetime as dt

from database.read_class import Read
from database.create_class import Create
from database.update_class import Update
from database.database_layer import DBLayer


from model_classes.airplane_class import Airplane
from model_classes.departure_class import Departure
from model_classes.destination_class import Destination
from model_classes.employee_class import Employee
from model_classes.returnflight_class import ReturnFlight

class BLLayer:
	"""
	Business logic layer, handles communcaction betwwen UI and DB layers and does calculations relating to time.
	"""

	def paging_system(state):
		display_data = { }
		if state == "dest_list":
			data = Read.read_dest("valid", "True")
		elif state == "staff_list":
			data = Read.read_staff("valid", "True")
		elif state == "airplane_list":
			data = Read.read_airplane("valid", "True")

		display_data["data"] = [ instance for instance in data ]

		display_data["end"] = len(display_data["data"])

		return display_data

	def update_row(old_attributes, new_instance):
		finished = Update.replace_row(old_attributes, new_instance)
		return finished

	def create_row(state, new_instance):
		if state == "new_dest":
			finished = Create.create_dest(new_instance)
		elif state == "new_employee":
			finished = Create.create_staff(new_instance)
		elif state == "new_airplane":
			finished = Create.create_airplane(new_instance)
		elif state == "new_rtrip":
			finished = Create.create_rtrip(new_instance)
			# eh meira herna

		return finished


	def create_returnflight(departure):
		attribute_dict = departure.get_attributes()

		# Get destination ID
		dest = attribute_dict["arrivingAt"]

		# Flight time in minutes (int)
		flight_time = int(DBLayer.general_search("Destinations.csv", "ID", dest, "flight_time"))

		# Get departure time (iso format string)
		departure_time = attribute_dict["departure"]

		# Parse iso format string and add flight time minutes
		departure_time = dt.datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S")
		arrival_time = departure_time + dt.timedelta(minutes = flight_time)

		attribute_dict["arrival"] = arrival_time.isoformat()
		departure.__init__(attribute_dict)

		# Prepare attribute dict for ReturnFlight class
		# Switch ID for departingFrom and ArrivingAt
		attribute_dict["departingFrom"] = attribute_dict["arrivingAt"]
		attribute_dict["arrivingAt"] = "KEF"

		# Add 1 hour wait time
		departure_time = arrival_time + dt.timedelta(hours=1)
		attribute_dict["departure"] = departure_time.isoformat()

		# Calculate arrival time back to KEF
		arrival_time = departure_time + dt.timedelta(minutes = flight_time)
		attribute_dict["arrival"] = arrival_time


		ret_flight = ReturnFlight(attribute_dict)

		finished = Create.create_rtrip(departure, ret_flight)

		return finished









