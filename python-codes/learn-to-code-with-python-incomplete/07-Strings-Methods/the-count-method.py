def vowel_count(word):
    return word.count("a") + \
    word.count("e") + \
    word.count("i") + \
    word.count("o") + \
    word.count("u")
    
print(vowel_count("leo"))
print(vowel_count("Chinenyenwa"))



def find_my_letter(word, letter):
    return word.find(letter)
    
print(find_my_letter("chinagorom", "i"))