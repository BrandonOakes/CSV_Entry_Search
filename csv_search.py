#create menu option with ability to enter new entry or search previous entries
import csv, datetime, re, sys, os



def space():
	"""provides space between menu options"""

	print('_' * 75 + '\n' *4)


def clear():
	"""clears terminal screen"""
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def time_input():
	"""Ask user for time task took in minutes, try/except utilized to make sure
       user enters numbers only when indicating minutes
       """
	value = True
	while value:
		time = input('How much time in minutes, was spent on your task?\n>')
		clear()
		try: 
			int(time)
			return time
			value = False
			break
		except ValueError:
			print("""Sorry, {} is not a valid entry, please indicate time spent on task
with digits only. (ex. correct response -> 45 | incorrect response ->forty-five)\n\n\n""".format(time))


def search_menu():
	"""Menu options for searching prior entries, user can select between
	   four options, if user does not choose a number 1-4, they will be 
	   informed they have entered a invalid entry and menu options will 
	   appear again"""
	while True:

		searching_option = input('''How would you like to search for your entry?\n
	Type the number associated with your desired option.\n
1) Find by date\n
2) Find by exact name search\n
3) Find by time spent on task(minutes)\n
4) Find by regular expression pattern\n
>''')
		if searching_option == '1':
			return searching_option
			break
		elif searching_option == '2':
			return searching_option
			break
		elif searching_option == '3':
			return searching_option
			break
		elif searching_option == '4':
			return searching_option
			break
		else:
			clear()
			print('\nSorry {} is not a valid selection, please select 1, 2, 3, or 4.'.format(searching_option))
			space()


class NewEntry():
	"""Creates new entry with entries task name, time spent on entry and
	   additional notes about entry
	 """
	
	def __init__(self, task, time, notes):
		self.task = task
		self.time = time
		self.notes = notes


class SearchEntry():
	"""Searches csv file by date, regular expression pattern, time spent(minutes), exact string"""

	def __init__(self, search_choice):
		"""creates entry instance"""
		self.search_choice = search_choice

	def pulling_entry_date(self):
		"""allows user to retrieve specific entry from csv file based on date user inputs at command line"""

		with open('time_sheets.csv') as file_object:
			csvreader = csv.reader(file_object)
			entries = []
			for entry in csvreader:
				entries.append(entry)
			final_list = []
			value = True
			while value:
				for entry in entries:
					if self.search_choice == entry[3]:
						final_list.append(entry[:])
					else:
						continue
				if len(final_list) >= 1:
					clear()
					for entry in final_list:
						print('Task name: ' + entry[0])
						print('Time spent(min): ' + entry[1])
						print('Additional notes: ' + entry[2])
						print('Entry date: ' + entry [3])
						print('____'*15)
					break
				print("""Sorry your entry {} did not match any entry dates
make sure the entry date you enter is digits and includes year-mm-dd(example: 2018-03-15\n""".format(self.search_choice))
				self.search_choice = input('Enter the entry date you would like to search as year-mm-dd(example: 2018-03-15)\n\n>')
				value = True


	def pulling_entry_minutes(self):
		"""allows user to retrieve specific entry from csv file based on time spent user inputs at command line"""

		with open('time_sheets.csv') as file_object:
			csvreader = csv.reader(file_object)
			entries = []
			for entry in csvreader:
				entries.append(entry)
			final_list = []
			value = True
			while value:
				for entry in entries:
					if self.search_choice == entry[1]:
						final_list.append(entry[:])
					else:
						continue
				if len(final_list) >= 1:
					clear()
					for entry in final_list:
						print('Task name: ' + entry[0])
						print('Time spent(min): ' + entry[1])
						print('Additional notes: ' + entry[2])
						print('Entry date: ' + entry [3])
						print('____'*15)
					break
				print("""Sorry your entry {} did not match any entries, make sure you 
are only using digits and searching in terms of minutes the task took\n""".format(self.search_choice))
				self.search_choice = input('Enter the time spent(minutes) on the entry you are searching\n>')
				clear()
				value = True

	
	def pulling_entry_task(self):
		"""gives user entry associated with exact task name or associated notes"""

		with open('time_sheets.csv') as file_object:
			csvreader = csv.reader(file_object)
			entries = []
			for entry in csvreader:
				entries.append(entry)
			final_list = []
			value = True
			while value:
				for entry in entries:
					if self.search_choice.title() == entry[0]:
						final_list.append(entry[:])
					elif self.search_choice.title() != entry[0]:
						if self.search_choice.title() == entry[2]:
							final_list.append(entry[:])
						else:
							continue
				if len(final_list) >= 1:
					clear()
					for entry in final_list:
						print('Task name: ' + entry[0])
						print('Time spent(min): ' + entry[1])
						print('Additional notes: ' + entry[2])
						print('Entry date: ' + entry [3])
						print('____'*15)
					break
				print("""Sorry your entry {} did not match a task name or notes section
please check your spelling and try again\n""".format(self.search_choice))
				self.search_choice = input("Enter the exact name for the task name or additional notes you are searching\n\n>")
				value = True

	
	def pulling_entry_regex(self):
		"""loops through csv file to find matching regular expressions entered by user"""
		newlist = []
		regax_pattern = re.compile(self.search_choice)
		with open('time_sheets.csv') as file_object:
			csvreader = csv.reader(file_object)
			for entry in csvreader:
				if entry in newlist:
					continue
				else:
					for let in entry:
						if let in regax_pattern.findall(let):
							if entry in newlist:
								continue
							else:
								newlist.append(entry)
		for entry in newlist:
			print('Task name: ' + entry[0])
			print('Time spent(min): ' + entry[1])
			print('Additional notes: ' + entry[2])
			print('Entry date: ' + entry [3])
			print('____'*15)


def main_menu(): 
	"""main menu at command line"""

	def menu():
		"""Menu options for user to add new entry, search entry log or quit"""

		while True:  
			menu = input('''\nType the number associated with your desired option:\n\n 
1) New entry\n
2) Search entry\n
3) Quit\n
>''' )
			if menu == '1':
				return menu
				break
			elif menu == '2':
				return menu
				break
			elif menu == '3':
				return menu
				break
			else:
				clear()
				print('\nSORRY {} IS NOT A VALID SELECTION, please select 1, 2, or 3.'.format(menu))
				space()

	menu = menu()
	clear()


	def listed_dates():
		"""gives user list of dates associated with entries in csv file"""
		lis = []
		with open('time_sheets.csv') as file_object:
			csvreader = csv.reader(file_object)
			for entry in csvreader:
				lis += entry
		variable = ','.join(lis)
		#show all dates with entries
		regpattern = re.compile(r'\d{4}-\d\d-\d\d')
		print("Listed below are all possible dates with associated entries:\n:")
		dates_w_entry = regpattern.findall(variable)
		newlist =[]
		for var in dates_w_entry:
			#gets rid of same date duplicates
			if var in newlist:
				continue
			else:
				newlist.append(var)
		for entry in newlist:
			print(entry)

	if menu == '1':
		task = input('Enter the task name you would like to log below. \n>')
		task = task.title()
		clear()
		time = time_input()
		time = str(time)
		clear()
		notes = input('''Do you have any additional notes to add about your task? (if not type -> none):\n>''')
		notes = notes.title()
		date = datetime.date.today()
		clear()
		new_entry = NewEntry(task, time, notes)
		entry_info = [new_entry.task, new_entry.time, new_entry.notes, date]
		with open('time_sheets.csv', 'a') as file_object:
			csvwriter = csv.writer(file_object, delimiter=',')
			csvwriter.writerow(entry_info)
		print('\nTask name: ' + new_entry.task.title() + '.\n')
		print('Time spent on task: ' + new_entry.time + ' minutes.\n')
		print('Additional notes about task: ' + new_entry.notes.title() + '.\n')
		print('Current date listed below:')
		print(date)
		space()
		print('\t\t\tMAIN MENU\n\n\n')

	elif menu == '2':

		searching_option = search_menu()
		clear()
		if searching_option == '1':
			#give list of all possible dates to choose from
			listed_dates()
			space()
			search_choice = input('Enter the entry date you would like to search as year-mm-dd(example: 2018-03-15)\n\n>')
			clear()
			entry_request = SearchEntry(search_choice)
			entry_request.pulling_entry_date()
			print('\nEntries from the date you selected are shown above:\n\n\n')
		elif searching_option == '2':
			#give list of entries matching exact characters user provides
			search_choice = input("Enter the exact name for the entry you are searching\n>")
			clear()
			search_choice = search_choice.title()
			entry_request = SearchEntry(search_choice)
			entry_request.pulling_entry_task()
			print("\nListed above are entries matching your exact name search: \n\n\n")
		elif searching_option == '3':
			#give list of entries matching exact minutes user provides
			search_choice = input('Enter the time spent(minutes) on the entry you are searching\n>')
			clear()
			entry_request = SearchEntry(search_choice)
			entry_request.pulling_entry_minutes()
			print('\nListed above are entries matching the minute total you entered: \n\n\n')
		elif searching_option == '4':
			#give list of entries matching regax user supplied
			search_choice = input('Enter the regular expression you would like to use for your search pattern(ex. \w+\d+)\n>')
			entry_request = SearchEntry(search_choice)
			entry_request.pulling_entry_regex()
		space()
		print('\t\t\tMAIN MENU\n')
	elif menu == '3':
		sys.exit()

if __name__=='__main__':
	while True:
		main_menu()


