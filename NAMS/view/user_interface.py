# -*- coding: utf-8 -*-
from time import localtime, strftime
from controller.logic_layer import BLLayer
from pathlib import Path

from model_classes.airplane_class import Airplane
from model_classes.departure_class import Departure
from model_classes.destination_class import Destination
from model_classes.employee_class import Employee



class UILayer:

	#–––––––––––––––––––––––#
	# MAIN PROGRAM LOOP	    #
	#–––––––––––––––––––––––#
	@staticmethod
	def main():
		"""
		NAMS main program loop.
		"path" is a list containing name of all screens en route to current screen.
		"state" is current screen name.
		Each page has a corresponding UI class view type (Pager, Form or StaticOptions)
		"""
		path = ["front_page"]
		form_data = {}
		display_data = {}
		while True:
			state = path[-1]
			page_type = UILayer.page_check(state)

			if page_type == "form":
				if state == "update_staff":
					form_data = display_data
				else:
					form_data = BLLayer.form_system(state, form_data)

				if state == "update_staff":
					old_dict = display_data["instance"].get_attributes()

				form_data = Form.page(state, form_data)

				# Go back
				if form_data["action"] == "back":
					path.pop()
					form_data["action"] = ""

				# Create instance with data from user input
				else:

					form_data["instance"] = BLLayer.form_input_check(state, form_data["instance"])

					form_input = form_data["instance"].get_attributes().values()
					if "Villa" not in form_input:

						if state == "update_staff":
							finished = BLLayer.update_row(old_dict, display_data["instance"])
						else:
							finished = BLLayer.create_row(state, form_data["instance"])

						# If user created a flight and wants to staff it immediately
						if form_data["action"] == "staff_flight":

							staff_data = BLLayer.paging_system("staff_flight")
							staff_data["rtrip"] = False
							staff_data = Pager.page("staff_flight", staff_data)

							if staff_data["action"] == "back":
								path.pop()

							else:
								finished = BLLayer.create_crew_members(form_data["instance"], staff_data["instance_list"])
						form_data = {}
						path.pop()


			elif page_type == "pager":
				display_data = BLLayer.paging_system(state)

				display_data = Pager.page(state, display_data)
				# Go back or other specific actions
				if "action" in display_data and display_data["action"] != "":
					if display_data["action"] == "back":
						path.pop()
						display_data["action"] = ""
						display_data["datetime"] = ""

					elif display_data["action"] == "non_busy_staff":
						path.append("non_busy_staff")
						display_data["action"] = ""
						display_data["datetime"] = ""

					elif display_data["action"] == "busy_staff":
						path.append("busy_staff")
						display_data["action"] = ""
						display_data["datetime"] = ""


				# If an instance is chosen from list
				else:
					# If instance is a round trip instance, convert "instance" to departure instance instead
					if "rtrip" in display_data and display_data["rtrip"] is True:
						display_data["instance"] = display_data["departure"]

					# Other object types
					else:
						old_dict = display_data["instance"].get_attributes()

					if state == "employee_list":
						path.append("staff_member")

					else:
						# Put user into form mode for editing instance
						display_data = Form.page(state, display_data)

						# Go back
						if display_data["action"] == "back":
							path.pop()
							display_data["action"] = ""

						# Update instance
						else:

							# If instance is a round trip call different update function
							if "rtrip" in display_data and display_data["rtrip"] is True:
								finished = BLLayer.update_rtrip(display_data["departure"], display_data["returnflight"])

								# If user wants to staff the given round trip
								if display_data["action"] == "staff_flight":

									staff_data = BLLayer.paging_system("staff_flight")
									staff_data["rtrip"] = False
									staff_data = Pager.page("staff_flight", staff_data)

									if staff_data["action"] == "back":
										path.pop()

									else:
										finished = BLLayer.update_crew(display_data["departure"], staff_data["instance_list"])

							else:
								finished = BLLayer.update_row(old_dict, display_data["instance"])

			elif page_type == "static":
				state = StaticOptions.page(state)

				if state == "back":
					path.pop()
					if len(path) == 0:
						break

				else:
					path.append(state)



	@staticmethod
	def page_check(state):
		"""
		Checks which ui class type should handle given page.
		"""
		if state in ["new_employee", "new_airplane", "new_dest", "new_rtrip", "update_staff"]:
			return "form"
		elif state in ["employee_list", "dest_list", "airplane_list", "rtrip_list", "busy_staff", "non_busy_staff", "employee_schedule"]:
			return "pager"
		else:
			return "static"

	#–––––––––––––––––––––––#
	# UI RELATED FUNCTIONS  #
	#–––––––––––––––––––––––#
	@staticmethod
	def terminal_size():
		# Returns width and height of terminal screen (on mac and linux).
		# Code gotten from https://www.w3resource.com/python-exercises/python-basic-exercise-56.php
		try:
			import fcntl, termios, struct
			th, tw, hp, wp = struct.unpack('HHHH',
					fcntl.ioctl(0, termios.TIOCGWINSZ,
					struct.pack('HHHH', 0, 0, 0, 0)))
		except ModuleNotFoundError:
			import os
			os.system('')
			os.system('mode con: cols=120 lines=40')
			tw = 120
			th = 40
		return tw - 2, th - 2

	@staticmethod
	def move(y, direction="A"):
		# Moves cursor by default up by y number of rows.
		# If direction is set to "B", cursor moves down.
		# Got idea for function from http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
		print(f"\u001b[{y + 1}{direction}")

	@staticmethod
	def frame():
		"""
		Creates list of lines on screen (screen) and creates the screen border.
		Returns screen (list of strings).
		"""
		width, height = UILayer.terminal_size()
		screen = [ ]
		screen.append("+" + "-" * width + "+")

		for _ in range(height):
			screen.append("|" + " " * width + "|")
		screen.append("+" + "-" * width + "+")

		return screen

	@staticmethod
	def get_text(filename):
		""" Fetches text for display on screen from files."""
		filename = Path.cwd().joinpath("view").joinpath("pages").joinpath(filename)
		f = open(filename, "r", encoding="utf-8")
		text = [ line.rstrip("\n") for line in f if line[0] != "#"]
		f.close()
		return text

	@staticmethod
	def error_screen():
		print("Window is too small, please make window larger.")
		action = input()

	@staticmethod
	def aligner(screen_line, text, align="left"):
		"""
		Function for aligning text, using slicing. Default alignment is left.
		"""
		if align == "center":
			center = (len(screen_line) - len(text)) // 2
			center_end = center + len(text)
			return screen_line[:center] + text + screen_line[center_end:]

		elif align == "right":
			start = len(screen_line) - len(text) - 2
			return screen_line[:start] + text + screen_line[start + len(text):]

		else:
			return screen_line[:2] + text + screen_line[len(text) + 2:]

	@staticmethod
	def header(screen, state):
		"""
		Inserts header into screen. Returns modified screen.

		Args:
			screen: list of lines (strings) displayed on page.
			state: name of current page.

		Returns screen and how many lines were printed.
		"""

		logo = UILayer.get_text("logo.txt")
		line_number = 1

		if len(screen) > 21:
			for line in logo:
				screen[line_number] = UILayer.aligner(screen[line_number], line, "center")
				line_number += 1
			line_number += 1

		header_text = UILayer.get_text(state + ".txt")
		date = strftime("%A %x", localtime())
		clock = strftime("%H:%M", localtime())

		screen[line_number] = UILayer.aligner(screen[line_number], header_text[0], "left")

		screen[line_number] = UILayer.aligner(screen[line_number], date, "right")
		line_number += 1

		screen[line_number] = UILayer.aligner(screen[line_number], clock, "right")
		line_number += 1

		if state == "front_page":
			screen[line_number] = UILayer.aligner(screen[line_number], "0) Loka NAMS kerfinu", "left")
		else:
			screen[line_number] = UILayer.aligner(screen[line_number], "0) Til baka", "left")

		line_number += 1

		screen[line_number] = "|" + "-" * (len(screen[line_number]) - 2) + "|"

		return screen, line_number + 1

	@staticmethod
	def footer(screen, line_number):
		""" Inserts footer into screen. Returns modified screen."""
		ascii_art = UILayer.get_text("ascii_art.txt")
		ascii_art.reverse()

		if len(screen) - line_number > len(ascii_art) + 1:  # Only insert footer if it fits on screen.
			line_nr = -2
			for line in ascii_art:
				screen[line_nr] = UILayer.aligner(screen[line_nr], line, "center")
				line_nr -= 1

		return screen

	@staticmethod
	def get_action(text, jump):
		""" Jumps up a given number of lines, recieves user input and returns it."""
		UILayer.move(jump)
		action = input(text)
		return action


from view.forms_page import Form
from view.static_page import StaticOptions
from view.pager_page import Pager






