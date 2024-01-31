def long_word(word):
	return len(word) > 7

print(long_word("leo"))
print(long_word("Chinagorom"))


def first_longer_than_second(string1, string2):
	return len(string1) > len(string2)

print(first_longer_than_second("leo", "Chinagorom"))
print(first_longer_than_second("Chinagorom","leo"))