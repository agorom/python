

def fizzbuzz(number):
	start = 0
	end = number
	while start < end:
		
		start += 1

		if start % 3 == 0 and start % 5 == 0:
			print("FizzBuzz")

		elif start % 3 == 0:
			print("Fizz")

		elif start % 5 == 0:
			print("Buzz")

		else:
			print(start)


	



(fizzbuzz(100))

