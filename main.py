# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task
from task_manager.task_utils import mark_task_as_complete
from task_manager.task_utils import view_pending_tasks
from task_manager.task_utils import calculate_progress
from task_manager.validation import validate_due_date
from task_manager.validation import validate_task_description
# from datetime import datetime
from datetime import date


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input('Please specify a title for your new task: ')
            description = input('Please specify a description for your new task: ')
            
            while True:
                try:
                    year  = int(input('Please specify the year of the due date: '))
                    month = int(input('Please specify the month of the due date: '))
                    day   = int(input('Please specify the day of the due date: '))
                    due_date = date(year, month, day)
                except ValueError:
                    print("Sorry, wrong date format - please use numbers only.")
                    continue
                if validate_due_date(due_date):
                    break
                else:
                    print(f'Due date not accepted - please specify another!')
            # new_task = { "title": title, "description": description, "due_date": due_date, "completed": False }
            # add_task(new_task)
            add_task(title, description, due_date)
        elif choice == "2":
            task_marked_completed = input('Please specify the task that you you want to mark as completed?')
            mark_task_as_complete(task_marked_completed)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            calculate_progress()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

# task = 
    # "title": "Groceries", 
    # "description": "Shop at Market Basket for food", 
    # "due_date": "2024-06-26",
    # "completed": True}

