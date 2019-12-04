from csv import DictWriter

class Create:
    new_data_str = ""
    create_staff_str = ""
    create_airplane_str = ""
    create_dest_str = ""
    create_rtrip_str = ""
    path = ""

	def update_new_data_str():
	    pass

	def update_create_staff_str():
	    with open("Staff.csv", "a", newline='') as file:
    		writer = csv.DictWriter(file)
    		writer.writerow({"valdi" : ?, "ssn" : ? "staffID" : ?, "name" : ?, "job" : ?, "home" : ?, "landline" : ?, "gsm" : ?, "email" : ?, "license" : ?})



	def update_create_airplane_str():
	  	with open("Airplanse.csv", "a", newline='') as file:
    		writer = csv.DictWriter(file)
    		writer.writerow({"airplaneID" : ?, "manufacturer" : ? "name" : ?, "type" : ?, "seat_count" : ?, "valid" : ?,

	def update_create_dest_str():
	  	with open("Destination.csv", "a", newline='') as file:
    		writer = csv.DictWriter(file)
    		writer.writerow({"valid" : ?, "ID" : ? "country" : ?, "city" : ?, "airport" : ?, "flight_time" : ?, "distance" : ?, "contact_name" : ? "contact_phone" 

	def update_rtrip_str():
	  	with open("RoundTrips.csv", "a", newline='') as file:
    		writer = csv.DictWriter(file)
    		writer.writerow({"valid" : ?, "past" : ? "direction" : ?, "flightID" : ?, "departingFrom" : ?, "arrivingAT" : ?, "departure" : ?, "arrival" : ? "aircraft_name"