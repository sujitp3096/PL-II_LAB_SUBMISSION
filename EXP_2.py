print("Welcome to Student Marks Calculator")

DBMS = float(input("Enter the marks of DBMS: "))
OS = float(input("Enter the marks of Operating System: "))
TOC = float(input("Enter the marks of Theory of Computation (TOC): "))

Total_marks = DBMS + OS + TOC
Total_aggregate = (Total_marks / 3)

print(f"\nTotal Marks: {Total_marks} / 300")
print(f"Aggregate Percentage: {Total_aggregate}%")

if Total_aggregate < 40:
    print("Sorry, You Failed!! ")
elif 40 <= Total_aggregate < 60:
    print("Well done! You passed with **Second Class** ")
elif 60 <= Total_aggregate < 75:
    print("Nice! You passed with **First Class** ")
else:
    print("Excellent! You passed with **Distinction** ")
