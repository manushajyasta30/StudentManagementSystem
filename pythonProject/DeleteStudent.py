"""
Delete Student
"""
#from AddStudent import student_records

import re


student_rec = {'ID': '1234', 'name': "Manusha Jyasta", 'major': 'III','phone': "123-123-1234"}



def deleteStudent():
    print('=============================== Delete Student ============================ ')

    while True:

        while True:
            print('\u2666 1.Delete Student by ID')
            print('\u2666 2.Delete Student by Name')
            inputSelection = input("Please select 1 or 2:")
            if inputSelection == '1':
                student_id = input("Enter student's ID to delete: ")
                if not validate_studentID(student_id):
                    print("\u274C No record found")
                    continue
                #del student_rec[student_id]
                #implement delete by ID functionality
                print("")
                break
            elif inputSelection == '2':
                while True:
                    full_name = input("Enter student's full name (Firstname Lastname): ")
                    first_name, last_name = extract_first_last_name(full_name)
                    if not validate_name(first_name):
                        print("\u274C Invalid first name.")
                        continue

                    if not validate_name(last_name):
                        print("\u274C Invalid last name.")
                        continue
                    #del student_rec[full_name]
                    # implement delete by name functionality
                    break

                break

        print("\u2714 Student deleted successfully!")
        while True:
            print('\u2666 1.Continue')
            print('\u2666 2.exit')
            more_students = input("Please select 1 or 2:")
            if more_students == '1':
                deleteStudent()
            elif more_students == '2':
                print("Returning to the previous menu.")
                break
            else:
                print("\u274C Invalid input. Please enter 'yes' or 'no'.")
        print(student_rec)
        break



def validate_studentID(studentID):
    if studentID not in student_rec.values():
        return False
    else:
        return True

def validate_age(age):
    return age.isdigit() and 0 <= int(age) <= 100


def validate_phone(phone):
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)


def extract_first_last_name(full_name):
    names = full_name.split()
    if len(names) >= 2:
        return names[0], ' '.join(names[1:])  # Handling cases where last name has spaces
    return full_name, ''  # If only one name is given, treat it as the first name

def validate_name(name):
    return len(name) >= 2 and name.isalpha() and name[0].isupper()