
from database.database_layer import DBLayer
from model_classes import *
from csv import DictWriter
from pathlib import Path


class Update(DBLayer):


	def update_staff(employee, change_column, new_value):

		search_ssn = employee.get_ssn()
		finished = DBLayer.update_db_row("Staff.csv", change_column, new_value, "ssn", search_ssn)
		return True

	def update_airplane(airplane, change_column, new_value):

		search_name = airplane.get_name()
		finished = DBLayer.update_db_row("Airplanes.csv", change_column, new_value, "name", search_name)
		return True

	'''
	### Flóknara
	def update_rtrip(rtrip, change_column, new_value):
		search_ssn = rtrip.get_ID()
		finished = DBLayer.update_db_row("Staff.csv", change_column, new_value, "ssn", search_ssn)
		return True
	'''

	def update_dest(destination, change_column, new_value):
		search_ID = destination.get_ID()
		finished = DBLayer.update_db_row("Destinations.csv", change_column, new_value, "ID", search_ID)
		return True
