from database.database_layer import DBLayer
from model_classes import *
from csv import DictWriter
from pathlib import Path


######## VANTAR AÐ IMPLEMENTA SERIAL CODES I CSV FILES #######

class Create(DBLayer):
	new_data_str = ""
	create_staff_str = ""
	create_airplane_str = ""
	create_dest_str = ""
	create_rtrip_str = ""

	def create_staff(employee):
		path = DBLayer.path.joinpath("Staff.csv")

		with open(path, "a", newline='') as file:

			new_row_dict = employee.getattributes()
			fields = list(new_row_dict.keys())
			writer = DictWriter(file, fields)
			writer.writerow(new_row_dict)

	def create_airplane(airplane):
		path = DBLayer.path.joinpath("Airplanes.csv")
		with open(path, "a", newline='') as file:

			new_row_dict = airplane.getattributes()
			fields = list(new_row_dict.keys())

			writer = DictWriter(file, fields)
			writer.writerow(new_row_dict)

	def create_destination(destination):
		path = DBLayer.path.joinpath("Destinations.csv")
		with open(path, "a", newline='') as file:

			new_row_dict = destination.getattributes()
			fields = list(new_row_dict.keys())

			writer = DictWriter(file, fields)
			writer.writerow(new_row_dict)

	def create_rtrip(rtrip):
		path = DBLayer.path.joinpath("RoundTrips.csv")
		with open(path, "a", newline='') as file:

			new_row_dict = rtrip.getattributes()
			fields = list(new_row_dict.keys())
			writer = DictWriter(file, fields)

			writer.writerow(new_row_dict)

