class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lectors, course, grade):
        if isinstance(lectors, Lectors) and course in lectors.courses_attached:
            if course in lectors.grades:
                lectors.grades[course] += [grade]
            else:
                lectors.grades[course] = [grade]
        else:
            return "Ошибка"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
            average_rating = round(sum_rating / len_rating, 2)
            return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.av_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные катигории людей не сравниваем.")
            return
        return self.av_rating() < other.av_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectors(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
            average_rating = round(sum_rating / len_rating, 2)
            return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.av_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lectors):
            print("Разные категории людей на сравниваем.")
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student_1 = Student('Вася', 'Иван', 'Женя')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Анна', 'Ирина', 'Жанна')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

lectors_1 = Lectors('Олег', 'Анатолий')
lectors_1.courses_attached += ['Python']

lectors_2 = Lectors('Алёна', 'Виктория')
lectors_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Александр', 'Сергей')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Алеся', 'Елена')
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 7)

student_1.rate_lw(lectors_1, 'Python', 10)
student_1.rate_lw(lectors_1, 'Python', 7)
student_1.rate_lw(lectors_1, 'Python', 6)

student_2.rate_lw(lectors_2, 'Python', 10)
student_2.rate_lw(lectors_2, 'Python', 6)
student_2.rate_lw(lectors_2, 'Python', 6)

student_list = [student_1, student_2]
lectors_list = [lectors_1, lectors_2]
reviewer_list = [reviewer_1, reviewer_2]


import gc

print("список Reviewers")
for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)

print()
print("список Lectors")
for obj in gc.get_objects():
    if isinstance(obj, Lectors):
        print(obj)

print()
print("список Students")
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)

print()
print('Сравнение людей по средним оценкам:')
print('student_1 < student_2', student_1 < student_2)
print('lectors_1 > lectors_2 ', lectors_1 > lectors_2)
print('student_1 < lectors_1 ', student_1 < lectors_1)
print()


def average_rating_for_course_student(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for student in student_list:
        for course in student.grades:
            student_sum_rating = student.av_rating_for_course(course)
            sum_rating += student_sum_rating
            quantity_rating += 1
        average_rating = round(sum_rating / quantity_rating, 2)
        return  average_rating


def average_rating_for_course_lectors(course, lectors_list):
    sum_rating = 0
    quantity_rating = 0
    for lectors in lectors_list:
        for course in lectors.grades:
            lectors_sum_rating = lectors.av_rating_for_course(course)
            sum_rating += lectors_sum_rating
            quantity_rating += 1
        average_rating = round(sum_rating / quantity_rating, 2)
        return average_rating


print('Подсчёт средней оценки за домашние задания')
print(average_rating_for_course_student('Python', student_list))

print('Подсчёт средней оценки за лекцию')
print(average_rating_for_course_lectors('Python', lectors_list))