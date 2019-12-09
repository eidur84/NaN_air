# -*- coding: utf-8 -*-
from view.user_interface import UILayer
from controller.logic_layer import BLLayer

class Pager:

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
		while True:
			screen = UILayer.frame()        # Create border and line list (screen)
			screen, line_number = UILayer.header(screen, state)      # Create header
			text = UILayer.get_text(state + ".txt")      # Recieve text for current screen

			page_size = display_data["page_size"]
			if "rtrip" in display_data:
				screen, line_number, screen_too_small = Pager.format_rtrips(screen, line_number, display_data, index)

			else:
				counter = 0
				for instance in display_data["data"][index * page_size: index * page_size + page_size]:
					try:

						line_number += 1

						# Calls display function for object and creates string
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
			for line in screen:
				print("\n" + line, end="")

			# Format input line, move cursor and wait for input
			input_line = screen[line_number].rstrip("|+- ").rstrip("_")
			jump = len(screen) - (line_number + 1)
			action = UILayer.get_action(input_line, jump)

			if action.lower() == "n":
				if (index + 1) * page_size <= display_data["end"]:
					index += 1
			elif action.lower() == "p":
				if index > 0:
					index -= 1
			elif action in ["0", "1", "2", "3", "4", "5"]:
				if action == "0":
					display_data["action"] = "back"
					return display_data
				else:
					try:
						display_data["instance"] = display_data["data"][(index * page_size) + int(action) - 1]
						if "rtrip" in display_data:
							display_data["departure"] = display_data["instance"].get_departure()
							display_data["returnflight"] = display_data["instance"].get_returnflight()
						return display_data

					except IndexError:
						pass


	def format_rtrips(screen, line_number, display_data, index):
		counter = 0
		page_size = display_data["page_size"]
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
				screen_too_small = False

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				screen_too_small = True
				break

		return screen, line_number, screen_too_small






