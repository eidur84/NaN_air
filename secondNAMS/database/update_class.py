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

	def replace_row(old_attributes, new_instance):
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
