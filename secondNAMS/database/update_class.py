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

	def replace_row(old_attributes, new_instance):
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

		except IndexError:
			return False

		finished = Update.write_csv_file(filename, dict_list)
		return finished


	def replace_rtrip_row(departure, returnflight):
		new_dep_attributes = departure.get_attributes(for_csv=True)
		new_ret_attributes = returnflight.get_attributes(for_csv=True)

		old_departure_dict = DBLayer.generic_search("RoundTrips.csv", "flightID", new_dep_attributes["ID"])[0]
		old_returnflight_dict = DBLayer.generic_search("RoundTrips.csv", "flightID", new_ret_attributes["ID"])[0]

		bool1 = Update.replace_row(old_departure_dict, departure)
		bool2 = Update.replace_row(old_returnflight_dict, returnflight)

		return bool1 and bool2
