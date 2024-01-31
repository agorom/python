sentence = input("Enter a sentence: \n")
print("Your sentence is: \n",sentence)
what_to_change = input("What do you want to replace? \n")
new_word = input("What do you want to cahnge it with? \n")

result = sentence.replace(what_to_change, new_word)

print("This is your new sentence")

print(result)
