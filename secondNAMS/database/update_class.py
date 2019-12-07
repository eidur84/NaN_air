
from database.database_layer import DBLayer
from model_classes.destination_class import Destination
from model_classes.airplane_class import Airplane
from model_classes.employee_class import Employee
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
		#elif type(new_instance) is RTrip:
		#	filename = "RoundTrips.csv"

		dict_list = Update.get_csv_data(filename)
		try:
			index = dict_list.index(old_attributes)
			dict_list[index] = new_instance.get_attributes()

		except IndexError:
			return False

		finished = Update.write_csv_file(filename, dict_list)
		return finished

	def update_staff(employee, change_column, new_value):

		search_ssn = employee.get_ssn()
		finished = Update.update_db_row("Staff.csv", change_column, new_value, "ssn", search_ssn)
		return finished

	def update_airplane(airplane, change_column, new_value):

		search_name = airplane.get_name()
		finished = Update.update_db_row("Airplanes.csv", change_column, new_value, "name", search_name)
		return finished

	'''
	### Flóknara
	def update_rtrip(rtrip, change_column, new_value):
		search_ssn = rtrip.get_ID()
		finished = DBLayer.update_db_row("Staff.csv", change_column, new_value, "ssn", search_ssn)
		return True
	'''

	def update_dest(destination, change_column, new_value):
		search_ID = destination.get_ID()
		finished = Update.update_db_row("Destinations.csv", change_column, new_value, "ID", search_ID)
		return finished
