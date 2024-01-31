invalid_number = True

while invalid_number:
	user_value = int(input("Enter a number greater than 10: \n"))

	if user_value > 10:
		print(f"Thanks!, that is a great choice {user_value} is perfect")
		invalid_number = False

	else:
		print("That does not fit... \n Try again!!")