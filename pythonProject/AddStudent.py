"""
Add Student
"""

import re

student_records = {}


def addStudent():
    print('=============================== Add Student ============================ ')
    print('1. The first letter of firstname and lastname must be capitalized')
    print('2. Firstname and lastname must each have at least two letters')
    print('3. No digit allowed in the name')
    print('4. Age must between 0 and 100')
    print('5. Gender can be M (Male), F (Female) or O (Other)')
    print('6. Phone must be in the (xxx-xxx-xxxx) format')
    print("Adding a new student...")
    while True:

        while True:
            full_name = input("Enter student's full name (Firstname Lastname): ")
            first_name, last_name = extract_first_last_name(full_name)
            if not validate_name(first_name):
                print("\u274C Invalid first name.")
                continue

            if not validate_name(last_name):
                print("\u274C Invalid last name.")
                continue

            break


        while True:
            age = input("Enter student's age: ")
            if not validate_age(age):
                print("\u274C Invalid age.")
                continue
            break

        while True:
            gender = input("Enter student's gender (M/F/O): ")
            if not validate_gender(gender):
                print("\u274C Invalid gender.")
                continue
            break

        while True:
            phone = input("Enter student's phone number (xxx-xxx-xxxx): ")
            if not validate_phone(phone):
                print("\u274C Invalid phone number. ")
                continue
            break


        student = {
            'name': full_name,
            'age': age,
            'gender': gender,
            'phone': phone
        }
        student_id = generate_unique_id()
        student_records[student_id] = student
        print("\u2714 Student added successfully!")
        while True:
            print('\u2666 1.Continue')
            print('\u2666 2.exit')
            more_students = input("Please select 1 or 2:")
            if more_students == '1':
                addStudent()
            elif more_students == '2':
                print("Returning to the previous menu.")
                break
            else:
                print("\u274C Invalid input. Please enter 'yes' or 'no'.")
        print(student_records)
        break


def extract_first_last_name(full_name):
    names = full_name.split()
    if len(names) >= 2:
        return names[0], ' '.join(names[1:])  # Handling cases where last name has spaces
    return full_name, ''  # If only one name is given, treat it as the first name


def generate_unique_id():
    return len(student_records) + 1


def validate_name(name):
    return len(name) >= 2 and name.isalpha() and name[0].isupper()


def validate_age(age):
    return age.isdigit() and 0 <= int(age) <= 100


def validate_gender(gender):
    return gender.upper() in ['M', 'F', 'O']


def validate_phone(phone):
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)


