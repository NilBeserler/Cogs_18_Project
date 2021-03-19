"""A collection of functions to interact with the todo list."""

import pandas as pd
import numpy as np

main_list = []
archive_list = []

def add_task():
    """
    Adds up to two new tasks to the main_list which contains all the  tasks
    Parameters: None
    Return:None
    
    """
    
    #Collects user input
    task = input("Enter task: ")
    due_date = input("Enter due date: ")
    status = "incomplete"
        
    #Appends user input dictionary to main_list
    main_list.append ({"Task": task,
                        "Due date": due_date,
                        "Status": status})
    
# Additional test to test the function (See test_functions Notes)
if len(main_list) == 1:
    assert main_list[i]["Task"] == task
        
def display_list():  
    """
    Creates dataframe of all the tasks and returns it 
    Parameters: None
    Return: Data table of tasks
    """
    #Creates a dataframe from the main list 
    df = pd.DataFrame(main_list)
    
    #Edits the format of the datatable
    df.index = df.index + 1
    def color_incomplete(val):
        color = 'red' if val == "incomplete" else "black"
        return 'color: %s' % color
    styled_data= df.style.applymap(color_incomplete)
    
    return display(styled_data)
   
def archive_task():
    """"
    Moves task names to archive_list and deletes them from the main list.
    Parameters: None
    Return: Archived tasks
    """
    print("The current todo list is: ")
    display_list()
    
    arched_task = input("Which task do you want to move to archive?: ")
    
    #Goes through the mainlist and archives the chosen task
    for dics in range(len(main_list)):
            if main_list[dics]["Task"] == arched_task:
                del main_list[dics]
                archive_list.append(arched_task)
                break
    
    print ("Here are your archived tasks: ", archive_list)
    
    #Additional test to check if function works
    assert arched_task in archive_list
            
                       
def status_update():
    """
    Updated the status of selected task to complete.
    Parameters: None
    Return:None
    
    """
    
    print("The current todo list is: ")
    display_list()
    
    updated_task = input("Which task do you want to update?: ")
    
    #Goes through the list and changes the status of chosen task to complete 
    for dics in range(len(main_list)):
            if main_list[dics]["Task"] == updated_task:
                main_list[dics]["Status"]= "complete"
               

