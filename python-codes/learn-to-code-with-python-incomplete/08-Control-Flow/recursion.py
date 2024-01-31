def count_down_from(number):
	start = number
	while start > 0:
		print(start)
		start -= 1



print()

count_down_from(5)

def countdown(start):
	while start > 0:
		print(start)
		start -= 1


countdown(10)


print()

def countdownr(number):

	if number <= 0:
		return

	else:
		print(number)
		countdownr(number-1)


countdownr(100)