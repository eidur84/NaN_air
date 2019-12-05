from BLLayer import BLLayer

class StaffHandler():


	def create_staff(DATA):
		if len(DATA) > 0:
			bool = Employee.set_name(DATA)

		if len(DATA) > 0:
			bool = Employee.set_ssn(DATA)

		if len(DATA) > 0:
			bool = Employee.set_address(DATA)

		if len(DATA) > 0:
			bool = Employee.set_landline(DATA)

		if len(DATA) > 0:
			bool = Employee.set_gsm(DATA)

		if len(DATA) > 0:
			bool = Employee.set_email(DATA)

		if len(DATA) > 0:
			bool = Employee.set_job(DATA)

		if len(DATA) > 0:
			bool = Employee.set_allowed_planes(DATA)

		return bool

	def license_check():
		if Employee.get_allowed_planes == '':
			return False
		else:
			return True

	def update_staff(DATA):
		pass

	def read_staff(DATA1, DATA2):
		#Þessu ætti að breyta í eitthvað sem BLLayer sér um því þessi klasi ætti ekki að tala við
		# Database layer
		DBLayer.generic_search('Staff.csv', DATA1, DATA2)

	def invalidate_staff(DATA):
		#Þessu ætti að breyta Invalidate klasin ætti ekki að vera í beinni samræðu við StaffHandler
		Invalidate.invalidate_staff(DATA)