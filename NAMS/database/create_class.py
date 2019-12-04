from database.DBLayer import DBLayer
from model_classes import *
from csv import DictWriter
from pathlib import Path


class Create(DBLayer):
	new_data_str = ""
	create_staff_str = ""
	create_airplane_str = ""
	create_dest_str = ""
	create_rtrip_str = ""

	def update_new_data_str():
		pass

	def update_create_staff_str():
		path = Path.joinpath(path).joinpath(Staff.csv)

		with open(path, "a", newline='') as file:

			writer = DictWriter(file)
			new_row_dict = Employee.getattributes()
			writer.writerow(new_row_dict)

	def update_create_airplane_str():
		path = Path.joinpath(path).joinpath(Airplanes.csv)
		with open(path, "a", newline='') as file:
			writer = DictWriter(file)
			new_row_dict = Airplane.getattributes()
			writer.writerow(new_row_dict)

	def update_create_dest_str():
		path = Path.joinpath(path).joinpath(Destinations.csv)
		with open(path, "a", newline='') as file:
			writer = DictWriter(file)
			new_row_dict = Destination.getattributes()
			writer.writerow(new_row_dict)

	def update_rtrip_str():
		path = Path.joinpath(path).joinpath(RoundTrips.csv)
		with open(path, "a", newline='') as file:
			writer = DictWriter(file)
			new_row_dict = Rtrip.getattributes()
			writer.writerow(new_row_dict)

