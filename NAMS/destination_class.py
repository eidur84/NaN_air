class Destination:
    """
    Model class for destinations.
    """
    def __init__(self):
        self.__valid_bool = False
        self.__country_name_str = ''
        self.__city_name_str = ''
        self.__airport_name_str = ''
        self.__distance_int = 0
        self.__flight_time_int = 0
        self.__contact_name_str = ''
        self.__contact_phone_str = ''

    #def set_valid(self):
        #if self.__country_name_str.isalpha() == True.......
            #self.__valid_bool = True
        #else:
            #self.__valid_bool = False

    def get_valid(self):
        return self.__valid_bool

    def set_country_name(self, name_str):
        if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
            self.__country_name_str = name_str
            return True
        else:
            return False

    def get_country_name(self):
        return self.__country_name_str

    def set_city_name(self, name_str):
        if name_str.replace(" ", "").isalpha() and len(name_str) <= 60:
            self.__city_name_str = name_str
            return True
        else:
            return False

    def get_city_name(self):
        return self.__city_name_str

    def set_airport_name(self, name_str):
        if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
            self.__airport_name_str = name_str
            return True
        else:
            return False

    def get_airport_name(self):
        return self.__airport_name_str

    def set_distance(self, km_count_int):
        if km_count_int.isdecimal():
            self.__distance_int = km_count_int
            return True
        else:
            return False

    def get_distance(self):
        return self.__distance_int

    def set_flight_time(self, min_count_int):
        if min_count_int.isdecimal():
            self.__flight_time_int = min_count_int
            return True
        else:
            return False

    def get_flight_time(self):
        return self.__flight_time_int

    def set_contact_name(self, name_str):
        if name_str.replace(' ', '').isalpha() and len(name_str) <= 60:
            self.__contact_name_str = name_str
            return True
        else:
            return False

    def get_contact_name(self):
        return self.__contact_name_str

    def set_contact_number(self, phone_str):
        if phone_str.isalpha():
            self.__contact_phone_str = phone_str
            return True
        else:
            return False

    def get_contact_number(self):
        return self.__contact_phone_str
