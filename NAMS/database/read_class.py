from csv import DictReader
from database.database_layer import DBLayer


class Read(DBLayer):

	def read_staff(filter_column, key_word):
		staff_read = DBLayer.generic_search('Staff.csv', filter_column, key_word)
		return staff_read

	def read_airplane(filter_column, key_word):
		airplane_read = DBLayer.generic_search('Airplanes.csv', filter_column, key_word)
		return airplane_read

	def read_destination(filter_column, key_word):
		destination_read = DBLayer.generic_search('Destinations.csv', filter_column, key_word)
		return destination_read

'''
	def read_rtrip(rtrip, filter_column):
		rtrip_read = DBLayer.generic_search('RoundTrips.csv', filter_column, read_rtrip_str)
		return rtrip_read
'''