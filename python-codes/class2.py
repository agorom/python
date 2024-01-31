class Person:
	def __init__(self, name, age, level):
		self.name = name
		self.age = age
		self.level = level


name = input("What is your name? \n")
age = int(input("How old are you? \n"))
level = int(input("What is your level? \n"))

Person1 = Person(name, age, level)

print(Person1.name)