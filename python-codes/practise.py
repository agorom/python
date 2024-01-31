secret = "leo"
guess = ""
guess_count = 0
guess_limit = 5

out_of_guesses = False

while guess != secret  and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Make a guess: \n")
		guess_count += 1

		if guess_count == 1:
			print(f"You have {guess_limit - 1} left")
		elif guess_count == 2:
			print(f"You have {guess_limit - 2} left")
		elif guess_count == 3:
			print(f"You have {guess_limit - 3} left")
		elif guess_count == 4:
			print(f"This is your last chance, think deep")

	else:
		out_of_guesses = True

if out_of_guesses:
	print("You lose!!!")

else:
	print("Yes!!! you win")

	
