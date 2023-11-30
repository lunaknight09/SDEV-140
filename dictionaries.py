"""
Course Management System:

This script provides a simple course management system implemented in Python.
It allows for the addition, removal, and checking of courses in a dictionary-based data structure.
"""
#Module 6 Dictionary Lab
#November 29, 2023
#Nathan Hopkins
class CourseManagementSystem:
    def __init__(self):
        self.courses = {}

#Display the names of all available courses
    def display_course_names(self):
        print("Available Courses:")
        for code, name in self.courses.items():
            print(f"{code}: {name}")

#Add a new course to the course_info dictionary.
    def add_course(self, code, name):
        code = code.upper()
        if code not in self.courses:
            self.courses[code] = name
            print(f"Course '{code}' added successfully!")
        else:
            print(f"Course '{code}' already exists.")

#Remove an existing course from the course_info dictionary
    def remove_course(self, code):
        code = code.upper()
        if code in self.courses:
            del self.courses[code]
            print(f"Course '{code}' removed successfully!")
        else:
            print(f"Course '{code}' does not exist.")

#Check if a course exists in the course_info dictionary
    def check_course_existence(self, code):
        code = code.upper()
        if code in self.courses:
            print(f"Course '{code}' exists.")
        else:
            print(f"Course '{code}' does not exist.")

#Main Program loop and renamed CourseMangementSystem to "cms" for easier functionality inside the dictionary
if __name__ == "__main__":
    cms = CourseManagementSystem()

    while True:
        print("\nCourse Management System")
        print("1. Display Course Names")
        print("2. Add New Course")
        print("3. Remove Course")
        print("4. Check Course Existence")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            cms.display_course_names()
        elif choice == '2':
            course_code = input("Enter the course code: ")
            course_name = input("Enter the course name: ")
            cms.add_course(course_code, course_name)
        elif choice == '3':
            course_code = input("Enter the course code to remove: ")
            cms.remove_course(course_code)
        elif choice == '4':
            course_code = input("Enter the course code to check: ")
            cms.check_course_existence(course_code)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
