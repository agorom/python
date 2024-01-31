def reverse(string):
	start_index = 0
	last_index = len(string) - 1
	reversed_string = ""


	while last_index >= start_index:
		reversed_string += string[last_index]