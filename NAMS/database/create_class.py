# -*- coding: utf-8 -*-
from database.database_layer import DBLayer
from csv import DictWriter
from pathlib import Path


class Create(DBLayer):
	"""
	Class for handling Create functionality of database layer.
	Functions return True if creation was successful.

	Methods:
		append_db_row(filename, object_instance)
		create_rtrip(rtrip_instance)
		create_crew(crew_instance)
	"""
	@staticmethod
	def append_db_row(filename, obj_instance, rtrip=False):
		"""
		Appends the data from an object instance to given file.
		"""
		backup_csv = DBLayer.path.joinpath("backups").joinpath(filename)
		filename = DBLayer.path.joinpath(filename)
		filestream = open(filename, "a", encoding="utf-8")

		if rtrip:
			new_row_dict = obj_instance.get_attributes(True)
		else:
			new_row_dict = obj_instance.get_attributes()
		column_names = list(new_row_dict.keys())


		writer = DictWriter(filestream, column_names)

		writer.writerow(new_row_dict)
		filestream.close()

		# Update backup files
		updated_file = open(filename, "r", encoding="utf-8")
		updated_data = updated_file.read()
		updated_file.close()

		backup_filestream = open(backup_csv, "w", encoding="utf-8")
		backup_filestream.write(updated_data)
		backup_filestream.close()

		return True

	@staticmethod
	def create_rtrip(departure, returnflight):
		"""
		Adds new round trip (voyage), using append_db_row function.
		"""

		bool1 = Create.append_db_row("RoundTrips.csv", departure, rtrip=True)
		bool2 = Create.append_db_row("RoundTrips.csv", returnflight, rtrip=True)

		finished = bool1 and bool2
		return finished

	@staticmethod
	def create_crew(crew_row):
		""" Adds row to Crew.csv"""

		finished = Create.append_db_row("Crew.csv", crew_row)
		return finished





