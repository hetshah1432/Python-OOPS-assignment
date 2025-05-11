class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self):
        print(f"{self.name} uploaded content on {self.subject}.")

    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Subject: {self.subject}")

class CourseCreator(Instructor):
    def create_course(self, course_name):
        print(f"{self.name} created course: {course_name}")

    def display_info(self):
        print(f"Course Creator: {self.name}, Email: {self.email}, Subject: {self.subject}")
