from typing import List


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rate = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for x in self.grades:
            grades_count += len(self.grades[x])
        self.average_rate = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {round(self.average_rate, 1)}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rate < other.average_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rate = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for x in self.grades:
            grades_count += len(self.grades[x])
        self.average_rate = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {round(self.average_rate, 1)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rate < other.average_rate


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


best_student1 = Student('Ruoy', 'Eman', 'male')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Vince', 'Clarke', 'female')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

best_student3 = Student('Dave', 'Gahn', 'male')
best_student3.courses_in_progress += ['Python']
best_student3.courses_in_progress += ['Git']
best_student3.finished_courses += ['Введение в программирование']

cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Andy', 'Fletcher')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Git']

cool_lecturer3 = Lecturer('Martin', 'Li Gore')
cool_lecturer3.courses_attached += ['Git']

cool_reviewer1 = Reviewer('Some', 'Buddy')
cool_reviewer1.courses_attached += ['Python']
cool_reviewer1.courses_attached += ['Git']

cool_reviewer2 = Reviewer('Alan', 'Wilder')
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['Git']

best_student1.rate_hw(cool_lecturer1, 'Python', 10)
best_student1.rate_hw(cool_lecturer1, 'Python', 10)
best_student1.rate_hw(cool_lecturer1, 'Python', 10)
best_student1.rate_hw(cool_lecturer1, 'Python', 10)

best_student1.rate_hw(cool_lecturer2, 'Python', 9)
best_student1.rate_hw(cool_lecturer2, 'Python', 10)
best_student1.rate_hw(cool_lecturer2, 'Python', 10)

best_student1.rate_hw(cool_lecturer3, 'Git', 10)
best_student1.rate_hw(cool_lecturer3, 'Git', 9)
best_student1.rate_hw(cool_lecturer3, 'Git', 10)

best_student2.rate_hw(cool_lecturer1, 'Python', 10)
best_student2.rate_hw(cool_lecturer1, 'Python', 10)
best_student2.rate_hw(cool_lecturer1, 'Python', 10)
best_student2.rate_hw(cool_lecturer1, 'Python', 10)

best_student2.rate_hw(cool_lecturer2, 'Python', 9)
best_student2.rate_hw(cool_lecturer2, 'Python', 10)
best_student2.rate_hw(cool_lecturer2, 'Python', 10)

best_student2.rate_hw(cool_lecturer3, 'Git', 10)
best_student2.rate_hw(cool_lecturer3, 'Git', 9)
best_student2.rate_hw(cool_lecturer3, 'Git', 10)

best_student3.rate_hw(cool_lecturer1, 'Python', 10)
best_student3.rate_hw(cool_lecturer1, 'Python', 9)
best_student3.rate_hw(cool_lecturer1, 'Python', 10)
best_student3.rate_hw(cool_lecturer1, 'Python', 10)

best_student3.rate_hw(cool_lecturer2, 'Python', 9)
best_student3.rate_hw(cool_lecturer2, 'Python', 10)
best_student3.rate_hw(cool_lecturer2, 'Python', 10)

best_student3.rate_hw(cool_lecturer3, 'Git', 10)
best_student3.rate_hw(cool_lecturer3, 'Git', 9)
best_student3.rate_hw(cool_lecturer3, 'Git', 7)

cool_reviewer1.rate_hw(best_student1, 'Python', 9)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)

cool_reviewer2.rate_hw(best_student1, 'Git', 10)
cool_reviewer2.rate_hw(best_student1, 'Git', 10)
cool_reviewer2.rate_hw(best_student1, 'Git', 10)
cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Git', 8)
cool_reviewer2.rate_hw(best_student2, 'Git', 7)

cool_reviewer1.rate_hw(best_student3, 'Python', 10)
cool_reviewer1.rate_hw(best_student3, 'Python', 7)
cool_reviewer1.rate_hw(best_student3, 'Python', 9)
cool_reviewer2.rate_hw(best_student3, 'Git', 8)
cool_reviewer2.rate_hw(best_student3, 'Git', 7)
cool_reviewer2.rate_hw(best_student3, 'Git', 9)

print(f'\n{cool_reviewer1}\n\n{cool_reviewer2}')
print(f'\n{cool_lecturer1}\n\n{cool_lecturer2}\n\n{cool_lecturer3}')
print(f'\n{best_student1}\n\n{best_student2}\n\n{best_student3}')
print()

print(f'Результат сравнения студентов (по средним оценкам за ДЗ):\n'
      f'{best_student1.name} {best_student1.surname} < {best_student2.name} {best_student2.surname} = {best_student1 < best_student2}\n'
      f'{best_student1.name} {best_student1.surname} > {best_student2.name} {best_student2.surname} = {best_student1 > best_student2}\n'
      f'{best_student1.name} {best_student1.surname} < {best_student3.name} {best_student3.surname} = {best_student1 < best_student3}\n'
      f'{best_student1.name} {best_student1.surname} > {best_student3.name} {best_student3.surname} = {best_student1 > best_student3}\n'
      f'{best_student2.name} {best_student2.surname} < {best_student3.name} {best_student3.surname} = {best_student2 < best_student3}\n'
      f'{best_student2.name} {best_student2.surname} > {best_student3.name} {best_student3.surname} = {best_student2 > best_student3}\n')

print(f'Результат сравнения лекторов (по средним оценкам за лекции):\n'
      f'{cool_lecturer1.name} {cool_lecturer1.surname} < {cool_lecturer2.name} {cool_lecturer2.surname} = {cool_lecturer1 < cool_lecturer2}\n'
      f'{cool_lecturer1.name} {cool_lecturer1.surname} > {cool_lecturer2.name} {cool_lecturer2.surname} = {cool_lecturer1 > cool_lecturer2}\n'
      f'{cool_lecturer1.name} {cool_lecturer1.surname} < {cool_lecturer3.name} {cool_lecturer3.surname} = {cool_lecturer1 < cool_lecturer3}\n'
      f'{cool_lecturer1.name} {cool_lecturer1.surname} > {cool_lecturer3.name} {cool_lecturer3.surname} = {cool_lecturer1 > cool_lecturer3}\n'
      f'{cool_lecturer2.name} {cool_lecturer2.surname} < {cool_lecturer3.name} {cool_lecturer3.surname} = {cool_lecturer2 < cool_lecturer3}\n'
      f'{cool_lecturer2.name} {cool_lecturer2.surname} > {cool_lecturer3.name} {cool_lecturer3.surname} = {cool_lecturer2 > cool_lecturer3}\n')


student_list = [best_student1, best_student2, best_student3]

lecturer_list = [cool_lecturer1, cool_lecturer2, cool_lecturer3]


def student_rate(student_list, course):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if course in student.grades.keys():
            sum_all += student.average_rate
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rate(lecturer_list, course):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course]:
            sum_all += lecturer.average_rate
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {round(student_rate(student_list, 'Python'), 1)}")
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {round(student_rate(student_list, 'Git'), 1)}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {round(lecturer_rate(lecturer_list, 'Python'), 1)}")
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {round(lecturer_rate(lecturer_list, 'Git'), 1)}")
print()
