from csv import DictReader
from database.DBLayer_class import DBLayer

class Read(DBLayer):
	read_staff_str = ""
	read_airplane_str = ""
	read_dest_str = ""
	read_rtrip_str = ""

	def update_read_staff_str():
		staff_read = DBLayer.generic_search('staff.csv', filter_column, read_staff_str)
		return staff_read

	def update_airplane_str():
		airplane_read = DBLayer.generic_search('Airplanes.csv', filter_column, read_airplane_str)
		return airplane_read

	def update_read_dest_str():
		destination_read = DBLayer.generic_search('Destinations.csv', filter_column, read_dest_str)
		return destination_read

	def update_read_rtrip_str():
		rtrip_read = DBLayer.generic_search('RoundTrips.csv', filter_column, read_rtrip_str)
		return rtrip_read
