# -*- coding: utf-8 -*-
from database.database_layer import DBLayer
from model_classes.employee_class import Employee
from model_classes.airplane_class import Airplane
from model_classes.destination_class import Destination
from model_classes.departure_class import Departure
from model_classes.crew_class import Crew

class Read(DBLayer):
	"""
	Class for read functionality of database layer. Searches files and returns list of instances of requested object.
	"""

	@staticmethod
	def read_staff(filter_column, key_word):
		"""
		Looks in staff csv file for rows matching given conditions.
		Returns list of instances.
		"""
		attribute_dict_list = DBLayer.generic_search('Staff.csv', filter_column, key_word)
		staff_list = [ ]
		for attribute_dict in attribute_dict_list:
			employee = Employee(attribute_dict)
			staff_list.append(employee)

		return staff_list

	@staticmethod
	def read_airplane(filter_column="valid", key_word="True"):
		"""
		Looks in airplane csv file for rows matching given conditions.
		Returns list of instances.
		"""
		attribute_dict_list = DBLayer.generic_search('Airplanes.csv', filter_column, key_word)

		airplane_list = [ ]
		for attribute_dict in attribute_dict_list:
			airplane = Airplane(attribute_dict)
			airplane_list.append(airplane)

		return airplane_list

	@staticmethod
	def read_dest(filter_column="valid", key_word="True"):
		"""
		Looks in destination csv file for rows matching given conditions.
		Returns list of instances.
		"""
		attribute_dict_list = DBLayer.generic_search('Destinations.csv', filter_column, key_word)
		dest_list = [ ]
		for attribute_dict in attribute_dict_list:
			destination = Destination(attribute_dict)
			dest_list.append(destination)

		return dest_list

	@staticmethod
	def read_rtrip(filter_column="valid", key_word="True"):
		"""
		Looks in rtrip csv file for rows matching given conditions.
		Returns list of rows in round trip file.
		"""
		attribute_dict_list = DBLayer.generic_search('RoundTrips.csv', filter_column, key_word)

		return attribute_dict_list

	@staticmethod
	def flight_crew(flightID = "all"):
		"""
		Finds crew members for a given flightID. Returns list of Crew instances (rows in csv file).
		"""

		crew_list = [ ]
		if flightID == "all":
			attribute_dict_list = Read.generic_search("Crew.csv", "valid", "True")

			for attribute_dict in attribute_dict_list:
				crew_row = Crew(attribute_dict)
				crew_list.append(crew_row)

		else:
			attribute_dict_list = Read.generic_search("Crew.csv", "flightID", flightID)

			for attribute_dict in attribute_dict_list:
				if attribute_dict["valid"] == "True":
					crew_row = Crew(attribute_dict)
					crew_list.append(crew_row)


		return crew_list

	@staticmethod
	def departures_on_date(date_str):
		""" Finds departures on same day as date_str (format: YYYY-MM-DD)."""

		attribute_dict_list = Read.read_rtrip("valid", "True")
		departure_list = [ ]
		for row_nr in range(0, len(attribute_dict_list), 2):
			if attribute_dict_list[row_nr]["departure"][0:10] == date_str:
				departure = Departure(attribute_dict_list[row_nr], from_csv=True)
				departure_list.append(departure)

		return departure_list



