""" Import required datetime module for UserInput class and methods"""

import datetime

class UserInput():
    """ Class to create and parse user input and write to csv file.

    The class has four different methods to create a task an write it
    to the csv file.
    
    The class methods return 4 values which are passed in menu.py to
    file_edit.py to write the tasks in the csvfile

    """

    def ask_date():
        """
        Method to ask and write task date to csv file.

        """

        #get task date, parse into datetime format
        while True:
            user_date = input("Enter task Date in MM/DD/YYY format > ")
            try:
                parsed_date = datetime.datetime.strptime(user_date, '%m/%d/%Y')
                break
            except ValueError:
                print("Oops! Not a valid date format.")
                
        task_date = datetime.datetime.strftime(parsed_date, '%m/%d/%Y')
        return task_date 

    def ask_name():
        """
        Method to ask and write task name to csv file.

        """
        #get task name 
        task_name = input("Please enter task name >")
        return task_name

    def ask_time():
        """
        Method to ask and write task spent in minutes to csv file.

        """
        # get time spent on task in minutes
        while True:
            try:
                task_time = int(input("Please enter the time spent on task in minutes >"))
            except ValueError:
                print ("This is not a valid time spent in minutes")
            else:
                break
        return task_time

    def ask_note():    
        # get additional notes by the user
        task_note = input("Enter any additional task notes here >")
        
        return task_note
