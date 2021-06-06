"""A. Кружки
Напишите код для решения задачи про поиск кружков,
которые посещает хотя бы один ученик. Ваше решение
должно задействовать O(1) дополнительной памяти
(то есть помимо памяти, выделенной под массив visited_optional_courses)
"""

with open('input.txt') as f:
    visited_optional_courses = list(f)

unique_courses = []
for course in visited_optional_courses[1:]:
    if course not in unique_courses:
        unique_courses.append(course)

for visited_course in unique_courses:
    print(visited_course, end="")
