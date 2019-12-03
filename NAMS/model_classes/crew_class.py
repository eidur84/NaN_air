class Crew:
    """
    Model class containing staff members for a particular flight
    """
    __valid_bool = False
    __flightID_int = ""	
    __headpilot_str = ''
    __copilot_str = ''
    __headsteward_str = ''
    __otherstewards_strlst = []

    def __init__(self, flightid, headpilot, copilot, headsteward, otherstewards):
        self.__flightID_int = flightid		# vantar get/set methods
        self.__headpilot_str = headpilot
        self.__copilot_str = copilot
        self.__headsteward_str = headsteward
        self.__otherstewards_strlst = []

    # !!Validation á klasabreytum fyrir database layerinn.. Vantar að klára!!

    # def set_valid(self):
    #    if self.__flightID_str.isalpha() == True and len(__flightID_str) == 0 and len(country_name_str) > 0 \
	#	and self.__city_name_str.isalpha() == True and len(city_name_str) <= 60 and len(city_name_str) > 0 \
	#	and self.__airport_name_str.isalpha() == True and len(airport_name_str) <= 60 and len(airport_name_str) > 0 \
	#	and isinstance(__distance_int,int) and __distance_int > 0 \
     #   and isinstance(__flight_time_int,int) and __flight_time_int > 0:	
     #   	self.__valid_bool = True
	#	else:
	#		self.__valid_bool = False   	


    def set_headpilot(self, name):
        if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
            self.__headpilot_str = name
            return True
        else:
            return False

    def get_headpilot(self):
        return self.__headpilot_str

    def set_copilot(self, name):
        if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
            self.__copilot_str = name
            return True
        else:
            return False

    def get_copilot(self):
        return self.__copilot_str

    def set_headsteward(self, name):
        if name.replace(' ', '').isalpha() and len(name) <= 60:
            self.__headsteward_str = name
            return True
        else:
            return False

    def get_headsteward(self):
        return self.__headsteward_str

    def set_stewards(self, name):
        if name.replace(' ', '').isalpha() and len(name) <= 60:
            self.__otherstewards.append(name)
            return True
        else:
            return False