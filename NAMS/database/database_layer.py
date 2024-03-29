# -*- coding: utf-8 -*-
from csv import DictReader, DictWriter
from pathlib import Path
# Children imported at bottom of file

class DBLayer:
	"""
	Class for main/shared functionality of database layer.
	Parses information from the logic layer and sends to corresponding child CRUD class.
	"""

	# pathlib.Path used for system agnostic directory paths.
	path = Path.cwd().joinpath("database").joinpath("csv_files")

	@staticmethod
	def request_create(data_type, instance):
		if data_type == "staff":
			valid = Create.create_staff(instance)

		elif data_type == "dest":
			valid = Create.create_dest(instance)

		elif data_type == "airplane":
			valid = Create.create_airplane(instance)

		elif data_type == "rtrip":
			valid = Create.create_rtrip(instance[0], instance[1])
		else:
			return False

		return valid

	@staticmethod
	def generic_search(filename, filter_column, key_word, result_column="all"):
		"""
		Function which searches a csv file for key_word in filter_column.
		Returns value in specified result_column for each matched row.
		Returns all values in row if result_column is "all" (default value).
		"""

		csv_file = DBLayer.path.joinpath(filename)

		filestream = open(csv_file, "r", encoding="utf-8")
		csv_dict = DictReader(filestream)  # Loads rows into dictionary with column names as keys.


		results = [ ]

		for row in csv_dict:

			# Finds row with value in filter_column matching key_word.
			if row[filter_column] == key_word and row["valid"] == "True":

				if result_column == "all":
					results.append(dict(row))

				else:
					results.append(row[result_column])

		filestream.close()
		return results

	@staticmethod
	def get_csv_data(filename):
		"""
		Reads data from given csv file into list of dictionaries.
		Dict:
			Key: column name, Value: each rows corresponding value.
		"""
		filename = DBLayer.path.joinpath(filename)
		filestream = open(filename, "r", encoding="utf-8")
		csv_reader = DictReader(filestream)

		dict_list = [ ]
		for row in csv_reader:
			dict_list.append(dict(row))

		filestream.close()
		return dict_list

	@staticmethod
	def write_csv_file(filename, dict_list):
		"""
		Overwrites a given csv file with data from a given list of dictionaries.
		Dict:
			Key: column name, Value: each rows corresponding value.
		"""

		if len(dict_list) == 0:
			return False

		backup_csv = DBLayer.path.joinpath("backups").joinpath(filename)
		filename = DBLayer.path.joinpath(filename)

		column_names = list(dict_list[0].keys())

		filestream = open(filename, "w", encoding="utf-8")
		writer = DictWriter(filestream, fieldnames=column_names)

		writer.writeheader()
		for row in dict_list:
			writer.writerow(row)


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
	def update_db_row(filename, column_name, new_data, PK_column, key_word):
		"""
		Searches PK_column in csv file for key_word, changes data in column_name to new_data.
		"""

		dict_list = DBLayer.get_csv_data(filename)

		for row in dict_list:
			if row[PK_column] == key_word:
				row[column_name] = new_data
				break

		finished = DBLayer.write_csv_file(filename, dict_list)
		return finished


	@staticmethod
	def invalidate_crew_members(tuple_list):
		"""
		Function receives list of tuples (ssn, flightID) and changes validity of matching lines in Crew.csv file to False
		"""
		crew_dict_list = DBLayer.get_csv_data("Crew.csv")
		for ssn, flightid in tuple_list:
			for row in crew_dict_list:
				if row["ssn"] == ssn and row["flightID"] == flightid:
					row["valid"] = "False"
					break

		finished = DBLayer.write_csv_file("Crew.csv", crew_dict_list)
		return finished

# IMPORTS AT BOTTOM OF FILE TO PREVENT CIRCULAR IMPORTS (X imports Y and Y starts by importing X)
from database.create_class import Create
from database.update_class import Update
from database.invalidate_class import Invalidate
# See http://effbot.org/zone/import-confusion.htm#circular-imports for explanation
