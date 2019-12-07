
from ui.user_interface import UILayer


class StaticOptions(UILayer):

	def page(path=["front_page"]):
		"""
		Page function for static page type.

		Fetches text from last file in given path, creates screen and checks if screen is large enough before printing.
		Recieves user input.

		Args:
			path: list of screen names (route to current screen from front page)

		Returns user input along with path.
		"""

		screen = UILayer.frame()        # Create border and line list (screen)
		screen, line_number = UILayer.header(screen, path)      # Create header
		text = UILayer.get_text(path[-1] + ".txt")      # Recieve text for last page in given path

		for line in text[1:]:

			try:
				line_number += 1
				screen[line_number] = UILayer.aligner(screen[line_number], line)

			except IndexError:      # If screen is too small
				UILayer.error_screen()
				return StaticOptions.page(path)

		screen = UILayer.footer(screen, line_number)

		# Print screen
		for line in screen:
			print("\n" + line, end="")

		# Format input line
		input_line = screen[line_number].rstrip("|+- ").rstrip("_")
		jump = len(screen) - (line_number + 1)
		action = UILayer.get_action(input_line, jump)

		return action, path
