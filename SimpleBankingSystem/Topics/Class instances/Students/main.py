import sys

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year


no_of_lines = 3
lines = []
for _ in range(no_of_lines):
    line = sys.stdin.readline()
    lines.append(line.strip())

s = Student(lines[0], lines[1], lines[2])

print(s.student_id)
