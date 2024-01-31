file = open("name_of_friends.txt", "r")

for line in (file.readlines()):
	print(line)

file.close()
