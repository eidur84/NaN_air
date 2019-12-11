# -*- coding: utf-8 -*-
from database.database_layer import DBLayer
from model_classes import *
from csv import DictWriter
from pathlib import Path


class Invalidate(DBLayer):
	"""
	Class for delete (invalidate) functionality in database layer.
	Sets valid value to "False".
	"""

	def invalidate_staff(employee):
		"""
		Sets valid value for given employee to False.
		"""
		csv_file = DBLayer.path.joinpath("Staff.csv")

		employee_ssn = employee.get_attributes()["name"]
		finished = Invalidate.update_db_row(csv_file, "valid", "False", "ssn", employee_ssn)
		return finished


	def invalidate_airplane(airplane):
		"""
		Sets valid value for given airplane to False.
		"""
		csv_file = DBLayer.path.joinpath("Airplanes.csv")

		airplane_name = airplane.get_attributes()["name"]
		finished = Invalidate.update_db_row(csv_file, "valid", "False", "name", airplane_name)
		return finished


	def invalidate_dest(destination):
		"""
		Sets valid value for given destination to False.
		"""
		csv_file = DBLayer.path.joinpath("Destinations.csv")

		dest_id = destination.get_attributes()["ID"]
		finished = Invalidate.update_db_row(csv_file, "valid", "False", "ID", dest_id)
		return finished

	##### Vantar fyrir round trip #####