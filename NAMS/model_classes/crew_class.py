class Crew:
	"""
	Model class containing staff members for a particular flight.
	"""

	def __init__(self):
		self.__flightID_str = ""		# vantar get/set methods
		self.__headpilot = ''
		self.__copilot = ''
		self.__headsteward = ''
		self.__otherstewards = []

	def set_headpilot(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__headpilot = name_str
			return True
		else:
			return False

	def get_headpilot(self):
		return self.__headpilot

	def set_copilot(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__copilot = name_str
			return True
		else:
			return False

	def get_copilot(self):
		return self.__copilot

	def set_headsteward(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__headsteward = name_str
			return True
		else:
			return False

	def get_headsteward(self):
		return self.__headsteward

	def set_stewards(self, name_str):
		if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
			self.__otherstewards.append(name_str)
			return True
		else:
			return False
