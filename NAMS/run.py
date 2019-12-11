# -*- coding: utf-8 -*-
from view.user_interface import UILayer
from database.update_class import Update

if __name__ == '__main__':
	Update.update_rtrip_csv_file()
	UILayer.main()
