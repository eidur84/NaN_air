

from database.database_layer import DBLayer


class BLLayer:
	"""
	Buisness logic layer
	"""

	def receive_data(path, data):
		if "staff_page" in path:
			if "new_staff_form" in path:
				exit_status = StaffHandler.create_staff(data)
				if type(exit_status) is bool:
					return exit_status
				else:
					valid = BLLayer.creator("staff", exit_status)
					return valid

	def creator(data_type, instance):
		valid = DBLayer.request_create(data_type, instance)
		return valid





# IMPORTS AT BOTTOM OF FILE TO PREVENT CIRCULAR IMPORTS (X imports Y and Y starts by importing X)
from logic.staff_handler import StaffHandler
from logic.airplane_handler import AirplaneHandler
from logic.destination_handler import DestHandler
from logic.rtrip_handler import RTripHandler
# See http://effbot.org/zone/import-confusion.htm#circular-imports for explanation
