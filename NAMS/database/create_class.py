
from csv import DictWriter, DictWriter
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
			writer.writerow({"airplaneID" : ?, "manufacturer" : ? "name" : ?, "type" : ?, "seat_count" : ?, "valid" : ?,})

	def update_create_dest_str():
		path = Path.joinpath(path).joinpath(Destinations.csv)
		with open(path, "a", newline='') as file:
			writer = DictWriter(file)
			writer.writerow({"valid" : ?, "ID" : ? "country" : ?, "city" : ?, "airport" : ?, "flight_time" : ?, "distance" : ?, "contact_name" : ? "contact_phone" })

	def update_rtrip_str():
		path = Path.joinpath(path).joinpath(RoundTrips.csv)
		with open(path, "a", newline='') as file:
			writer = DictWriter(file)
			writer.writerow({"valid" : ?, "past" : ? "direction" : ?, "flightID" : ?, "departingFrom" : ?, "arrivingAT" : ?, "departure" : ?, "arrival" : ? "aircraft_name"

