""" Import required modules for RecordChange class and methods
Import UserInput class to manage validation of user input when
editing task details such as datetimes.
"""

import datetime
import csv
from user_input import UserInput

class RecordChange():
    """ Class to edit or delete task from csv file.

   To edit or delete task from the csv file:
   1. Read file and output entries to a list
   2. Ask user for task name to edit or delete
   3. Save new date into a new list
   4. Overwrite new list to existing file

    """

    def __init__(self):
        """
        Method to instantiate csv file reading and get rows

        self.rows stores current csvfile contents before
        any edits or deletes by the user

        """

        with open('work_log.csv', newline='') as csvfile:
        # Read csv file and get unique date values that hav entries
            self.reader = csv.DictReader(csvfile, delimiter = ',')
            self.rows = list(self.reader)

    def record_edit(self):
        """
        Method to edit or delete a task
        """
        output = []
        final = []

        # check if an entry with user provided Task name exists
        while True:
            user_input = (input("Choose a Task Name to edit or delete > ")).lower()
            for item in self.rows:
                if user_input == (item['Task Name']).lower():
                    output.append(item)
            if len(output) > 0:
                break
            else:
                print("Oops! Task Entry with Task Name:{} does not exist".format(user_input)) 

        # if entry with user key exists then print entry details for the user
        if len(output) > 0:
            print("Entry to edit or delete")
            print('-'*30)
            for item in output:
                for key, value in item.items():
                    print("{}: {}".format(key, value))
            print('-'*30)

        # Ask user to edit or delete the task
        while True:
            try:
                choice = int(input("Woud like to 1:Edit or 2:Delete the task? > "))
                if (choice == 1) or (choice == 2):
                    break
                else:
                    print("Not a valid choice.  Choose again")

            except ValueError:
                print("Not a valid choice")

        if choice == 1:
            # Get user selected key to edit and check if it is a valid field name 
            headers = ['Date', 'Task Name', 'Time Spent', 'Task Note']
            while True:
                key_edit = input("What would you like to edit:\nDate\nTask Name\nTime Spent\nTask Note\n > """)
                if key_edit in headers:
                    break
                else:
                    print("Not a valid task key to edit.  Try Again")

            # Ask user for the replacement value by calling methods in class UserInput and append output to output list
            print("Please enter the new value")
            if key_edit == headers[0]:
                new_value = UserInput.ask_date()
                output[0][key_edit] = new_value
            elif key_edit == headers[1]:
                new_value = UserInput.ask_name()
                output[0][key_edit] = new_value
            elif key_edit == headers[2]:
                new_value = UserInput.ask_time()
                output[0][key_edit] = new_value
            elif key_edit == headers[3]:
                new_value = UserInput.ask_note()
                output[0][key_edit] = new_value

            # Add task details which changed/deleted to a new final list of all values
            for item in self.rows:
                if item[key_edit] != output[0][key_edit]:
                    final.append(item)
                else:
                    final.append(output[0])

        # DELETE a task, user selected task for deletion is omitted from final list
        elif choice == 2:
            for item in self.rows:
                if item['Task Name'] != output[0]['Task Name']:
                    final.append(item) 

        # Write new values to the file again
        fieldnames = ['Date', 'Task Name', 'Time Spent','Task Note']
        with open('work_log.csv', 'w') as csvfile:
            taskwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            taskwriter.writeheader()
            for row in final:
                taskwriter.writerow({
                    'Date':row['Date'],
                    'Task Name':row['Task Name'],
                    'Time Spent':row['Time Spent'],
                    'Task Note':row['Task Note']
                })
