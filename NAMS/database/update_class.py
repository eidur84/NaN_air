# -*- coding: utf-8 -*-
from database.database_layer import DBLayer
from model_classes.destination_class import Destination
from model_classes.airplane_class import Airplane
from model_classes.employee_class import Employee
from model_classes.departure_class import Departure
from model_classes.returnflight_class import ReturnFlight

from csv import DictWriter
from pathlib import Path


class Update(DBLayer):
	"""
	Class for updating rows in csv files.
	"""
	@staticmethod
	def replace_row(old_attributes, new_instance, filename=""):
		"""
		Rewrites line matching old_attibutes with attributes of new_instance.
		Args:
			old_attributes: dict containing old info to search for in csv file.
			new_instance: instance of a given updated object.
		"""
		if type(new_instance) is Destination:
			filename = Update.path.joinpath("Destinations.csv")
		elif type(new_instance) is Employee:
			filename = Update.path.joinpath("Staff.csv")
		elif type(new_instance) is Airplane:
			filename = Update.path.joinpath("Airplanes.csv")
		elif type(new_instance) is Departure or type(new_instance) is ReturnFlight:
			filename = Update.path.joinpath("RoundTrips.csv")

		dict_list = Update.get_csv_data(filename)

		try:
			index = dict_list.index(old_attributes)
			if type(new_instance) is Departure or type(new_instance) is ReturnFlight:
				dict_list[index] = new_instance.get_attributes(True)
			else:
				dict_list[index] = new_instance.get_attributes()

		except ValueError:
			return False

		finished = Update.write_csv_file(filename, dict_list)
		return finished

	@staticmethod
	def replace_crew(departure, new_crew_list):
		"""
		Updates crew info for given flight.
		(Invalidates old crew and writes new crew to csv file.)
		"""
		filename = Update.path.joinpath("Crew.csv")
		dict_list = Update.get_csv_data(filename)

		flightID = departure.get_attributes()["flightID"]

		for row in dict_list:
			if row["flightID"] == flightID:
				row["valid"] = False

		for crew_row in new_crew_list:
			new_row = crew_row.get_attributes()
			dict_list.append(new_row)

		finished = Update.write_csv_file(filename, dict_list)
		return finished

	@staticmethod
	def replace_rtrip_row(departure, returnflight):
		"""
		Function for updating rows in round trip csv file. Edits two lines instead of one.
		Args:
			departure: updated instance of Departure class
			returnflight: updated instance of ReturnFlight class
		"""
		new_dep_attributes = departure.get_attributes(for_csv=True)
		new_ret_attributes = returnflight.get_attributes(for_csv=True)

		old_departure_dict = DBLayer.generic_search("RoundTrips.csv", "flightID", new_dep_attributes["flightID"])[0]
		old_returnflight_dict = DBLayer.generic_search("RoundTrips.csv", "flightID", new_ret_attributes["flightID"])[0]

		bool1 = Update.replace_row(old_departure_dict, departure)
		bool2 = Update.replace_row(old_returnflight_dict, returnflight)

		return bool1 and bool2

	@staticmethod
	def update_rtrip_csv_file():
		"""
		Goes through RoundTrips.csv, and sets "past" column to be True if flight date is before current day, False otherwise.
		Achieved by changing rows into model classes and writing file again.
		"""
		filename = DBLayer.path.joinpath("RoundTrips.csv")

		flight_data = DBLayer.get_csv_data(filename)
		updated_data = [ ]
		outbound = True
		for flight_row in flight_data:
			if outbound:
				departure = Departure(flight_row, from_csv=True)
				updated_data.append(departure.get_attributes(for_csv=True))
				outbound = False
			elif not outbound:
				returnflight = ReturnFlight(flight_row)
				updated_data.append(returnflight.get_attributes(for_csv=True))
				outbound = True

		flights_updated_bool = DBLayer.write_csv_file(filename, updated_data)
		return flights_updated_bool


