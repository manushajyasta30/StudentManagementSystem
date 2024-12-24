"""
Modify Student
"""
from AddStudent import student_records

import re


student_rec = {'ID': '1234', 'age': '21', 'major': 'III','phone': "123-123-1234"}



def modifyStudent():
    print('=============================== Modify Student ============================ ')

    while True:

        while True:
            student_id = input("Enter student's ID to modify: ")
            #first_name, last_name = extract_first_last_name(full_name)
            if not validate_studentID(student_id):
                print("\u274C No record found")
                continue
            break
        while True:
                # student_id = input("Enter student's ID to modify: ")
            new_age = input("New Age: ")
            if not validate_age(new_age):
                print("\u274C Invalid student age")
                new_age = input("Please enter student's age:")
                continue
            break
        while True:
            major = input("New major: ")
            break
        while True:
            phone = input("New Phone (xxx-xxx-xxxx): ")
            if not validate_phone(phone):
                print("\u274C Invalid phone number. ")
                continue
            break


        student = {

            'age': new_age,
            'major': major,
            'phone': phone
        }
        student_rec.update(student)
        print("\u2714 Student modified successfully!")
        while True:
            print('\u2666 1.Continue')
            print('\u2666 2.exit')
            more_students = input("Please select 1 or 2:")
            if more_students == '1':
                modifyStudent()
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


