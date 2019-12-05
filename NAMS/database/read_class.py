from csv import DictReader
from database.database_layer import DBLayer

class Read(DBLayer):
	read_staff_str = ""
	read_airplane_str = ""
	read_dest_str = ""
	read_rtrip_str = ""

	def update_read_staff_str(employee, filter_column, read_name_str):
		staff_read = DBLayer.generic_search('Staff.csv', filter_column, read_name_str)
		return staff_read

	def update_airplane_str(airplane, filter_column):
		airplane_read = DBLayer.generic_search('Airplanes.csv', filter_column, read_airplane_str)
		return airplane_read

	def update_read_dest_str(destination, filter_column):
		destination_read = DBLayer.generic_search('Destinations.csv', filter_column, read_dest_str)
		return destination_read

	def update_read_rtrip_str(rtrip, filter_column):
		rtrip_read = DBLayer.generic_search('RoundTrips.csv', filter_column, read_rtrip_str)
		return rtrip_read
