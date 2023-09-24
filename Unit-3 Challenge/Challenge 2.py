'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_num = roll_number
    self.cgpa = cpa


def sort_students(student_list):
   Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sored__students


# Example usage:
students = [
    Student("", "A123", 10),
    Student("", "A124", 9.0),
    Student("", "A125", 10),
    Student("", "A126", 8.5),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))

