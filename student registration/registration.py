# ----------------------------------------------------------------
# Date: 11/09/2023
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
from student import list_courses, add_course, drop_course
from billing import display_bill


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}
    # begin the login session
    status = False
    while status is False:

        # Get the student ID number or 0 if they wish to end the session
        s_id = input('Enter the ID to log in, or 0 to quit: ')

        # call on the login function
        if s_id != '0':
            status = login(s_id, student_list)

        # end the session loop
        else:
            print('Session Ended')
            break
        # display the menu and call on other function corresponding to the options chosen
        while status is not False:
            show_menu()
            action = input('What would you like to do? ')
            print('')
            if action == '1':
                add_course(s_id, course_roster, course_max_size)
            elif action == '2':
                drop_course(s_id, course_roster)
            elif action == '3':
                list_courses(s_id, course_roster)
            elif action == '4':
                display_bill(s_id, student_in_state, course_roster, course_hours)

            # end the current student loop and return to the beginning of the login loop
            elif action == '0':
                print('Session ended.\n')
                status = False


def login(s_id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: s_id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    student_pin = input('Enter PIN: ')

    # Set the login in loop to true if ID and PIN are present in the student registration
    if (s_id, student_pin) in s_list:
        print('ID and PIN verified')
        return True

    # if not, set the loop to false
    else:
        print('ID or PIN could not be verified.\n')
        return False


def show_menu():
    # ------------------------------------------------------------
    # This function displays the action menu to the logged in student.
    # It takes no parameters and returns no values.
    # -------------------------------------------------------------
    print('\nAction Menu\n'
          '___________\n'
          '1: Add course\n'
          '2: Drop course\n'
          '3: List courses\n'
          '4: Show bill\n'
          '0: Logout')


main()
