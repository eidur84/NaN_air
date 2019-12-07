
from logic.logic_layer import BLLayer


class UILayer:

	def staff_creator():
		path = ["front_page", "staff_page", "new_staff_form"]
		print("Velkomin í NAMS\n\n")
		print("Vinsamlegast sláðu inn upplýsingar fyrir nýjan starfsmann:\n")

		data = [ ]
		form_fields = ["nafn", "kennitölu", "heimilisfang", "heimasíma", "farsíma", "tölvupóst", "starfsheiti", "leyfða flugvél"]
		index = 0
		# Ítra í gegnum listann og bið um uppl. fyrir hvert.

		while True:

			if index < len(form_fields):

				while True:
					field = input("Vinsamlegast sláðu inn " + form_fields[index] + ": ")
					# Set user input í data listann.
					data.append(field)

					# skoða hvort inputið sé rétt.
					valid = BLLayer.receive_data(path, data)  # KALLAR Í SET FÖLL MODEL KLASANS

					if valid:  # Held áfram í næsta form field ef virkar að stilla gildi attribute i model klasa.
						index += 1
						break

					else:  # Annars tek færsluna úr data listanum og reyni aftur.
						data.pop()
						print("Vinsamlegast farðu aftur yfir innslegnar upplýsingar")
			else:
				print("búið")
				break



