import re

s = "The love that was professed by Okoli Chisom to me Onah Leo Chinagorom was all fake"

match = re.search("Chisom", s)

if match:
	print("Hurray!! Chisom was found")

else:
	print("Not found")


match_2 = re.findall(r"\b\w{4}\b", s)
print(match_2)

s_2 = re.sub("Chisom", "Zita", s)
print(s_2)

# to match any email

pattern = r"\b[\w.-]+@[\w.-]+\b"

# url
pattern = r"https?://[\w\-./]+"