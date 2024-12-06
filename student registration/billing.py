# ----------------------------------------------------------------
# Date: 11/07/2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime


def display_bill(s_id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: s_id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------

    # Check for and assign In or Out of state student status
    if s_id in s_in_state and s_in_state[s_id]:
        student_state = 'In-State'
    else:
        student_state = 'Out-of-State'

    # Get the current_date_time w/ datetime module
    current_datetime = datetime.datetime.now()

    # Print the bill header - strftime function used to format current datetime
    print("Tuition Summary - Fake Tech University")
    print(f"Student: {s_id}, {student_state} Student")
    print(current_datetime.strftime("%b %d, %Y at %I:%M %p"))
    # print(f"{current_datetime:%b %d, %Y at %I:%M %p}")
    print("Course    Hours      Cost")
    print("------    -----    ---------")

    # Bill Processing
    bill_total = 0.0
    total_hours = 0
    for course, hours in c_hours.items():
        # Assign Out-of-State course_cost
        if student_state == "Out-of-State":
            course_cost = hours * 850
        # Assign In-State course_cost
        else:
            course_cost = hours * 225

        # Check if Student ID registered in Class Roster; If so, print a line with course data
        if s_id in c_rosters.get(course, []):
            bill_total += course_cost
            total_hours += hours
            print(f"{course}        {hours}    $ {course_cost:.2f}")

    # Print the student's total bill cost
    print("        -------    ---------")
    print(f"Total         {total_hours}    $ {bill_total:.2f}")
