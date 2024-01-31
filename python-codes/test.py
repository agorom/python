import module2

from student import Student

print(module2.get_file_extendion("leo.txt"))


Onah_Leo_Chinagorom = Student("Onah Leo Chinagorom", "Mechanical Engineering", 3.6, False)

print(Onah_Leo_Chinagorom)


user_name = input("Create a user name:\n")

print(f"Welcome {user_name}\nAnswer the following question correctly")

name = input("What is your name:\n")
major = input("What is your major:\n")
gpa = input("What is your GPA:\n")
is_on_probation = input("Are you on probation:\n")

if is_on_probation == "yes":
	is_on_probation = "True"
else:
	is_on_probation = "False"

user_name = Student(name, major, gpa, is_on_probation)

print(user_name.is_on_probation)