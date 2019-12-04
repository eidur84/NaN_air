class DBLayer:

	input_data = ''
	# output_data =
	key_word = ''
	search_column = ''
	result_column = ''
	filenames = []

	def search():
		pass


        def generic_search(self, filename, filter_column, key_word, result_column="all"):
            """
            Function which searches a csv file for key_word in filter_column.
            Returns value in specified result_column for each matched row.
            Returns all values in row if result_column is "all" (default value).
            """
            filename = f'csv_files/{filename}'

            csv_file = open(filename, "r")
            csv_dict = DictReader(csv_file)  # Loads rows into dictionary with column names as keys.

            results = [ ]

            for row in csv_dict:

                # Finds row with value in filter_column matching key_word.
                if row[filter_column] == key_word:

                    if result_column == "all":
                        results.append([value for key, value in row.items()])

                    else:
                        results.append(row[result_column])

            csv_file.close()
            return results
