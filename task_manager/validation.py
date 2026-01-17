from datetime import datetime

def validate_task_title(title):
    ## checking to make sure title is a string
    if type(title) != str or type(title) == int: 
        raise ValueError("Invalid input - Please type a string")
    return True
    
def validate_task_description(description):
    ## checking to make sure title is a string
    if type(description) != str or type(description) == int: 
        raise ValueError("Invalid input - Please type a string")
    if len(description) > 500:
        # anything here
            return True
    raise ValueError("Invalid length - Please type no less then 500 characters")
    
    
def validate_due_date(due_date):
    ## making sure the day is sometime in the future
    current_time = datetime.now().date() #.now()
    if due_date < current_time:
        raise ValueError("Please specify a day in the future!")
    return True