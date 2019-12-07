# -*- coding: utf-8 -*-
from view.user_interface import UILayer


class StaticOptions(UILayer):

	def page(state):
		"""
		Page function for static page type.

		Fetches text from a page's corresponding txt file, creates screen
		and checks if screen is large enough before printing.
		Recieves user input.

		Args:
			state: Current screen name.

		Returns user input along with path.
		"""
		while True:
			screen = UILayer.frame()        # Create border and line list (screen)
			screen, line_number = UILayer.header(screen, state)      # Create header
			text = UILayer.get_text(state + ".txt")      # Recieve text for current screen

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

			# Go back a page
			if action == "0":
				return "back"

			# Action checks for each static page in program
			if state == "front_page":
				if action == "1":
					return "employee_page"
				elif action == "2":
					return "rtrip_page"
				elif action == "3":
					return "dest_page"
				elif action == "4":
					return "airplane_page"

			elif state == "employee_page":
				if action == "1":
					return "new_employee"
				elif action == "2":
					return "employee_list"

			elif state == "rtrip_page":
				if action == "1":
					return "new_rtrip"
				elif action == "2":
					return "rtrip_list"

			elif state == "dest_page":
				if action == "1":
					return "new_dest"
				elif action == "2":
					return "dest_list"

			elif state == "airplane_page":
				if action == "1":
					return "new_airplane"
				elif action == "2":
					return "airplane_list"

			elif state == "employee_info":
				if action == "1":
					return "employee_schedule"
				elif action == "2":
					return "update_employee"




