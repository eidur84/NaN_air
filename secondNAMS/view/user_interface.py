# -*- coding: utf-8 -*-
from time import localtime, strftime
from controller.logic_layer import BLLayer

from model_classes.airplane_class import Airplane
from model_classes.departure_class import Departure
from model_classes.destination_class import Destination
from model_classes.employee_class import Employee



class UILayer:

	#–––––––––––––––––––––––#
	# MAIN PROGRAM LOOP	    #
	#–––––––––––––––––––––––#

	def main():
		"""
		NAMS main program loop.
		"path" is a list containing name of all screens en route to current screen.
		"state" is current screen name.
		Each page has a corresponding UI class view type (Pager, Form or StaticOptions)
		"""
		path = ["front_page"]
		while True:
			state = path[-1]
			page_type = UILayer.page_check(state)

			if page_type == "form":
				form_data = BLLayer.form_system(state)

				form_data = Form.page(state, form_data)

				if form_data["action"] == "back":
					path.pop()

				else:
					finished = BLLayer.create_row(state, form_data["instance"])

					path.pop()

			elif page_type == "pager":
				display_data = BLLayer.paging_system(state)

				action = Pager.page(state, display_data)

				if action == "back":
					path.pop()
				else:
					instance = action
					old_dict = instance.get_attributes()
					new_instance = Form.page(state, instance)
					finished = BLLayer.update_row(old_dict, new_instance)


			elif page_type == "static":
				state = StaticOptions.page(state)

				if state == "back":
					path.pop()
					if len(path) == 0:
						break

				else:
					path.append(state)




	def page_check(state: str) -> str:
		"""
		Checks which ui class type should handle given page.
		"""
		if state in ["new_employee", "new_airplane", "new_dest", "new_rtrip"]:
			return "form"
		elif state in ["employee_list", "dest_list", "airplane_list", "rtrip_list"]:
			return "pager"
		else:
			return "static"

	#–––––––––––––––––––––––#
	# UI RELATED FUNCTIONS  #
	#–––––––––––––––––––––––#

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

	def move(y, direction="A"):
		# Moves cursor by default up by y number of rows.
		# If direction is set to "B", cursor moves down.
		# Got idea for function from http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
		print(f"\u001b[{y + 1}{direction}")


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

	def get_text(filename) -> list:
		""" Fetches text for display on screen from files."""
		f = open(f'view/pages/{filename}', "r", encoding="utf-8")
		text = [ line.rstrip("\n") for line in f if line[0] != "#"]
		f.close()
		return text

	def error_screen():
		print("Window is too small, please make window larger.")
		action = input()

	def aligner(screen_line, text, align="left") -> str:
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

	def footer(screen, line_number) -> list:
		""" Inserts footer into screen. Returns modified screen."""
		ascii_art = UILayer.get_text("ascii_art.txt")
		ascii_art.reverse()

		if len(screen) - line_number > len(ascii_art) + 1:  # Only insert footer if it fits on screen.
			line_nr = -2
			for line in ascii_art:
				screen[line_nr] = UILayer.aligner(screen[line_nr], line, "center")
				line_nr -= 1

		return screen


	def get_action(text, jump) -> str:
		""" Jumps up a given number of lines, recieves user input and returns it."""
		UILayer.move(jump)
		action = input(text)
		return action


from view.forms_page import Form
from view.static_page import StaticOptions
from view.pager_page import Pager






