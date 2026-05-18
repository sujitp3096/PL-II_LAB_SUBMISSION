# creating a Student Dictionary
student = {
"Name": "Sujit Pawar",
"RegNo": 23141048,
"Department": "IT",
"Year": "SY",
"Marks(CGPA)": 9.0,
"Address": { # Added nested dictionary
"City": "Ichalkaranji",
"State": "Maharashtra",
"Pincode": 416115
}
}
print(student)
# update Year and Marks values
student["Year"] = "TY"
student["Marks(CGPA)"] = 9.0
print(student)
print(student["Name"])
# Accessing nested dictionary values
print(student["Address"]["City"]) 
print(student["Address"]["Pincode"]) 
#creating null dictionary
stud = {}
print(stud)
# Methods of dictionary
print(student.keys())
print(student.values())
print((student.get("Address")).get("City"))
#adding new key value pair to nested dictionary.
student["Address"]["Country"]="India"
print(student)
