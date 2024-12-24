# StudentManagement.py

from AddStudent import student_records
class StudentManagement:
    def __init__(self):
        self.students = student_records  # Dictionary to store student records

    def show_students(self):
        print("Select an option to display student records:")
        print("\u2666 1. Show all students")
        print("\u2666 2. Show students by name")
        print("\u2666 3. Show students by ID")
        print('\u2666 Other Return')

        option = input("Enter your choice (1-3): ")
        if option == '1':
            self.show_all_students()
        elif option == '2':
            self.show_students_by_name()
        elif option == '3':
            self.show_students_by_id()
        else:
            print("\u274C  Returning to the previous menu.")

    def show_all_students(self):
        if not self.students:
            print("\u274C No student Existing.")
            return

        print("All Student Records:")
        for student_id, student_info in self.students.items():
            print(f"Student ID: {student_id}")
            print(f"Student Name: {student_info['name']}")
            print(f"Student Age: {student_info['age']}")
            print(f"Student Gender: {student_info['gender']}")
            print(f"Student Contact: {student_info['phone']}")
            # Display other student information as needed
            print("---------------")

    def show_students_by_name(self):
        name = input("Enter the name to search: ")
        found_students = [student_info for student_info in self.students.values() if student_info['name'].lower() == name.lower()]
        if not found_students:
            print("\u274C No matching student records found.")
            return

        print(f"Student(s) with name '{name}':")
        for student in found_students:
            print(f"Student ID: {student['id']}")
            print(f"Student Name: {student['name']}")
            print(f"Student Age: {student['age']}")
            print(f"Student Gender: {student['gender']}")
            print(f"Student Contact: {student['phone']}")
            # Display other student information as needed
            print("---------------")

    def show_students_by_id(self):
        student_id = input("Enter the student ID: ")
        student_info = self.students.get(student_id)
        if not student_info:
            print("\u274C No student found with the given ID.")
            return

        print("Student Information:")
        print(f"Student ID: {student_info['id']}")
        print(f"Student Name: {student_info['name']}")
        print(f"Student Age: {student_info['age']}")
        print(f"Student Gender: {student_info['gender']}")
        print(f"Student Contact: {student_info['phone']}")
        # Display other student information as needed

    def add_student(self):
        # Implement functionality to add a student record
        pass

    def modify_student(self):
        # Implement functionality to modify student details
        pass

    def delete_student(self):
        # Implement functionality to delete a student record
        pass

# Usage example
student_manager = StudentManagement()

