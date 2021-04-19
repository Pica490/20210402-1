student_list = []
lecturer_list = []
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
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{average(some_name):.2f}\n' \
               f'Завершенные курсы:{self.finished_courses}\nКурсы в процессе изучения:{self.courses_in_progress}'

    def __lt__(self, other):
       return average(self) < average(other)

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
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average(some_name):.2f}\n'

    def __lt__(self, other):
       return average(self) < average(other)

def average(some_name):
    a = some_name.grades.values()
    sum = 0
    count = 0
    for value in list(a):
        for number in value:
            sum = sum + number
            count = count + 1
    return sum / count

class Reviewer(Mentor):
    def __str__(self):
        return f'\nИмя:{self.name}\nФамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'm')
student_list.append(best_student)
best_student.courses_in_progress += ['Python','Git']
best_student.finished_courses += ['Java']

exellent_student = Student('Princess', 'Frog', 'f')
student_list.append(exellent_student)
exellent_student.courses_in_progress += ['Git']
exellent_student.finished_courses += ['Python']

Reviewer_1 = Reviewer('Some','Buddy')
Reviewer_1.courses_attached += ['Python', 'Git']

Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(exellent_student, 'Git', 10)

lecturer_1 = Lecturer ('Vasilisa','Intelligent')
lecturer_1.courses_attached += ['Python','Java']
lecturer_list.append(lecturer_1)

best_student.rate_l(lecturer_1, 'Python', 10)
best_student.rate_l(lecturer_1, 'Python', 5)

lecturer_2 = Lecturer ('Roi','Soleil')
lecturer_2.courses_attached += ['Git']
lecturer_list.append(lecturer_2)

best_student.rate_l(lecturer_2, 'Python', 10)
exellent_student.rate_l(lecturer_2, 'Git', 10)

print(f'Оценки студента {exellent_student.surname}: {exellent_student.grades}')
print(f'Оценки лектора {lecturer_1.surname}: {lecturer_1.grades}')

some_name = Reviewer_1
print(some_name)

some_name = lecturer_1
print(some_name)

some_name = exellent_student
print(some_name)

print(f'\nОценки студента {best_student.surname} ниже, чем у {exellent_student.surname}?: {Student.__lt__(best_student, exellent_student)}')
print(f'Оценки лектора {lecturer_1.surname} ниже, чем у {lecturer_2.surname}?: {Lecturer.__lt__(lecturer_1, lecturer_2)}')

def avg_hw_course(student_list, course):
    sum = 0
    count = 0
    for student in student_list:
        if course in student.grades:
            for number in student.grades[course]:
                sum += number
                count += 1
    return sum / count
course = 'Git'
a = avg_hw_course(student_list, course)
print(f'\nСредняя оценка всех студентов по курсу {course}: {a}')

def avg_l_course(lecturer_list, course):
    sum = 0
    count = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            for number in lecturer.grades[course]:
                sum += number
                count += 1
    return sum / count

course = 'Python'
b = avg_l_course(lecturer_list, course)
print(f'\nСредняя оценка всех лекторов {course}: {b}')