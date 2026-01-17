from datetime import datetime

# Import validation functions
from .validation import *
# import validate_task_title
# import validate_task_description
# import validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    new_task = {}
    new_task["title"] = title
    new_task["description"] = description
    new_task["due_date"] = due_date
    new_task["completed"] = 'False'
    tasks.append(new_task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    print(tasks)
    if tasks[index]:
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print(" Sorry can't find! Please specify again! ")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    counter = 0
    for el in tasks:
        # if el["completed"] == 'False':
        if el["completed"] == 'True':
            counter += 1 
    return(counter/len(tasks)*100)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    # print(tasks)
    counter = 0
    for el in tasks:
        # if el["completed"] == 'False':
        if el["completed"] == True:
            counter += 1 
    part = counter
    whole = len(tasks)
    return((part/whole)*100)

############################
# task = 
    # "title": "Groceries", 
    # "description": "Shop at Market Basket for food", 
    # "due_date": "2024-06-26",
    # "completed": True}