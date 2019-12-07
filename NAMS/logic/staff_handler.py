
from model_classes.employee_class import Employee


class StaffHandler:

	def create_staff(data):
		new_staff = Employee()

		if len(data) > 0:
			valid = new_staff.set_name(data[0])

		if len(data) > 1:
			valid = new_staff.set_ssn(data[1])

		if len(data) > 2:
			valid = new_staff.set_address(data[2])

		if len(data) > 3:
			valid = new_staff.set_landline(data[3])

		if len(data) > 4:
			valid = new_staff.set_gsm(data[4])

		if len(data) > 5:
			valid = new_staff.set_email(data[5])

		if len(data) > 6:
			valid = new_staff.set_job(data[6])

		if len(data) > 7:
			valid = new_staff.set_license(data[7])
			if valid:
				new_staff.set_valid()
				return new_staff

		return valid


	def update_staff(data):
		pass
