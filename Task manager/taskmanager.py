"""
taskmanager.py
12/01/2024
file for the TaskManager Class
"""

from listqueue import ListQueue
from Job import Job


class TaskManager:
    def __init__(self, short_limit=1, medium_limit=3):
        self.short = ListQueue()
        self.medium = ListQueue()
        self.long = ListQueue()

        self.workday = ListQueue()

        self.short_limit = short_limit
        self.medium_limit = medium_limit

    def add_job(self, job: Job):
        if job.get_time_needed() <= self.short_limit:
            self.short.add(job)
        elif job.get_time_needed() <= self.medium_limit:
            self.medium.add(job)
        else:
            self.long.add(job)

    def remove_job(self, name):
        removed = False
        temp_queue = ListQueue()
        while not self.short.is_empty():
            job = self.short.pop()
            if job.name != name or removed: # Add job to temp if it is not the first matching job
                temp_queue.add(job)
            else: 
                removed = True
        self.short = ListQueue(temp_queue)

        temp_queue.clear()
        if not removed:
            while not self.medium.is_empty():
                job = self.medium.pop()
                if job.name != name or removed: # Add job to temp if it is not the first matching job
                    temp_queue.add(job)
                else: 
                    removed = True
            self.medium = ListQueue(temp_queue)

        temp_queue.clear()
        if not removed:
            while not self.long.is_empty():
                job = self.long.pop()
                if job.name != name or removed: # Add job to temp if it is not the first matching job
                    temp_queue.add(job)
                else: 
                    removed = True
            self.long = ListQueue(temp_queue)

        if removed:
            print("\n*Job Removed!*\n")
        else:
            print("\nJob is not in queue!\n")


    def fill_workday(self, workday_length=8.0):
        # attempt to schedule high priority job of each length every loop until day is filled
        time_filled = 0
        self.workday.clear()
        while True:
            skipped = True
            if not self.long.is_empty() and time_filled + self.long.peek().get_time_needed() <= workday_length:
                job = self.long.pop()
                self.workday.add(job)
                time_filled += job.get_time_needed()
                skipped = False

            if not self.medium.is_empty() and time_filled + self.medium.peek().get_time_needed() <= workday_length:
                job = self.medium.pop()
                self.workday.add(job)
                time_filled += job.get_time_needed()
                skipped = False

            if not self.short.is_empty() and time_filled + self.short.peek().get_time_needed() <= workday_length:
                job = self.short.pop()
                self.workday.add(job)
                time_filled += job.get_time_needed()
                skipped = False

            if skipped:
                break

        return self.workday

    def get_workday(self):
        return self.workday


def test():
    task_manager = TaskManager()
    jobs = [Job('Short', 1),
            Job('Medium', 2),
            Job('Medium', 1.5),
            Job('Short', 0.5),
            Job('Long', 4.5),
            Job('Medium', 2),
            Job('Short', 0.25),
            Job("Long", 3.5)]

    time_available = float(input('How long is your work day? '))
    for job in jobs:
        task_manager.add_job(job)

    workday = task_manager.fill_workday(time_available)

    print(f"Today's Schedule:")
    time_filled = 0
    while not workday.is_empty():
        job = workday.pop()
        print(job)
        time_filled += job.get_time_needed()

    print(f'Time filled: {time_filled} hrs')


if __name__ == "__main__":
    test()
