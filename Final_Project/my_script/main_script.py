""" This script is used to determine which function to run based on userinput """

import my_module.functions as fc

intro = (""""Reminder:
 
          Add task -> adds tasks
          Archive task -> moves your task to archive list
          Status update -> updates status of task to complete
          See tasks -> displays all your tasks
          
      """)

print(intro)


Run = True
while Run:
    # Asks for user input as long as the program is running 
    message = input(">>> " )
    
    #Determines which function to run based on user input 
    if message.lower() == "add task":
        fc.add_task()
        
        user_input2= input("Would you like to add another task?(Yes / No): ")
        if user_input2 == "Yes":
            fc.add_task()
        
    elif message.lower() == "see tasks":
        fc.display_list()
            
    elif message.lower() == "archive task":
        fc.archive_task()
        
    elif message.lower() == "status update":
        fc.status_update()

  

