


# version 2

import sys
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)
from task_manager.validation import validate_due_date, validate_task_description
from datetime import date


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        print("Enter your choice (1-5): ", end="")
        choice = sys.stdin.readline().strip()
        if not choice:  # EOF detected
            print("\nEnd of input detected. Exiting the program...")
            break

        if choice == "1":
            # Title
            print('Please specify a title for your new task: ', end="")
            title = sys.stdin.readline().strip()
            if not title:
                print("\nInput cancelled. Returning to menu.")
                continue

            # Description with validation (now handles raised ValueError)
            description = None
            while True:
                print('Please specify a description for your new task: ', end="")
                desc_input = sys.stdin.readline().strip()
                if not desc_input:  # EOF or empty line
                    print("\nInput cancelled. Returning to menu.")
                    description = None
                    break

                try:
                    validate_task_description(desc_input)  # Will raise ValueError if invalid
                    description = desc_input
                    break
                except ValueError as e:
                    print(e)  # Prints the validator's message, e.g. "Invalid length - Please type no less then 500 characters"
                    print("Please try again.")

            if description is None:
                continue

            # Due date with validation
            due_date = None
            while True:
                print('Please specify the year of the due date: ', end="")
                year_str = sys.stdin.readline().strip()
                if not year_str:
                    print("\nInput cancelled. Returning to menu.")
                    due_date = None
                    break

                print('Please specify the month of the due date: ', end="")
                month_str = sys.stdin.readline().strip()
                if not month_str:
                    due_date = None
                    break

                print('Please specify the day of the due date: ', end="")
                day_str = sys.stdin.readline().strip()
                if not day_str:
                    due_date = None
                    break

                try:
                    year = int(year_str)
                    month = int(month_str)
                    day = int(day_str)
                    potential_date = date(year, month, day)
                except ValueError:
                    print("Sorry, wrong date format - please use numbers only.")
                    continue

                if validate_due_date(potential_date):
                    due_date = potential_date
                    break
                else:
                    print("Due date not accepted (past date or invalid) - please specify another!")

            if due_date is None:
                continue

            add_task(title, description, due_date)
            print("Task added successfully!")

        elif choice == "2":
            print('Please specify the task title or ID to mark as completed: ', end="")
            task_identifier = sys.stdin.readline().strip()
            if not task_identifier:
                continue
            mark_task_as_complete(task_identifier)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


#### original version
# # Import functions from task_manager.task_utils package
# from task_manager.task_utils import add_task
# from task_manager.task_utils import mark_task_as_complete
# from task_manager.task_utils import view_pending_tasks
# from task_manager.task_utils import calculate_progress
# from task_manager.validation import validate_due_date
# from task_manager.validation import validate_task_description
# # from datetime import datetime
# from datetime import date


# # Define the main function
# def main():
#     while True:
#         print("Task Management System")
#         print("1. Add Task")
#         print("2. Mark Task as Complete")
#         print("3. View Pending Tasks")
#         print("4. View Progress")
#         print("5. Exit")
#         choice = input("Enter your choice (1-5): ")

#         if choice == "1":
#             title = input('Please specify a title for your new task: ').strip()

#             # Description with validation loop
#             while True:
#                 description = input('Please specify a description for your new task: ').strip()
#                 try:
#                     if validate_task_description(description):
#                         break
#                     else:
#                         print("Description not accepted (too short/empty/invalid format). Please try again.")
#                 except Exception as e:
#                     print(f"Error validating description: {e}")
#                     print("Please try again.")

#             # Due date with validation loop
#             while True:
#                 try:
#                     year  = int(input('Please specify the year of the due date: '))
#                     month = int(input('Please specify the month of the due date: '))
#                     day   = int(input('Please specify the day of the due date: '))
#                     due_date = date(year, month, day)
#                 except ValueError:
#                     print("Sorry, wrong date format - please use numbers only.")
#                     continue

#                 if validate_due_date(due_date):
#                     break
#                 else:
#                     print("Due date not accepted (past date or invalid) - please specify another!")

#             # Add the task
#             add_task(title, description, due_date)
#             print("Task added successfully!")

#         elif choice == "2":
#             task_identifier = input('Please specify the task title or ID to mark as completed: ').strip()
#             mark_task_as_complete(task_identifier)

#         elif choice == "3":
#             view_pending_tasks()

#         elif choice == "4":
#             calculate_progress()

#         elif choice == "5":
#             print("Exiting the program...")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")
        
# if __name__ == "__main__":
#     main()

# # task = 
#     # "title": "Groceries", 
#     # "description": "Shop at Market Basket for food", 
#     # "due_date": "2024-06-26",
#     # "completed": True}

