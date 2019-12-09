# -*- coding: utf-8 -*-
from csv import DictReader
from database.database_layer import DBLayer
from model_classes.employee_class import Employee
from model_classes.airplane_class import Airplane
from model_classes.destination_class import Destination
from model_classes.departure_class import Departure
from model_classes.returnflight_class import ReturnFlight
from model_classes.rtrip_class import RTrip


class Read(DBLayer):
	"""
	Class for read functionality of database layer. Searches files and returns list of instances of requested object.
	"""

	def read_staff(filter_column, key_word):
		attribute_dict_list = DBLayer.generic_search('Staff.csv', filter_column, key_word)
		staff_list = [ ]
		for attribute_dict in attribute_dict_list:
			employee = Employee(attribute_dict)
			staff_list.append(employee)

		return staff_list

	def read_airplane(filter_column, key_word):
		attribute_dict_list = DBLayer.generic_search('Airplanes.csv', filter_column, key_word)
		airplane_list = [ ]
		for attribute_dict in attribute_dict_list:
			airplane = Airplane(attribute_dict)
			airplane_list.append(airplane)

		return airplane_list

	def read_dest(filter_column, key_word):
		attribute_dict_list = DBLayer.generic_search('Destinations.csv', filter_column, key_word)
		dest_list = [ ]
		for attribute_dict in attribute_dict_list:
			destination = Destination(attribute_dict)
			dest_list.append(destination)

		return dest_list


	def read_rtrip(filter_column, key_word):
		attribute_dict_list = DBLayer.generic_search('RoundTrips.csv', filter_column, key_word)
		rtrip_list = [ ]
		count = 0
		for attribute_dict in attribute_dict_list:

			if attribute_dict["direction"] == "outbound":
				departure = Departure(attribute_dict, from_csv=True)
				count += 1
			elif attribute_dict["direction"] == "inbound":
				returnflight = ReturnFlight(attribute_dict)
				count += 1

			if count == 2:
				rtrip = RTrip(departure, returnflight)
				count = 0
				rtrip_list.append(rtrip)

		return rtrip_list
