from Student import StudentManagement, student_manager

from AddStudent import addStudent
from ModifyStudent import modifyStudent
from DeleteStudent import deleteStudent


#from ModifyStudent import modifyStudent


def show_user_menu(Username):
    print('===========================================================')
    print(f'******************* Welcome {Username} to Student Management System *************************')
    menu = '''
        		â—†  1. Add Student
        		â—†  2. Show Student
        		â—†  3. Modify Student
        		â—†  4. Delete Student
        		â—†  5. Query Student Scores
        		â—†  6. Return to the Previous Menu
        		'''

    while True:
        print('=============================================================')
        print(menu)
        print('=============================================================')
        choice = input("Please Select(1-6):")
        if choice == '1':
            addStudent()
        elif choice == '2':
            student_manager.show_students()
        elif choice == '3':
            modifyStudent()
        elif choice == '4':
            deleteStudent()
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            print("Invalid choice. Please enter (1-6)")
