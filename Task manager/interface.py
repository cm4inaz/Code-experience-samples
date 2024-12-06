"""
interface.py
11/30/2024
Interface for the Task Management System
"""

from Job import Job
from taskmanager import TaskManager


class Interface:
    def __init__(self):
        self.task_manager = TaskManager()

    def add_job(self):
        name = input("Enter the job name: ")
        while True:
            try:
                time_needed = float(input("Enter the time needed for the job (in hours): "))
                job = Job(name, time_needed)
                self.task_manager.add_job(job)
                break
            except ValueError:
                print("Invalid input! Please use a number for hours!")

    def remove_job(self):
        name = input("Enter the job name: ")
        self.task_manager.remove_job(name)

    def display_workday(self):
        workday = self.task_manager.fill_workday()
        print("Workday tasks:")
        time_filled = 0
        while not workday.is_empty():
            job = workday.pop()
            print(f"- {job}")
            time_filled += job.get_time_needed()
        print(f'Time filled: {time_filled} hrs')


if __name__ == "__main__":
    interface = Interface()
    while True:
        action = input("Add job or generate workday? (add/generate/exit): ").lower()
        if action[:1] == 'a':
            interface.add_job()
        elif action[:1] == 'g':
            interface.display_workday()
        elif action[:1] == 'e':
            break
