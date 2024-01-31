# name, adjective, noun

mad_libs = "{} laughed at the {} {}."

print(mad_libs.format("Leo", "green", "alien"))


mad_libs = "{0} laughed at the {1} {2}."

print(mad_libs.format("Leo", "green", "alien"))


mad_libs = "{name} laughed at the {adjective} {noun}."

print(mad_libs.format(name = "Nenye", adjective = "beautiful", noun = "girl"))


mad_libs2 = "{name}, you are a foolish {adjective} {noun}."

name = input("What is your name? \n")
adjective = input("Are you tall or short? \n")
noun = input("Are you a man or woman? \n")

print(mad_libs2.format(name = name, adjective = adjective, noun = noun))

