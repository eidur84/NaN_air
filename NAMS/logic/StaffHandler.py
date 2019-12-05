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
		pass

	def update_staff():
		pass

	def read_staff():
		pass

	def invalidate_staff():
		pass