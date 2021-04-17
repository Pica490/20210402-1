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
    def __str__(self):
        a = some_name.grades.values()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{average(a):.2f}\n' \
               f'Завершенные курсы:{self.finished_courses}\nКурсы в процессе изучения:{self.courses_in_progress}'

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

    def __str__(self):
        a = some_name.grades1.values()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average(a):.2f}\n'

def average(a):
    sum = 0
    count = 0
    for value in list(a):
        for number in value:
           sum = sum + number
           count = count + 1
    return sum / count

def count_1(a):
    count = 0
    for value in list(a):
        for number in value:
            count = count + 1
    return count

class Reviewer(Mentor):
    def __str__(self):
        return f'\nИмя:{self.name}\nФамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['Java', 'Git']

Reviewer_1 = Reviewer('Some','Buddy')
Reviewer_1.courses_attached += ['Python']

Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)

lecturer_1 = Lecturer ('Vasilisa','Intelligent')
lecturer_1.courses_attached += ['Python','Java','1']

best_student.rate_l(lecturer_1, 'Python', 10)
best_student.rate_l(lecturer_1, 'Python', 2)
best_student.rate_l(lecturer_1, 'Java', 5)

some_name = Reviewer_1
print(some_name)

some_name = lecturer_1
print(some_name)

some_name = best_student
print(some_name)

