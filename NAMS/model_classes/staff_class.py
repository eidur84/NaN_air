class Staff:

    # Myndum við geyma þennan klasa í DB layernum og fylla hann þegar forritið er keyrt?

    def __init__(self):
        self.__pilot_list = []
        self.__steward_list = []

    def add_pilot(self, name_str):
        if name_str.remove(' ', '').isalpha():
            self.__pilot_list.append(name_str)
            return True
        else:
            return False

    def get_pilot_list(self):
        return self.__pilot_list

    def add_steward(self, name_str):
        if name_str.remove(' ', '').isalpha():
            self.__steward_list.append(name_str)
            return True
        else:
            return False

    def get_steward_list(self):
        return self.__steward_list
