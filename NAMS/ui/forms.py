
from ui.user_interface import UILayer
from logic.logic_layer import BLLayer
from time import sleep

class Form(UILayer):

	def page(path):
		"""
		Page function for form page type.

		Fetches text from last file in given path, creates screen and checks if screen is large enough before printing.
		Recieves user input for each form.

		Args:
			path: list of screen names (route to current screen from front page)

		Returns user input along with path.
		"""

		screen = UILayer.frame()        # Create border and line list (screen)
		screen, line_number = UILayer.header(screen, path)      # Create header
		text = UILayer.get_text(path[-1] + ".txt")      # Recieve text for last page in given path

		form_fields = [row for row in text if len(row) > 0 and (row[0] == "|" or row[0] == "+")]
		form_prompts = [row for row in text[len(form_fields) + 1:] if len(row) > 0 and row[0] != " "]

		for line in form_fields:
			try:
				line_number += 1
				screen[line_number] = UILayer.aligner(screen[line_number], line, "center")

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				return StaticOptions.page(path)

		line_number += 1
		screen = UILayer.footer(screen, line_number)

		forms = []
		for line in form_prompts:

			screen[line_number] = UILayer.aligner(screen[line_number - len(form_prompts) - 3], line, "center")
			input_line = screen[line_number].rstrip("|+- ").rstrip("_")

			while True:
				# Print screen and move cursor
				for line in screen:
					print("\n" + line, end="")

				jump = len(screen) - (line_number + 1)

				action = UILayer.get_action(input_line, jump)
				forms.append(action)

				# Check given input using model class set methods
				valid = BLLayer.receive_data(path, forms)

				if valid:
					break

				else:
					forms.pop()
					screen[line_number] = UILayer.aligner(
						screen[line_number - len(form_prompts) - 3],
						"Vinsamlegast farðu aftur yfir innslegnar upplýsingar.",
						"center"
					)
					for line in screen:
						print("\n" + line, end="")
					sleep(1.5)


		return action, path
