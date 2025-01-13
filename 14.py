# Practice Ideas:

# Calculate the average marks for each student.
# Find the student with the highest marks in science.
# Add a new subject and its marks for each student.
students = {
    "101": {"name": "Ankit", "age": 22, "marks": {"math": 90, "science": 85}},
    "102": {"name": "Priya", "age": 21, "marks": {"math": 88, "science": 92}},
    "103": {"name": "Rohan", "age": 23, "marks": {"math": 76, "science": 80}},
}



def calculate_highest_marks(students):
        highest=0
        highest_student_name=""
        for i in students:
            current_student=students[i]['marks']['science']
            if current_student>highest:
                highest=current_student
                highest_student_name=students[i]['name']
        print(f"Highest Marks {highest}, Student name is {highest_student_name}")

def average_marks_of_each_students(students):
        avg=0
        for i in students:
            maths=students[i]['marks']['math']
            science=students[i]['marks']['science']
            avg=maths+science/2
            print(f"Average Marks of {students[i]['name']} : {round(avg)}")

def add_new_subject(subject_name,students):
    #   subject_marks=int(input("Enter the marks: "))
      for i in students:
            subject_marks=int(input(f"Enter the History Marks of {students[i]['name']}--> "))
            students[i]['marks'][subject_name]=subject_marks
      print(students)


# calculate_highest_marks(students)
# average_marks_of_each_students(students)
# add_new_subject("History",students)
        




