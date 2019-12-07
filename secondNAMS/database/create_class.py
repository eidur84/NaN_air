from database.database_layer import DBLayer
from model_classes import *
from csv import DictWriter
from pathlib import Path


class Create(DBLayer):
	"""
	Class for handling Create functionality of database layer.
	Functions return True if creation was successful.

	Methods:
		append_db_row(filename, object_instance)
		create_staff(employee_instance)
		create_airplane(airplane_instance)
		create_destination(destination_instance)
		create_rtrip(rtrip_instance)
	"""

	def append_db_row(filename, obj_instance):
		"""
		Appends the data from an object instance to given file.
		"""

		filestream = open(filename, "a")

		new_row_dict = obj_instance.get_attributes()
		column_names = list(new_row_dict.keys())


		writer = DictWriter(filestream, column_names)

		writer.writerow(new_row_dict)

		filestream.close()
		return True


	def create_staff(employee):
		"""
		Adds new staff member, using append_db_row function.
		"""
		csv_file = DBLayer.path.joinpath("Staff.csv")

		finished = Create.append_db_row(csv_file, employee)
		return finished


	def create_airplane(airplane):
		"""
		Adds new airplane, using append_db_row function.
		"""
		csv_file = DBLayer.path.joinpath("Airplanes.csv")

		finished = Create.append_db_row(csv_file, airplane)
		return finished


	def create_dest(destination):
		"""
		Adds new destination, using append_db_row function.
		"""
		csv_file = DBLayer.path.joinpath("Destinations.csv")

		finished = Create.append_db_row(csv_file, destination)
		return finished


	def create_rtrip(departure, returnflight):
		"""
		Adds new round trip (voyage), using append_db_row function.
		"""
		csv_file = DBLayer.path.joinpath("RoundTrips.csv")

		bool1 = Create.append_db_row(csv_file, departure)
		bool2 = Create.append_db_row(csv_file, returnflight)

		finished = bool1 and bool2
		return finished




