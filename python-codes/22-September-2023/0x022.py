def sum(*args):
	result = 0

	for x in args:
		result += x

	return result

print(sum(1, 2, 4, 5))

numbers = list(input("Enter numbers and separate them with comma"))

args = []
for i in numbers:
	args.append(i)

print(args)



def multiply(*args):
	result = 1
	for x in args:
		result *= x

	return result

print(multiply(4,5))

def print_kwarg(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")


print_kwarg(name= "Onah Leo Chinagorom",
	Department= "Mechanical Engineering", leve= "500 level",
	Registration_Number= 20181112883)


def print_args_kwargs(*args, **kwargs):
	print("Positional argument:", args)
	print("Keyword argument:", kwargs)

print_args_kwargs(1,3,5,6,7,8,9,0, name = "Onah Leo Chinagorom", level = "500 level")


#lambda function#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
doubled = map(lambda x: x*2, numbers)
print(list(doubled))