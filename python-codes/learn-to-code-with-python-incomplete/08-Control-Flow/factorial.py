print("FACTORIAL CALCULATOR")

def factorial(number):
    

    #if number < 0:
      #  return (-1) * (number * factorial(number - 1))
    
    if number == 1 or number == 0:
        return number

    elif number > 0:
        return number * factorial(number - 1)


    else:
        number *= -1 
        return -1 * (number * factorial(((number)) - 1))
    
number = int(input("Enter the number: \n"))
print(factorial(number))
