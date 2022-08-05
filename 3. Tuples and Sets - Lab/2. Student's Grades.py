number_of_students = int(input())

students = {}
for next_line in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    grades = [f"{grades:.2f}" for grades in grade]
    print(f"{student} -> {' '.join([str(grade) for grade in grades])} (avg: {average_grade:.2f})")
