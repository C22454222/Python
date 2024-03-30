class Student:
    """
    A class to represent a student.

    Attributes:
    - study_type (str): The type of study (e.g., POSTGRADUATE, UNDERGRADUATE).
    - f_name (str): First name of the student.
    - l_name (str): Last name of the student.
    - courses (list): List of courses the student is registered for.
    """

    def __init__(self, study_type, f_name, l_name):
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.courses = []

    def set_courses(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{self.study_type} Student: {self.f_name} {self.l_name}, Courses: {', '.join(self.courses)}"


class RegistrationData:
    """
    A class to represent registration data for a student.

    Attributes:
    - address (str): The address of the student.
    - registration_fee (float): The registration fee paid by the student.
    - student (Student): An instance of the Student class.
    - s_id (str): Student ID.
    """

    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.address = address
        self.registration_fee = registration_fee
        self.student = Student(study_type, f_name, l_name)
        self.s_id = s_id

    def display_student_data(self):
        print(f"Student ID: {self.s_id}")
        print(f"Name: {self.student.f_name} {self.student.l_name}")
        print(f"Study Type: {self.student.study_type}")
        print(f"Address: {self.address}")
        print(f"Registration Fee: ${self.registration_fee}")
        print(f"Courses: {', '.join(self.student.courses)}")

    def set_student_id_property(self, s_id):
        self.s_id = s_id

    def get_student_object(self):
        return self.student

    def __str__(self):
        return f"Registration Data: {self.student}"

# MAIN SCOPE - UNCOMMENT IT AND RUN AFTER IMPLEMENTING YOUR SOLUTION
r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     "POSTGRADUATE", "Lucas", "Rizzo")
r.display_student_data()
print()
r.set_student_id_property("C12345")
r.display_student_data()
print()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.get_student_object().set_courses(course)

r.display_student_data()
print()
print(r.get_student_object())  # extra to match the __str__ additional function
print()
print(RegistrationData.__doc__)
