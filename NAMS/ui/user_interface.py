
import sys

from time import localtime, strftime
from logic.logic_layer import BLLayer


class UILayer:

	def terminal_size():
		# Returns width and height of terminal screen.
		# Code gotten from https://www.w3resource.com/python-exercises/python-basic-exercise-56.php
		try:
			import fcntl, termios, struct
			th, tw, hp, wp = struct.unpack('HHHH',
					fcntl.ioctl(0, termios.TIOCGWINSZ,
					struct.pack('HHHH', 0, 0, 0, 0)))
		except ModuleNotFoundError:
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

	def get_text(filename):
		""" Fetches text for display on screen from files."""
		f = open(f'ui/pages/{filename}', "r")
		text = [ line.rstrip("\n") for line in f if line[0] != "#"]
		f.close()
		return text

	def error_screen():
		print("Window is too small, please make window larger.")
		action = input()

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

	def header(screen, path):
		"""
		Inserts header into screen. Returns modified screen.

		Args:
			screen: list of lines (strings) displayed on page.
			path: list of pages, route to current screen from front page.

		Returns screen and how many lines were printed.
		"""

		logo = UILayer.get_text("logo.txt")
		line_number = 1

		if len(screen) > 21:
			for line in logo:
				screen[line_number] = UILayer.aligner(screen[line_number], line, "center")
				line_number += 1
			line_number += 1

		header_text = UILayer.get_text(path[-1] + ".txt")
		date = strftime("%A %x", localtime())
		clock = strftime("%H:%M", localtime())

		screen[line_number] = UILayer.aligner(screen[line_number], header_text[0], "left")

		screen[line_number] = UILayer.aligner(screen[line_number], date, "right")
		line_number += 1

		screen[line_number] = UILayer.aligner(screen[line_number], clock, "right")
		line_number += 1

		if path == ["front_page"]:
			screen[line_number] = UILayer.aligner(screen[line_number], "0) Loka NAMS kerfinu", "left")
		else:
			screen[line_number] = UILayer.aligner(screen[line_number], "0) Til baka", "left")

		line_number += 1

		screen[line_number] = "|" + "-" * (len(screen[line_number]) - 2) + "|"

		return screen, line_number + 1

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


	def get_action(text, jump):
		""" Jumps up a given number of lines, recieves user input and returns it."""
		UILayer.move(jump)
		action = input(text)
		return action


	def page_check(path):
		if path[-1] in ["new_employee", "new_airplane", "new_destination", "new_rtrip"]:
			
			#Forms.page(path)
		elif path[-1] in ["staff_list", "destination_list", "airplane_list", "rtrip_list"]:
			#Pager.page(path)
		else:
			#StaticOptions.page(path)

	def main():
		path = ["front_page"]
		while True:
			page_type = page_check(path)









