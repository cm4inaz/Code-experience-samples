# ----------------------------------------------------------------
# Date: 11/10/2023
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(s_id, c_roster):
    # Get the list of courses the student is enrolled in

    enrolled_courses = []
    for course, roster in c_roster.items():
        if s_id in roster:
            enrolled_courses.append(course)

    # Total number of courses the student is currently in
    total_courses = len(enrolled_courses)

    # Display the list of courses
    print("Courses:")
    for course, roster in c_roster.items():
        status = " (Enrolled)" if s_id in roster else ""
        print(f"{course}{status}")

    # Display the total number of courses the student is enrolled in
    print(f"Total courses enrolled: {total_courses}")


def add_course(s_id, c_roster, c_max_size):
    # Get the course the student wants to add
    course_to_add = input("Enter course you want to add: ").upper()

    if course_to_add not in c_roster:
        print("Course not found.")
    elif s_id in c_roster[course_to_add]:
        print("You are already enrolled in that course.")
    elif len(c_roster[course_to_add]) >= c_max_size[course_to_add]:
        print("Course already full.")
    else:
        c_roster[course_to_add].append(s_id)
        print("Course added.")


def drop_course(s_id, c_roster):
    # Get the course the student wants to drop
    course_to_drop = input("Enter course you want to drop: ").upper()

    if course_to_drop not in c_roster:
        print("Course not found")
    # Check if student is enrolled in the course
    elif s_id not in c_roster[course_to_drop]:
        print("You are not enrolled in that course.")
    else:
        # Remove the student from a course
        c_roster[course_to_drop].remove(s_id)
        print("Course dropped")
