class Rtrip():
    def __init__(self):
        self.__valid_bool = True 
        self.__dest_str = ""
        self.__rtime_int = ""
        self.__passenger_count_int = ""
        self.__start_time_str = ""
        self.__return_time_str = ""
        self.__start_date_str = ""
        self.__return_date_str = ""

    def valid_bool(self, valid_bool):
        pass

    def set_dest_str(self, dest_str):
        if dest_str.replace(" ","").isalpha():
            self.__dest_str = dest_str
            return True
        else:
            return False
    
    def get_dest_str(dest_str):
        return self.__get_dest_str
    
    def set_rtime_int(self, rtime_int):
        if rtime_int.isdecimal:
            self.__rtime_int = rtime_int:
            return True
        else:
            return False

    def get_rtime_int(self):
        return self.__rtime_int

    def set_passenger_count_int(self, passenger_count_int):
        if passenger_count_int.isdecimal:
            self.__passenger_count_int = passenger_count_in:
            return True
        else:
            return False

    def get_passenger_count_int(self):
        return self.__passenger_count_int

    def set_start_time_str(self, start_time_str):
        if start_time_str.replace(" ","").isalpha():
            self.__start_time_str = start_time_str:
            return True
        else:
            return False

    def get_start_time_str(self):
        return __start_time_str
    
    def set_return_time_str(self, return_time_str):
        if return_time_str.replace(" ","").isalpha():
            self.__return_time_str = return_time_str:
            return True
        else:
            return False

    def get_return_time_str(self):
        return self.__return_time_str
        
    def set_start_date_str(self, start_date_str):
        if start_date_str.replace(" ","").isalpha():
            self.__start_date_str = start_date_str:
            return True
        else:
            return False
    
    def get_start_date_str(self):
        return self.__start_date_str

    def set_return_date_str(self, return_date_str):
        if return_date_str.replace(" ","").isalpha():
            self.__return_date_str = return_date_str:
            return True
        else:
            return False
        
    def get_return_date_str(self):
        return self.__return_date_str

class Airplane():
    self.__seat_count_int = ""
    self.__type_str = ""
    self.__manuf_str = ""

    def set_seat_count_int(self, seat_count_int):
        if seat_count_int.isdecimal:
            self.__seat_count_int = seat_count_int:
            return True
        else:
            return False

    def get_seat_count_int(self):
        return self.__seat_count_int

    def set_type_str(self, type_str):
        if type_str.replace(" ","").isalpha():
            self.__type_str = type_str
            return True
        else:
            return False
    
    def get_type_str(self):
        return self._type_str

    def set_manuf_str(self, manuf_str):
        if manuf_str.replace(" ","").isalpha():
            self.__manuf_str = manuf_str
            return True
        else:
            return False

    def get_manuf_str(self):
        return self.__manuf_str