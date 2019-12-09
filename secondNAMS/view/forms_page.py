# -*- coding: utf-8 -*-
from view.user_interface import UILayer
from controller.logic_layer import BLLayer

class Form(UILayer):

	def form_outline(screen, line_number, attribute_list):
		"""
		Creates frame for input fields and inserts filled fields into screen.
		Args:
			screen: list of lines to be printed on screen
			line_number: current line number (int)
			attribute_list: list of tuples (form name, form entry)
		"""

		frame_width = 40
		for key, attribute in attribute_list:
			if len(key) + len(str(attribute)) > frame_width:
				frame_width = len(key) + len(attribute)

		screen[line_number] = UILayer.aligner(screen[line_number], "+" + "-" * (frame_width - 2) + "+", "center")

		for key, attribute in attribute_list:
			try:
				line_number += 1

				if attribute == "" or attribute == 0:
					line = "| " + key + ": " + "_" * (frame_width - 6 - len(key)) + " |"
				else:
					line = "| " + key + ": " + attribute + " " * (frame_width - 6 - len(key) - len(attribute)) + " |"

				screen[line_number] = UILayer.aligner(screen[line_number], line, "center")
				screen_too_small = False

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				screen_too_small = True
				break

		line_number += 1
		screen[line_number] = UILayer.aligner(screen[line_number], "+" + "-" * (frame_width - 2) + "+", "center")

		return screen, line_number, screen_too_small



	def page(state, form_data):
		"""
		Page function for form page type.

		Fetches text from last file in given path, creates screen and checks if screen is large enough before printing.
		Recieves user input for each form.

		Args:
			state: Current screen name
			form_data: Dictionary. Key: "instance" Value: instance of given object

		Returns user input along with path.
		"""

		while True:
			screen = UILayer.frame()        # Create border and line list (screen)
			screen, line_number = UILayer.header(screen, state)      # Create header
			text = UILayer.get_text(state + ".txt")      # Recieve text for last page in given path

			form_fields = form_data["instance"].attribute_translation()  # Retrieves icelandic translations of form fields
			form_dict = form_data["instance"].get_attributes()  # Retrieve dict of attributes
			dict_keys = form_data["instance"].dict_keys()  # Retreive keys to attribute dictionary

			# Create frame for form fields
			screen, line_number, screen_too_small = Form.form_outline(screen, line_number, form_fields)

			if screen_too_small:
				continue


			line_number += 1
			screen = UILayer.footer(screen, line_number)


			index = 1
			for key, value in form_fields:
				print(key,value)
				translated_forms = form_data["instance"].attribute_translation()
				line_number -= len(form_fields) + 2
				screen, line_number, screen_too_small = Form.form_outline(screen, line_number, translated_forms)
				line_number += 1
				screen[line_number] = "|" + " " * (len(screen[line_number]) - 2) + "|"
				screen[line_number] = UILayer.aligner(screen[line_number], key + ": _", "center")
				input_line = screen[line_number].rstrip("|+- ").rstrip("_")


				# Print screen and move cursor
				for line in screen:
					print("\n" + line, end="")

				jump = len(screen) - (line_number + 1)
				action = UILayer.get_action(input_line, jump)

				if action.lower() == "q":
					form_data["action"] = "back"
					return form_data

				if action == "0" and key != "Klukkustund":
					form_data["action"] = "back"
					return form_data

				if action != "":
					print(dict_keys[index], action)
					form_dict[dict_keys[index]] = action

				index += 1
				form_data["instance"].__init__(form_dict)


				# Opportunity to change info
				if key == form_fields[-1][0]:

					# Automatically go back through form if ERROR in one of the fields
					if "ERROR" in form_dict.values():
						action = "2"
					else:
						translated_forms = form_data["instance"].attribute_translation()
						line_number -= len(form_fields) + 2
						screen, line_number, screen_too_small = Form.form_outline(screen, line_number, translated_forms)
						line_number += 1
						screen[line_number] = "|" + " " * (len(screen[line_number]) - 2) + "|"
						screen[line_number] = UILayer.aligner(screen[line_number], "Eru skráðar upplýsingar í lagi? 1) Já 2) Nei : _", "center")
						input_line = screen[line_number].rstrip("|+- ").rstrip("_")

						# Print screen and move cursor
						for line in screen:
							print("\n" + line, end="")

						jump = len(screen) - (line_number + 1)
						action = UILayer.get_action(input_line, jump)

			if action == "2":
				continue

			form_data["instance"].set_valid()
			form_data["action"] = "create"
			return form_data







