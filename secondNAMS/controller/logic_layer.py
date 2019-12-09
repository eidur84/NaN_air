# -*- coding: utf-8 -*-
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
		elif state == "employee_list":
			data = Read.read_staff("valid", "True")
		elif state == "rtrip_list":
			data = Read.read_rtrip("valid", "True")

		display_data["data"] = [ instance for instance in data ]
		if state == "date_list":
			display_data["page_size"] = 7
		elif state == "rtrip_list":
			display_data["page_size"] = 3
			display_data["rtrip"] = True
		else:
			display_data["page_size"] = 5
		display_data["end"] = len(display_data["data"])

		return display_data


	def update_rtrip(departure, returnflight):
		finished = Update.replace_rtrip_row(departure, returnflight)
		return finished


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
			finished = BLLayer.create_returnflight(new_instance)
			# eh meira herna

		return finished

	def form_system(state):
		form_data = { }
		if state == "new_dest":
			form_data["instance"] = Destination()
		elif state == "new_employee":
			form_data["instance"] = Employee()
		elif state == "new_rtrip":
			form_data["instance"] = Departure()
		elif state == "new_airplane":
			form_data["instance"] = Airplane()

		return form_data

	def create_returnflight(departure):
		attribute_dict = departure.get_attributes()

		# Get destination ID
		dest = attribute_dict["arrivingAt"]

		# Flight time in minutes (int)
		flight_time = DBLayer.generic_search("Destinations.csv", "ID", dest, "flight_time")
		flight_time = int(flight_time[0])

		# Find last serial in csv file and increment
		serial = int(DBLayer.generic_search("RoundTrips.csv", "valid", "True", "flightID")[-1])
		attribute_dict["flightID"] = serial + 1

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

		# Increment serial
		attribute_dict["flightID"] += 1

		# Calculate arrival time back to KEF
		arrival_time = departure_time + dt.timedelta(minutes = flight_time)
		attribute_dict["arrival"] = arrival_time.isoformat()


		ret_flight = ReturnFlight(attribute_dict)

		finished = Create.create_rtrip(departure, ret_flight)

		return finished


