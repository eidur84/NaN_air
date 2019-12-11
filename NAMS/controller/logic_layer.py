# -*- coding: utf-8 -*-
import datetime as dt

from database.read_class import Read
from database.create_class import Create
from database.update_class import Update
from database.database_layer import DBLayer

from model_classes.airplane_class import Airplane
from model_classes.departure_class import Departure
from model_classes.destination_class import Destination
from model_classes.employee_class import Employee
from model_classes.returnflight_class import ReturnFlight
from model_classes.crew_class import Crew
from model_classes.rtrip_class import RTrip
from model_classes.flightdate_class import FlightDate


class BLLayer:
	"""
	Business logic layer, handles communcaction betwwen UI and DB layers and does calculations relating to time.
	"""
	@staticmethod
	def paging_system(state, display_data={}):
		"""
		Creates a key,value pair in display_Data dict, key: "data", value: list of object instances.
		"""

		if state == "dest_list":
			data = Read.read_dest("valid", "True")

		elif state == "staff_list":
			data = Read.read_staff("valid", "True")

		elif state == "airplane_list":
			data = Read.read_airplane("valid", "True")

		elif state == "employee_list":
			data = Read.read_staff("valid", "True")

		elif state == "non_busy_staff":
			display_data, data = BLLayer.filter_busy_staff(display_data)

		elif state == "busy_staff":
			display_data, data = BLLayer.filter_busy_staff(display_data, busy=True)

		elif state == "rtrip_list":
			attribute_dict_list = Read.read_rtrip("valid", "True")
			data = BLLayer.create_rtrip_list(attribute_dict_list)

		elif state == "employee_schedule":
			display_data = BLLayer.create_schedule(display_data)
			display_data["page_size"] = len(display_data["data"])
			display_data["end"] = len(display_data["data"])
			return display_data


		display_data["data"] = data

		# If showing dates in pager show in weeks
		if state == "date_list":
			display_data["page_size"] = 7
			display_data["rtrip"] = False

		# Show only 4 round trips in pager
		elif state == "rtrip_list":
			display_data["page_size"] = 4
			display_data["rtrip"] = True

		# Default number of entries in pager is 5
		else:
			display_data["page_size"] = 5
			display_data["rtrip"] = False

		display_data["end"] = len(display_data["data"])

		return display_data


	@staticmethod
	def show_available_staff(form_data):
		""" Returns list of staff not flying on departure date."""

		dep_str = form_data["instance"].get_attributes()["departure"][0:10]
		departure_list = Read.departures_on_date(dep_str)

		flightID_list = [ ]
		for departure in departure_list:
			flightID_list.append(departure.get_attributes()["flightID"])

		busy_ssn_list = []
		for flightID in flightID_list:
			crew_list = Read.flight_crew(flightID)

			for crew_row in crew_list:
				busy_ssn_list.append(crew_row.get_attributes()["ssn"])

		all_staff = Read.read_staff("valid", "True")
		data = []
		for employee in all_staff:
			if employee.get_attributes()["ssn"] not in busy_ssn_list:
				data.append(employee)

		form_data["data"] = data
		form_data["page_size"] = 7
		form_data["rtrip"] = False
		return form_data


	@staticmethod
	def create_schedule(display_data):
		"""
		Creates one week from last monday, finds flights in week
		Returns list of flights if an employees ssn is found to match in Crew csv.
		"""

		display_data["data"] = [ ]
		if "week" in display_data:
			last_monday = dt.datetime.today().date() + display_data["week"] * dt.timedelta(days=7)
		else:
			last_monday = dt.datetime.today().date()
			display_data["week"] = 0

		while last_monday.weekday() != 0:
			last_monday = last_monday - dt.timedelta(days=1)
		current_week = [ ]
		week_day = last_monday

		# Get YYYY-MM-DD strings for each day in week, starting on last monday
		for _ in range(7):
			current_week.append(week_day.isoformat()[0:10])
			week_day = week_day + dt.timedelta(days=1)

		# Find flights on each day in given week, add to week_flights list
		week_flights = [ ]
		for date in current_week:
			departures = Read.departures_on_date(date)
			week_flights.append(departures)

		# If employee's ssn matches one found in crew for a departure, add departure and returning flight to employee's schedule
		staff_schedule = [ ]
		for departure_list in week_flights:
			for departure in departure_list:
				crew_row_list = Read.flight_crew(departure.get_attributes()["flightID"])

				for crew_row in crew_row_list:
					ssn = crew_row.get_attributes()["ssn"]

					if ssn == display_data["instance"].get_attributes()["ssn"]:
						returnflight = BLLayer.create_returnflight(departure, instant_write=False, make_serial=False)
						rtrip = RTrip(departure, returnflight)
						staff_schedule.append(rtrip)

		display_data["data"] = staff_schedule
		display_data["datetime"] = last_monday
		display_data["week_end"] = week_day
		return display_data



	@staticmethod
	def filter_busy_staff(display_data, busy=False):

		# If no date set, use today as starting point
		if display_data["datetime"] == "":
			today = dt.datetime.today()
			display_data["datetime"] = dt.datetime(today.year, today.month, today.day)

		else:
			if display_data["action"] == "next_date":
				display_data["datetime"] = display_data["datetime"] + dt.timedelta(days=1)
				display_data["action"] = ""

			elif display_data["action"] == "prev_date":
				display_data["datetime"] = display_data["datetime"] - dt.timedelta(days=1)
				display_data["action"] = ""

		if busy:
			display_data["destinations"] = {}

		departure_list = Read.departures_on_date(display_data["datetime"].isoformat()[0:10])
		ssn_list = [ ]
		for departure in departure_list:
			crew_list = Read.flight_crew(departure.get_attributes()["flightID"])

			for crew in crew_list:
				ssn_list.append(crew.get_attributes()["ssn"])

				if busy:
					key = crew.get_attributes()["ssn"]
					display_data["destinations"][key] = departure

		read_data = Read.read_staff("valid", "True")
		data = [ ]
		if not busy:

			for employee in read_data:

				if employee.get_attributes()["ssn"] not in ssn_list:
					data.append(employee)

		else:
			for employee in read_data:

				if employee.get_attributes()["ssn"] in ssn_list:
					data.append(employee)

		return display_data, data


	@staticmethod
	def form_input_check(state, instance):
		"""
		Checks if primary keys in each new form are unique.
		Also checks if other fields (such as airplane license) correspond with data in database (such as airplane names).
		"""
		attribute_dict = instance.get_attributes()
		if state == "new_employee":

			ssn_list = DBLayer.generic_search("Staff.csv", "valid", "True", result_column="ssn")
			if attribute_dict["ssn"] in ssn_list:
				attribute_dict["ssn"] = "Villa"

			airplane_names = DBLayer.generic_search("Airplanes.csv", "valid", "True", result_column="name")
			if attribute_dict["license"] not in airplane_names:
				attribute_dict["license"] = "Villa"

		elif state == "new_airplane":
			airplane_names = DBLayer.generic_search("Airplanes.csv", "valid", "True", result_column="name")
			if attribute_dict["name"] in airplane_names:
				attribute_dict["name"] = "Villa"

		elif state == "new_dest":
			dest_id_list = DBLayer.generic_search("Destinations.csv", "valid", "True", result_column="ID")
			if attribute_dict["ID"] in dest_id_list:
				attribute_dict["ID"] = "Villa"

		elif state == "new_rtrip":
			dest_id_list = DBLayer.generic_search("Destinations.csv", "valid", "True", result_column="ID")
			if attribute_dict["arrivingAt"] not in dest_id_list or attribute_dict["arrivingAt"] == "KEF":
				attribute_dict["arrivingAt"] = "Villa"

			airplane_names = DBLayer.generic_search("Airplanes.csv", "valid", "True", result_column="name")
			if attribute_dict["aircraft_name"] not in airplane_names:
				attribute_dict["aircraft_name"] = "Villa"

			departure = dt.datetime.strptime(attribute_dict["departure"], "%Y-%m-%dT%H:%M:%S")

			runway_empty = BLLayer.runway_check(departure)
			if not runway_empty:
				attribute_dict["departure"] = "Villa"

		instance.__init__(attribute_dict)
		return instance


	@staticmethod
	def runway_check(new_dep_time):
		""" Checks if new planned departure takes off within 10 minutes of another departure."""
		dep_str = new_dep_time.isoformat()[0:10]
		same_day_dep_list = Read.departures_on_date(dep_str)
		runway_empty = True

		for departure in same_day_dep_list:
			old_dep_time = dt.datetime.strptime(departure.get_attributes()["departure"], "%Y-%m-%dT%H:%M:%S")
			if old_dep_time - new_dep_time < dt.timedelta(minutes=10) or new_dep_time - old_dep_time < dt.timedelta(minutes=10):
				runway_empty = False

		return runway_empty


	@staticmethod
	def create_rtrip_list(attribute_dict_list):
		"""
		Creates list of flights for Pager, marks departing flight as manned or unmanned and returns list.
		"""
		rtrip_list = [ ]
		count = 0
		for attribute_dict in attribute_dict_list:

			if attribute_dict["direction"] == "outbound":
				departure = Departure(attribute_dict, from_csv=True)

				manned_status = False
				head_pilot = False
				assistant_pilot = False
				head_steward = False

				crew = Read.flight_crew(attribute_dict["flightID"])

				for member in crew:

					rank = member.get_rank()
					if rank == "Yfirflugmaður":
						head_pilot = True
					elif rank == "Aðstoðarflugmaður":
						assistant_pilot = True
					elif rank == "Yfirflugþjónn":
						head_steward = True

					manned_status = head_pilot and assistant_pilot and head_steward
					if manned_status:
						break

				departure.set_manned(manned_status)
				count += 1
			elif attribute_dict["direction"] == "inbound":
				returnflight = ReturnFlight(attribute_dict)
				count += 1

			# Collects two rows, creates Departure and ReturnFlight instances in order
			# Creates RTrip instance containing the two connected instances
			if count == 2:
				rtrip = RTrip(departure, returnflight)
				count = 0
				rtrip_list.append(rtrip)

		return rtrip_list


	@staticmethod
	def create_crew_members(departure, employee_list, instant_write = True):
		"""
		Creates crew info for crew csv file.
		Creates an instance of Crew and, if instant_write is set to True, sends to Create for writing into csv file.
		Else returns list of crew rows for csv file.
		"""

		flightID = departure.get_attributes()["flightID"]

		head_pilot_assigned = False
		head_steward_assigned = False

		crew_list = [ ]
		for employee in employee_list:
			employee_dict = employee.get_attributes()
			employee_ssn = employee_dict["ssn"]
			employee_role = employee_dict["job"]

			# Initialize empty attribute dict for crew row
			crew_dict = {}
			crew_dict["flightID"] = flightID
			crew_dict["ssn"] = employee_ssn

			if employee_role == "Flugmaður":

				crew_dict["role"] = employee_role

				# If head pilot not assigned
				if not head_pilot_assigned:
					# Assign first pilot in list as head pilot
					crew_dict["rank"] = "Yfirflugmaður"
					head_pilot_assigned = True

				# If flight already has a head pilot
				else:
					# Other pilots in list become assistant pilots
					crew_dict["rank"] = "Aðstoðarflugmaður"

			elif employee_role == "Flugþjónn":

				crew_dict["role"] = employee_role

				# Assign first steward in list as head steward
				if not head_steward_assigned:
					crew_dict["rank"] = "Yfirflugþjónn"
					head_steward_assigned = True

				else:
					# Other stewards
					crew_dict["rank"] = "Flugþjónn"
			else:
				crew_dict["role"] = "Villa"
				crew_dict["rank"] = "Villa"


			crew_row = Crew(crew_dict)
			if instant_write:
				finished = Create.create_crew(crew_row)
			else:
				crew_list.append(crew_row)

		if instant_write:
			return finished
		else:
			return crew_list


	@staticmethod
	def update_crew(departure, employee_list):
		crew_list = BLLayer.create_crew_members(departure, employee_list, instant_write=False)

		# ** Remove selected employees from other flights on same day **

		dep_str = departure.get_attributes()["departure"][0:10]

		# Get flights on same day
		departures_on_date = Read.departures_on_date(dep_str)

		# Get ssns for all busy employees on given date and corresponding flightID
		busy_ssn_list = [ ]
		for departure in departures_on_date:

			flightID = departure.get_attributes()["flightID"]
			crew = Read.flight_crew(flightID)

			for member in crew:
				busy_ssn_list.append(member.get_attributes()["ssn"])
				busy_ssn_list.append(member.get_attributes()["flightID"])

		# Get employees which have been selected to man current departure and are also assigned another flight on same day
		busy_employees = [ ]
		for employee in employee_list:
			ssn = employee.get_attributes()["ssn"]

			if ssn in busy_ssn_list:
				flightID = busy_ssn_list[busy_ssn_list.index(ssn) + 1]

				employee_id_tuple = (employee, flightID)

				busy_employees.append(employee_id_tuple)

		# Function changes old flight assignment validity to False
		bool1 = DBLayer.invalidate_crew_members(busy_employees)

		# Replace crew for the current departure instance
		bool2 = Update.replace_crew(departure, crew_list)
		finished = bool1 and bool2

		return finished


	@staticmethod
	def update_rtrip(departure, returnflight):
		returnflight = BLLayer.create_returnflight(departure, instant_write=False, make_serial=False)
		finished = Update.replace_rtrip_row(departure, returnflight)
		return finished


	@staticmethod
	def update_row(old_attributes, new_instance):
		finished = Update.replace_row(old_attributes, new_instance)
		return finished


	@staticmethod
	def create_row(state, new_instance):
		""" Makes DBLayer add row to a file."""
		if state == "new_dest":
			finished = Create.append_db_row("Destinations.csv", new_instance)
		elif state == "new_employee":
			finished = Create.append_db_row("Staff.csv", new_instance)
		elif state == "new_airplane":
			finished = Create.append_db_row("Airplanes.csv", new_instance)
		elif state == "new_rtrip":
			finished = BLLayer.create_returnflight(new_instance, instant_write=True, make_serial=True)

		return finished


	@staticmethod
	def form_system(state, form_data={}):
		""" Creates empty instance for Form page."""
		if form_data == {}:
			if state == "new_dest":
				form_data["instance"] = Destination()
			elif state == "new_employee":
				form_data["instance"] = Employee()
			elif state == "new_rtrip":
				form_data["instance"] = Departure()
			elif state == "new_airplane":
				form_data["instance"] = Airplane()

		return form_data


	@staticmethod
	def create_returnflight(departure, instant_write=True, make_serial=True):
		"""
		Creates an instance of ReturnFlight from a Departure instance.
		Args:
			departure: instance of Departure.
			instant_write: boolean, if True write to csv file and return boolean, else return ReturnFlight instance.
			make_serial: boolean, if True create new serial for instances, else don't create new serial.
		"""

		attribute_dict = departure.get_attributes()

		# Get destination ID
		dest = attribute_dict["arrivingAt"]

		# Flight time in minutes (int)
		flight_time = DBLayer.generic_search("Destinations.csv", "ID", dest, "flight_time")
		flight_time = int(flight_time[0])

		if make_serial:
			# Find last serial in csv file and increment
			serial = int(DBLayer.generic_search("RoundTrips.csv", "valid", "True", "flightID")[-1])
			attribute_dict["flightID"] = serial + 1

		# Get departure time (iso format string)
		departure_time = attribute_dict["departure"]

		# Parse iso format string and add flight time minutes
		departure_time = dt.datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S")
		arrival_time = departure_time + dt.timedelta(minutes = flight_time)
		attribute_dict["arrival"] = arrival_time.isoformat()

		departure.__init__(attribute_dict)

		# Prepare attribute dict for ReturnFlight class
		# Switch ID for departingFrom and ArrivingAt
		attribute_dict["departingFrom"] = attribute_dict["arrivingAt"]
		attribute_dict["arrivingAt"] = "KEF"

		# Add 1 hour wait time
		departure_time = arrival_time + dt.timedelta(hours=1)
		attribute_dict["departure"] = departure_time.isoformat()

		# Increment serial
		attribute_dict["flightID"] = str(int(attribute_dict["flightID"]) + 1)

		# Calculate arrival time back to KEF
		arrival_time = departure_time + dt.timedelta(minutes = flight_time)
		attribute_dict["arrival"] = arrival_time.isoformat()


		ret_flight = ReturnFlight(attribute_dict)

		if instant_write:
			finished = Create.create_rtrip(departure, ret_flight)
			return finished
		else:
			return ret_flight

