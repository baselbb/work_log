""" Import required built in python modules, 
method subclasses for different ciphering methods and 
subclass for asking and checking user input """

import os
import datetime
from user_input import UserInput
from file_edit import FileEdit
from search_record import Search
from edit import RecordChange

# clear screen function when user quits or wants to return task program
def clear_screen():
    """
    Clear screen function when user runs main program script
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Ask user for choice of what they want to do
def menu():
    """
    User main menu for task logging, editting and searching.

    The menu function presents the user with different options to create task names in
    csv file.  

    The menu function calls different classes and methods based on user chosen input to 
    create task and write into a csv file.  Menu function also calls different classes and
    methods to read and edit tasks from the csv file.

    """
    # create menu and sub-menu choices for user
    main_options = {1:'Add a new task', 
                    2:'Search for a task', 
                    3:'Edit or Delete a task',
                    4:'Exit Menu'}

    search_options ={1:'Find by Date',
                     2:'Find by Time Spent',
                     3:'Find by Exact Search',
                     4:'Find by RegEx Pattern',
                     5:'Find by Date Range',
                     6:'Exit Menu'}

    # Print main menu choices
    print("Welcome to Task Manager.  From the menu below choose and option number")
    for key, value in main_options.items():
        print("{}: {}".format(key, value))
    
    # Get user choice for main menu choice
    while True:
        try:
            chosen = int(input("Please enter you chosen OPTION NUMBER here > "))
        except ValueError:
            print("Not a valid choice number")
        else:
            break

    # Ask for user input, 
    # Instantiate class FileEdit and then call method with paramters from user input 
    # Rows are added to csv file

    # User selects choice to create a new task 
    if chosen == 1: 
        task_date = UserInput.ask_date()
        task_name = UserInput.ask_name()
        task_time = UserInput.ask_time()
        task_note = UserInput.ask_note()
        log_task = FileEdit()
        log_task.add_row(task_date, task_name, task_time, task_note)

    # User selects choice to search for taks 
    elif chosen == 2:

        # Sub-menu for search options
        clear_screen()
        for key, value in search_options.items():
            print("{}: {}".format(key,value))

        # Get user choice for search sub menu
        while True:
            try:
                search_chosen = int(input("Please enter you chosen OPTION NUMBER here > "))
            except ValueError:
                print("Not a valid choice number")
            else:
                break

        # Instantiate class Search() and call methods based on user sub-menu choice
        log_task = Search()
        if search_chosen == 1:
            returned = log_task.search_date()
        elif search_chosen == 2:
            returned = log_task.search_time()
        elif search_chosen == 3:
            returned = log_task.search_string()
        elif search_chosen == 4:
            returned = log_task.search_pattern()
        elif search_chosen == 5:
            returned = log_task.search_range()
        elif search_chosen == 6:
            exit()
        else:
            print("Your choice:{} is not available".format(search_chosen))

        total_results = len(returned)

        # Print pagination menu of search results if returned results exists
        if total_results > 0:
            clear_screen()
            print('RESULTS OUTPUT')
            print("{} matching entries".format(total_results))
            print("-"*30)
            print("""To page through entries use the following commands:
                  [N]ext entry
                  [P]revious entry
                  [M]ain menu""")
            print('-'*30)

        # Pagination output of search result entries, displayed one by one
        counter = 0
        while counter < total_results:
            pagination = input("Enter letters [N], [P] or [M] > ").lower()
            if pagination == 'n':
                clear_screen()
                print("Result {} out of {}".format(counter+1, len(returned)))
                print("-"*30+"\n"+"-"*30 )
                for key, values in returned[counter].items():
                    print("{}: {}".format(key, values))
                counter += 1
            elif pagination == 'p':
                if counter == 0:
                    print("You have reached beginning of list")
                else:
                    clear_screen()
                    print("Result {} out of {}".format(counter+1, len(returned)))
                    print("-"*30+"\n"+"-"*30 )
                    for key, values in returned[counter].items():
                        print("{}: {}".format(key, values))
                    counter -= 1
            elif pagination == 'm':
                clear_screen()
                menu()
            else:
                ("Choice not valid.  Enter letters [N], [P] or [M] ")

    # Edit or delete a task 
    elif chosen == 3:
        log_task = RecordChange()
        log_task.record_edit()

    # Option to quit main menu
    elif chosen == 4:
        exit()

    # User enters a choice which is not available
    else:
        print("Your choice:{} is not available".format(chosen))


if __name__ == "__main__":
    clear_screen()
    menu()    
