""" Import required built in python modules. 
to write task entries in csvfile"""

import csv

class FileEdit():
    """ Class to create records and write record rows to a 
    csv file from user input.

    """
    def __init__(self):
        """
        Method to instantiate csv file reading and get rows

        self.taskwriter is used by class methods to write a task
        into the csvfile

        """

        self.fieldnames = ['Date', 'Task Name', 'Time Spent','Task Note']
        
        with open('work_log.csv', 'a') as csvfile:
            self.taskwriter = csv.DictWriter(csvfile, fieldnames = self.fieldnames)
            #self.taskwriter.writeheader()

    
    def add_row(self, task_date, task_name, task_time, task_note):
        """
        Method to write task details to csv file
        
        Arguments required:
        task_date: Task Date in strf format 
        task_name: Task Name as a string
        task_time: Time Spent on task in minutes
        task_note: Task Note, any additional notes on the task

        """

        # Open file for appending, write a row of task details using DictWriter
        with open('work_log.csv', 'a') as csvfile:
            self.taskwriter = csv.DictWriter(csvfile, fieldnames = self.fieldnames)
            self.taskwriter.writerow({
                    'Date':task_date,
                    'Task Name':task_name,
                    'Time Spent':task_time,
                    'Task Note':task_note
                })
