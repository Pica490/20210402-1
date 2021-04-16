class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}

class Reviewer(Mentor):
    pass

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','Java']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

Reviewer_1 = cool_mentor

Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)

lecturer_1 = Lecturer ('Vasilisa','Intelligent')
lecturer_1.courses_attached += ['Python','Java']

best_student.rate_l(lecturer_1, 'Python', 10)
best_student.rate_l(lecturer_1, 'Java', 5)

print (Reviewer_1.name)
print (best_student.grades)
print (lecturer_1.grades1)
