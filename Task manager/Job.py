"""
Job.py
12/01/2024
Implementation of Job Class
"""


class Job:
    def __init__(self, name, time_needed):
        """
        Initializes a Job instance.
        :param name: The name of the job.
        :param time_needed: The time needed to complete the job (in hours).
        """
        self.name = name
        self.time_needed = time_needed

    def get_time_needed(self):
        """ Returns the time needed to complete the job.
        :return: Time needed as a float. """
        return self.time_needed

    def __str__(self):
        """ Returns a string representation of the Job.
        :return: A string in the format 'Job Name (Time Needed hrs)'."""
        return f"{self.name} ({self.time_needed} hrs)"

    def __eq__(self, other):
        """Checks equality of two Job instances based on name and time needed.
        :param other: Another Job instance.
        :return: True if both have the same name and time needed, False otherwise."""
        if isinstance(other, Job):
            return self.name == other.name and self.time_needed == other.time_needed
        return False
