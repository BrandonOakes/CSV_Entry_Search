import os
import csv

def space():
	"""provides space between menu options"""

	print('_' * 75 + '\n' *4)


def clear():
	"""clears terminal screen"""
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def reading_csv():
	with open('time_sheets.csv') as file_object:
		csvreader = csv.reader(file_object)
		entries = []
		for entry in csvreader:
			entries.append(entry)
	return entries

def display_entries(entry):
	print('Task name: ' + entry[0])
	print('Time spent(min): ' + entry[1])
	print('Additional notes: ' + entry[2])
	print('Entry date: ' + entry [3])
	print('____'*15)