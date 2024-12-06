"""
Main.py
12/01/2024
Main file for the Task Management System
"""

from interface import Interface


def user_selection():
    while True:
        try:
            selection = int(input("Please select an option from the above list: "))
            if selection > 5 or selection < 1:
                raise ValueError
            return selection
        except ValueError:
            print("Invalid input!")


def main():
    interface = Interface()
    while True:
        print("\n* * * * * * * * * * * *")
        print("Task Management System")
        print("1 - Enter a new job")
        print("2 - Remove a job")
        print("3 - Display queue")
        print("4 - Generate workday")
        print("5 - Exit program")
        print("* * * * * * * * * * * *\n")
        user_input = user_selection()
        if user_input == 1:
            interface.add_job()
        elif user_input == 2:
            interface.remove_job()
        elif user_input == 3:
            print("Short tasks: ", interface.task_manager.short)
            print("Medium tasks: ", interface.task_manager.medium)
            print("Long tasks: ", interface.task_manager.long)
        elif user_input == 4:
            interface.display_workday()
        elif user_input == 5:
            print("Thank you for using our program!")
            break


main()
