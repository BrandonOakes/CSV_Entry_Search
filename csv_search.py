# create menu option with ability to enter new entry or search previous entries

import csv
import datetime
import re
import sys, pdb

from additional_functions import space, clear, reading_csv, display_entries


def menu():
    """Menu options for user to add new entry, search entry log or quit"""

    while True:
        answer = input('''\nType the number associated with your desired option:\n\n
1) New entry\n
2) Search entry\n
3) Quit\n
>''')
        try:
            if answer in ['1', '3']:
                return answer
                break
            elif answer == '2' and len(reading_csv()) >= 1:
                return answer
                break
            elif answer == '2' and len(reading_csv()) < 1:
                clear()
                print('''There are no entries to search,
at the main menu press 1 to enter a new entry ''')
                space()
            else:
                clear()
                print('''\nSORRY {} IS NOT A VALID SELECTION,
please select 1, 2, or 3.'''.format(answer))
                space()

        except FileNotFoundError:
            clear()
            print('''There are no entries to search,
at the main menu press 1 to enter a new entry ''')


class NewEntry():
    """Creates new entry with entries task name, time spent on entry and
       additional notes about entry
     """

    def __init__(self, task=None, time=None, notes=None):
        self.task = task
        self.time = time
        self.notes = notes

    def task_name(self):
        self.task = input('''Enter the task name you would like to log below.
\n>''').title()
        clear()

    def task_time(self):
        """Ask user for time task took in minutes, try/except utilized to make sure
       user enters numbers only when indicating minutes
       """
        value = True
        while value:
            self.time = input('''How much time in minutes,
was spent on your task?\n>''')
            clear()
            try:
                int(self.time)
                self.time = str(self.time)
                value = False
                clear()
                break
            except ValueError:
                print("""Sorry, {} is not a valid entry, please indicate time spent on task with
digits only. (ex. correct response -> 45 | incorrect response ->forty-five)
\n\n\n""".format(self.time))

    def task_notes(self):
        self.notes = input('''Do you have any additional notes to add about your task?
(if not type -> none):\n>''').title()
        clear()


def new_entry_made():
    date = datetime.date.today()
    new_entry = NewEntry()
    new_entry.task_name()
    new_entry.task_time()
    new_entry.task_notes()
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
        if searching_option in ['1', '2', '3', '4']:
            return searching_option
            break
        else:
            clear()
            print('''\nSorry {} is not a valid selection,
please select 1, 2, 3, or 4.'''.format(searching_option))
            space()


def search_decision(searching_option):
    if searching_option == '1':
        #give list of all possible dates to choose from
        """gives user list of dates associated with entries in csv file"""
        lis = []
        with open('time_sheets.csv') as file_object:
            csvreader = csv.reader(file_object)
            for entry in csvreader:
                lis += entry
        variable = ','.join(lis)
        #show all dates with entries
        regpattern = re.compile(r'\d{4}-\d\d-\d\d')
        print("Listed below are the dates with associated entries:\n:")
        dates_w_entry = regpattern.findall(variable)
        newlist = []
        for var in dates_w_entry:
            #gets rid of same date duplicates
            if var in newlist:
                continue
            else:
                newlist.append(var)
        for entry in newlist:
            print(entry)
        space()
        entry_request = SearchEntry()
        entry_request.pulling_entry_date()
        print('\nEntries from the date you selected are shown above:\n\n\n')
    elif searching_option == '2':
        #give list of entries matching exact characters user provides
        entry_request = SearchEntry()
        entry_request.pulling_entry_task()
    elif searching_option == '3':
        #give list of entries matching exact minutes user provides
        entry_request = SearchEntry()
        entry_request.pulling_entry_minutes()
    elif searching_option == '4':
        #give list of entries matching regax user supplied
        entry_request = SearchEntry()
        entry_request.pulling_entry_regex()
    space()
    print('\t\t\tMAIN MENU\n')


class SearchEntry():
    """Searches csv file by date, regular expression pattern,
     time spent(minutes), exact string
     """

    def __init__(self, search_choice=None):
        """creates entry instance"""
        self.search_choice = search_choice

    def pulling_entry_date(self):
        """allows user to retrieve specific entry from csv file
        based on date user inputs at command line
        """

        self.search_choice = input('''Enter the entry date you would like to search as year-mm-dd
(example: 2018-03-15)\n\n>''')
        entries = reading_csv()
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
                    display_entries(entry)
                break
            clear()
            print("""Sorry your entry {} did not match any entry dates
make sure the entry date you enter is digits and includes year-mm-dd
(example: 2018-03-15\n""".format(self.search_choice))
            self.search_choice = input('''Enter the entry date you would like to search as year-mm-dd
(example: 2018-03-15)\n\n>''')
            value = True

    def pulling_entry_task(self):

        self.search_choice = input("""Enter the exact name for the entry you are searching
\n>""").title()
        entries = reading_csv()
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
                    display_entries(entry)
                print("""\nListed above are entries
matching your exact name search: \n\n\n""")
                break
            clear()
            print("""Sorry your entry {} did not match a task name or notes section
please check your spelling and try again\n""".format(self.search_choice))
            self.search_choice = input("""Enter the exact name for the task name
or additional notes you are searching\n\n>""")
            value = True

    def pulling_entry_minutes(self):
        """allows user to retrieve specific entry from csv file
        based on time spent user inputs at command line
        """

        self.search_choice = input('''Enter the time spent(minutes)
on the entry you are searching\n>''')
        entries = reading_csv()
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
                    display_entries(entry)
                print('''\nListed above are entries matching
the minute total you entered: \n\n\n''')
                break
            clear()
            print("""Sorry your entry {} did not match any entries, make sure you
are only using digits and searching in terms of minutes the task took
\n""".format(self.search_choice))
            self.search_choice = input('''Enter the time spent(minutes)
on the entry you are searching\n>''')
            clear()
            value = True

    def pulling_entry_regex(self):
        """loops through csv file to find matching
         regular expressions entered by user
         """
        value = 0
        while value < 1:
            self.search_choice = input('''Enter the regular expression you would like to use for your search pattern
(ex. \w+\d+)\n>''')
            newlist = []
            regax_pattern = re.compile(self.search_choice)
            with open('time_sheets.csv') as file_object:
                csvreader = csv.reader(file_object)
                for entry in csvreader:
                    # print("Entry: ", entry)
                    if entry in newlist:
                        continue
                    else:
                        for let in entry:
                            # print("let: ", let)
                            # print("regax pattern is: ", regax_pattern)
                            if self.search_choice.isalpha():
                                regax_pattern = re.compile(r'.*{}.*'.format(self.search_choice), re.IGNORECASE)
                                if let in regax_pattern.findall(let):
                                    if entry in newlist:
                                        continue
                                    else:
                                        newlist.append(entry)
                            else:
                                if let in regax_pattern.findall(let):
                                    if entry in newlist:
                                        continue
                                    else:
                                        newlist.append(entry)
            if len(newlist) >= 1:
                for entry in newlist:
                    display_entries(entry)
                value = 1
            else:
                clear()
                print("""Sorry {} was not found as a match or regular expression,
please try again""".format(self.search_choice))


def main_menu():
    """main menu at command line"""

    choice = menu()
    clear()

    if choice == '1':
        new_entry_made()

    elif choice == '2':
        searching_option = search_menu()
        clear()
        search_decision(searching_option)

    elif choice == '3':
        sys.exit()

if __name__ == '__main__':
    while True:
        main_menu()
