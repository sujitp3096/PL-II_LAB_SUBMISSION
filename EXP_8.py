# Defining a class
class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # marks out of 100
    
    # Method to display student details
    def display(self):
        print("Student Details:")
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Marks : {self.marks}")
    
    # Method to update marks
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated to {self.marks}")
    
    # Method to check pass or fail
    def is_passed(self):
        return self.marks >= 40

# Creating objects
student1 = Student("Sujit Pawar", 101, 85)
student2 = Student("Sharwil", 102, 35)

# Display student details
student1.display()
print("Passed:", student1.is_passed())
print()
student2.display()
print("Passed:", student2.is_passed())
print()

# Update marks for student2
student2.update_marks(45)
student2.display()
print("Passed:", student2.is_passed())