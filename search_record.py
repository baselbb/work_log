""" Import required built in python modules. 
to search for entries in csvfile"""

import datetime
import csv
import re

class Search():
    """
    Class for task search with in a csv file.
    
    The class has 4 methods to search for  task by different chosen user
    input, which are:
    1. Search by task date
    2. Search by time spent on task
    3. Search by exact search string in task name or task notes
    4. Search by regex search pattern in task name or task notes
    """

    def __init__(self):
        """
        Method to instantiate csv file reading and get rows

        self.rows is used throughout the class to search for different tasks
        within the csv file

        Results from self.rows dictionary are placed in an output list which is returned
        to the main menu for display to the user
        """

        # Read csv file and get unique date values that hav entries
        with open('work_log.csv', newline='') as csvfile:
            self.reader = csv.DictReader(csvfile, delimiter = ',')
            self.rows = list(self.reader)
            self.available_dates = sorted(set([item['Date'] for item in self.rows if 'Date' in item]))

            # Parse dates into datetime format to see if user selected date is in list
            self.available_dates_parsed = [
                datetime.datetime.strptime(date, '%m/%d/%Y') 
                for date in self.available_dates]

            # Get unique list of minutes range
            self.available_minutes =  set(([item['Time Spent'] for item in self.rows if 'Time Spent' in item]))
            self.available_minutes_int = list(map(int, self.available_minutes))

    def search_date(self):
        """
        Method to search for task entries from csv file by Date
        """

        pagination = []

        # Print dates with entries to user
        print("The following dates have entries:"+"\n"+"-"*30)
        print(*self.available_dates, sep = '\n')

        # Ask user for date and check that date format the user entered is a valid  
        while True:
            date_selected = input("""Please enter the date you want to see entries for in MM/DD/YYYY format > """)
            try:
                user_date_parsed = datetime.datetime.strptime(date_selected, '%m/%d/%Y')
            except ValueError:
                print("Oops! {} Not a valid date format".format(date_selected))
            else:
                # Check if user parsed date is in parsed datetimes with available entries
                if user_date_parsed not in self.available_dates_parsed:
                    print("Oops! This date has no entries. Please select from the list above.")
                else:
                    break

        # Print tasks for selected dates including details
        for item in self.rows:
                item_date = datetime.datetime.strptime(item['Date'], '%m/%d/%Y')
                if item_date == user_date_parsed:
                    pagination.append(item)

        return pagination

    def search_time(self):
        """
        Method to search for task entries from csv file by Time spent on task
        in minutes
        """

        pagination = []
        # Print min-max range to help user choose with entries with minutes
        max_time = max(self.available_minutes_int)
        min_time = min(self.available_minutes_int)
        print("""The max-min Time Spent on tasks is between {} - {} minutes"""
              .format(min_time, max_time))

        while True:
            try:
                user_minutes = int(input("Please enter time spent on tasks in MINUTES >"))
            except ValueError:
                print("Not a valid minutes search selection.  Try again.")
            else:
                # Check if user minutes is in parsed datetimes with available entries
                if user_minutes not in self.available_minutes_int:
                    print("Oops! Minutes selectd has no matching entries.")
                else:
                    break

        # Print tasks for selected minutes including details
        for item in self.rows:
                item_minutes = int(item['Time Spent'])
                if user_minutes == item_minutes:
                    pagination.append(item)
    
        return pagination

    def search_string(self):
        """
        Method to search for task entries from csv file by exact search string
        provided by the user
        """

        pagination = []
        output = []
        user_string = str.split(input("Please the search term you are looking for >"))
        for term in user_string:
            for item in self.rows:
                if term in item['Task Name']:
                    if item not in output:
                        output.append(item)
                if term in item['Task Note']:
                    if item not in output:
                        output.append(item)

        if len(output) == 0:
            print("Oops! No matching results for entered search string")
        else:
            for item in output:
                pagination.append(item)

        return pagination

    def search_pattern(self):
        """
        Method to search for task entries from csv file by regex pattern
        """

        pagination = []
        output = []
        # Get user input for pattern and compile regex pattern in variable
        user_input = input("Please enter regex search pattern > ")
        pattern = r'{}'.format(user_input)

        # Search for regex pattern in task name and notes and add to output list
        try:
            for item in self.rows:
                if re.search(pattern, item['Task Name'], re.I):
                    if item not in output:
                        output.append(item)
                if re.search(pattern, item['Task Note'], re.I):
                    if item not in output:
                        output.append(item)
        except re.error:
            print("Oops! Regex entered not valid")

        # If no matches results, print statement to user, else send results to returned list 
        if len(output) == 0:
            print("Oops! No matching results for entered regex pattern: {}".format(user_input))
        else:
            for item in output:
                        pagination.append(item)

        return pagination

    def search_range(self):
        """
        Method to search for task entries from csv file by Date Range
        """

        pagination = []

        # Print dates with entries to user
        print("The following dates have entries:"+"\n"+"-"*30)
        print(*self.available_dates, sep = '\n')

        # START date loop to ask for start date and check if it is a valid date
        while True:
            # Ask user for date and check that date format the user entered is a valid  
            while True:
                start_date = input("""Please enter the START date you want to see entries for in MM/DD/YYYY format > """)
                try:
                    start_parsed = datetime.datetime.strptime(start_date, '%m/%d/%Y')
                except ValueError:
                    print("Oops! date format not valid")
                else:
                    # Check if user parsed date is in parsed datetimes with available entries
                    if start_parsed not in self.available_dates_parsed:
                        print("Oops! This date has no entries. Please select from the list above.")
                    else:
                        break

            # END date loop to ask for end date and check if it is a valid date
            while True:
                end_date = input("""Please enter the END date you want to see entries for in MM/DD/YYYY format > """)
                try:
                    end_parsed = datetime.datetime.strptime(end_date, '%m/%d/%Y')
                except ValueError:
                    print("Oops! date format not valid")
                else:
                    # Check if user parsed date is in parsed datetimes with available entries
                    if start_parsed not in self.available_dates_parsed:
                        print("Oops! This date has no entries. Please select from the list above.")
                    else:
                        break
            if start_parsed <= end_parsed:
                break
            else:
                print("End date should be AFTER start date")


        # Print tasks for selected dates including details
        for item in self.rows:
                item_date = datetime.datetime.strptime(item['Date'], '%m/%d/%Y')
                if (start_parsed <= item_date <= end_parsed):
                    pagination.append(item)

        return pagination
