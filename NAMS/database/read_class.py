from csv import DictReader
from database.database_layer import DBLayer
from model_classes.employee_class import Employee
from model_classes.airplane_class import Airplane
from model_classes.destination_class import Destination



class Read(DBLayer):
	"""
	Class for read functionality of database layer. Searches files and returns dictionary of instances of given object.
	"""

	def read_staff(filter_column, key_word):
		staff_dict_list = DBLayer.generic_search('Staff.csv', filter_column, key_word)
		staff_dict = {}
		staff_dict_list = enumerate(staff_dict_list)
		for num, attribute_dict in staff_dict_list:
			staff_member = Employee()
			staff_member.initialize(attribute_dict)
			staff_dict["staff" + str(num)] = staff_member

		return staff_dict

	def read_airplane(filter_column, key_word):
		airplane_dict_list = DBLayer.generic_search('Airplanes.csv', filter_column, key_word)
		airplane_dict = {}
		airplane_dict_list = enumerate(airplane_dict_list)
		for num, attribute_dict in airplane_dict_list:
			airplane = Airplane()
			airplane.initialize(attribute_dict)
			airplane_dict["airplane" + str(num)] = airplane

		return airplane_dict

	def read_destination(filter_column, key_word):
		dest_dict_list = DBLayer.generic_search('Destinations.csv', filter_column, key_word)
		dest_dict = {}
		dest_dict_list = enumerate(dest_dict_list)
		for num, attribute_dict in dest_dict_list:
			destination = Destination()
			destination.initialize(attribute_dict)
			dest_dict["dest" + str(num)] = destination

		return dest_dict


	def read_rtrip(filter_column, key_word):
		rtrip_dict_list = DBLayer.generic_search('RoundTrips.csv', filter_column, key_word)
		
		return rtrip_dict_list
