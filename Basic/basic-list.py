grades = list(range(1,10))
print(grades)

grades_odd = list(range(1,10,3))
print(grades_odd)


student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades.append(6.8)
print(student_grades)

student_grades.remove(9.1)
print(student_grades)

count = list.count(student_grades, 10.0)
print(count)