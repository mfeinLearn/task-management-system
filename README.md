
# Task Management System 

### Background

    You are a junior software developer working for a productivity app company. Your task is to create a Python program that allows users to manage their tasks and track their progress.

    You will need to create a task management system that allows users to add tasks, mark tasks as complete, view pending tasks, and track their progress. You should format the structure to store tasks as a list of dictionaries, each dictionary representing one task.

    By completing this lab exercise, you will gain practical experience in integrating functions, modules, packages, and data input validation to create a functional task management system. You will learn how to design and implement a modular and maintainable codebase that handles user input, data validation, and data processing.

### Identify the Problem

    Create a Python program that allows users to manage their tasks and track their progress. The task management system should allow users to add tasks, mark tasks as complete, view pending tasks, and track their progress.

    - Task 1: Define a dictionary structure to represent a task. You can use the structure below.
    - Task 2: Implement functions for adding tasks.
    - Task 3: Develop functions for validation.
    - Task 4: Develop functions for marking tasks as complete and viewing pending tasks.
    - Task 5: Create a main script to interact with the task management system.



### Develop the Code

- [x] Task 1: Define a dictionary structure

    Define a dictionary structure to represent a task. You can use the following:

    ```
    task = {"title": "Groceries",
    "description": "Shop at Market Basket for food", 
    "due_date": "2024-06-26",
    "completed": True}
    ```

- Task 2: Implement functions for adding tasks

    Create functions to encapsulate specific tasks and promote code reusability.

    In the validation.py module, create functions to validate user input for task details such as title, description, and due date.

    Function names: 

    validate_task_title
    validate_task_description
    validate_due_date
    In the task_utils.py module, define functions for adding a task, marking a task as complete, viewing pending tasks, and calculating progress, making sure to consider validation.

    Function names:

    add_task
    mark_task_as_complete
    view_pending_tasks
    calculate_progress


- Task 3: Organize functions with modules

    Organize related functions into modules to improve code structure and maintainability:

    Create separate modules for task-related functions (task_utils.py) and data input validation functions (validation.py).
    Group related modules into packages to create a hierarchical structure and enable better code organization:

    Create a package/folder called task_manager and organize the modules (task_utils.py and validation.py) within this package.


- Task 4: Develop functions for validation

    Implement data input validation within functions and modules to ensure data integrity and prevent errors:

    In the validation.py module, implement functions to handle invalid input and provide appropriate error messages.
    Use the validation functions in the task_utils.py module to validate user input before adding tasks.

- Task 5: Develop functions for marking tasks as complete and viewing pending tasks

    Create a main script to interact with the task management system. Use the functions, modules, and packages in the main script to solve the overall problem:

    In the main.py script, create a menu-based interface for the user to interact with the task management system.
    Use the functions from the task_utils.py module to perform operations such as adding tasks, marking tasks as complete, viewing pending tasks, and tracking progress.
    Your main script needs to be on the same directory level as the package task_manager.


### Test and Refine

- Run your program and test various input scenarios, including valid and invalid inputs.
- Verify that the validation functions correctly identify and handle invalid inputs.
- Refine your validation criteria and error messages if needed to provide a better user experience.