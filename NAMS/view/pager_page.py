# -*- coding: utf-8 -*-
from view.user_interface import UILayer
from controller.logic_layer import BLLayer
from model_classes.flightdate_class import FlightDate

class Pager:

	@staticmethod
	def page(state, display_data):
		"""
		Displays 5 lines of data from display_data and allows for paging forwards or backwards through data.

		Args:
			state: Current screen name
			display_data: Dictionary containing keys:
				"data": list of strings to print to screen.
				"end": length of data list
		"""

		index = 0
		display_data["action"] = ""
		display_data["instance_list"] = [ ]
		while True:
			screen = UILayer.frame()        # Create border and line list (screen)
			screen, line_number = UILayer.header(screen, state)      # Create header
			text = UILayer.get_text(state + ".txt")      # Recieve text for current screen

			page_size = display_data["page_size"]		# How many instances to display on each page

			if "rtrip" in display_data and display_data["rtrip"] is True:
				screen, line_number, screen_too_small = Pager.format_rtrips(screen, line_number, display_data, index)

			elif state == "non_busy_staff":
				screen, line_number, screen_too_small = Pager.format_staff(screen, line_number, display_data, index)

			elif state == "busy_staff":
				screen, line_number, screen_too_small = Pager.format_staff(screen, line_number, display_data, index, busy=True)

			elif state == "employee_schedule":
				screen, line_number, screen_too_small = Pager.format_schedule(screen, line_number, display_data, index)

			else:
				counter = 0

				for instance in display_data["data"][index * page_size: index * page_size + page_size]:
					try:

						line_number += 1

						# Calls display function for object and creates string
						# If assigning staff to a round trip
						if instance in display_data["instance_list"]:
							# Marks with asterix if staff member in crew for round trip
							line = str(counter + 1) + ") " + instance.short_display() + " *"

						else:
							line = str(counter + 1) + ") " + instance.short_display()

						screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
						counter += 1
						screen_too_small = False

					except IndexError:      # If screen is too small
						UILayer.error_screen()
						screen_too_small = True
						break

			if screen_too_small:
				continue

			for line in text[1:]:

				try:
					line_number += 1
					screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
					screen_too_small = False

				except IndexError:      # If screen is too small
					UILayer.error_screen()
					screen_too_small = True
					break

			if screen_too_small:
				continue

			screen = UILayer.footer(screen, line_number)

			# Print screen
			print("\n" * (len(screen) // 2))
			for line in screen:
				print("\n" + line, end="")

			# Format input line, move cursor and wait for input
			input_line = screen[line_number].rstrip("|+- ").rstrip("_")
			jump = len(screen) - (line_number + 1)
			action = UILayer.get_action(input_line, jump)

			# Page forwards
			if action.lower() == "n":
				if (index + 1) * page_size <= display_data["end"]:
					index += 1

			# Page backwards
			elif action.lower() == "p":
				if index > 0:
					index -= 1

			elif state == "employee_list" and action.lower() == "l":
				display_data["action"] = "non_busy_staff"
				return display_data

			elif state == "employee_list" and action.lower() == "u":
				display_data["action"] = "busy_staff"
				return display_data

			# Page by date on filtered staff list page
			elif (state == "non_busy_staff" or state == "busy_staff" or state == "employee_schedule") and action.lower() in ["l", "k", "0"]:
				if action.lower() == "l":
					if state == "employee_schedule":
						display_data["week"] += 1
					display_data["action"] = "next_date"
					return display_data

				elif action.lower() == "k":
					if state == "employee_schedule":
						display_data["week"] -= 1
					display_data["action"] = "prev_date"
					return display_data

				elif action == "0":
					display_data["action"] = "back"
					display_data["week"] = 0
					return display_data

			# Option to end choosing staff members for a given flight
			elif state == "staff_flight" and action.lower() == "l":
				return display_data

			# If instance is chosen from list shown by pager
			elif action in [ str(num) for num in range(page_size + 1) ]:  # Check if action within bounds of page size

				if action == "0":
					display_data["action"] = "back"
					return display_data

				# If user chooses an instance on current page
				else:
					try:

						# Make display_data["instance"] the chosen instance
						display_data["instance"] = display_data["data"][(index * page_size) + int(action) - 1]

						# If choosing a round trip, get instances of departure and returnflight
						if "rtrip" in display_data and display_data["rtrip"] == True:

							display_data["departure"] = display_data["instance"].get_departure()
							display_data["returnflight"] = display_data["instance"].get_returnflight()


						# If choosing staff members for a flight, add members to list of instances instead and continue loop
						elif state == "staff_flight":

							# Only add staff member if not already in list
							if display_data["instance"] not in display_data["instance_list"]:
								display_data["instance_list"].append(display_data["instance"])
							continue

						return display_data

					except IndexError:
						pass

	@staticmethod
	def format_rtrips(screen, line_number, display_data, index):
		""" Function for displaying roundtrips (departure and returning flight)."""
		counter = 0
		page_size = display_data["page_size"]
		screen_too_small = False
		for instance in display_data["data"][index * page_size: index * page_size + page_size]:
			try:

				line_number += 1

				# Calls display function for object and creates string
				line = str(counter + 1) + ") " + instance.display1()
				screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
				line_number += 1
				line = "   " + instance.display2()
				screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
				counter += 1

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				screen_too_small = True
				break

		return screen, line_number, screen_too_small

	@staticmethod
	def format_staff(screen, line_number, display_data, index, busy=False):
		""" Function for displaying filtered staff list (busy/non-busy)."""
		page_size = display_data["page_size"]
		line_number += 1
		line = FlightDate(display_data["datetime"]).short_display(with_time=False)
		screen_too_small = False
		screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
		if busy:
			for instance in display_data["data"][index * page_size: index * page_size + page_size]:
				try:

					line_number += 1
					ssn = instance.get_attributes()["ssn"]
					destination = display_data["destinations"][ssn].get_attributes()["arrivingAt"]
					# Calls display function for object and creates indented string
					line = "    " + instance.short_display() + "   Flug til: " + destination

					screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
					screen_too_small = False

				except IndexError:      # If screen is too small
					UILayer.error_screen()
					screen_too_small = True
					break

		else:
			for instance in display_data["data"][index * page_size: index * page_size + page_size]:
				try:

					line_number += 1

					# Calls display function for object and creates indented string
					line = "    " + instance.short_display()

					screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
					screen_too_small = False

				except IndexError:      # If screen is too small
					UILayer.error_screen()
					screen_too_small = True
					break

		return screen, line_number, screen_too_small


	@staticmethod
	def format_schedule(screen, line_number, display_data, index):

		page_size = display_data["page_size"]
		line_number += 1
		line = FlightDate(display_data["datetime"]).short_display(with_time=False)
		screen_too_small = False
		screen[line_number] = UILayer.aligner(screen[line_number], line, "left")
		for instance in display_data["data"][index * page_size: index * page_size + page_size]:
			try:

				line_number += 1

				# Calls display function for object and creates string
				line = "    " + instance.display1(show_manned=False) + "  ||  " + instance.display2(schedule_view=True)
				screen[line_number] = UILayer.aligner(screen[line_number], line, "left")

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				screen_too_small = True
				break

		return screen, line_number, screen_too_small




