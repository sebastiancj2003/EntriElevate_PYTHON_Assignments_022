# ### Exercise_1 ### Base class

# Base class
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"

# Subclass for Core Courses
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        return super().display_info() + f", Required for Major: {self.required_for_major}"

# Subclass for Elective Courses
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        return super().display_info() + f", Elective Type: {self.elective_type}"

# Example Usage
core = CoreCourse("CS101", "Data Structures", 3, True)
elective = ElectiveCourse("ART201", "Introduction to Painting", 2, "Liberal Arts")

print(core.display_info())
print(elective.display_info())



#Exercise_2

import employee

emp = employee.Employee("John Doe", 50000)

print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: {emp.get_salary()}")