nick_names = {
	"Anwu": "Anyanwu Magnus Chinaza",
	"Mpioko": "Chimezie Johnpaul Chimezie",
	"Onitsha": "Anyadiegwu Christopher Emeka",
	"Lebechi": "Anyalewechi Divinewealth Chimezirim",
	"Santa": "Edom ThankGod Chidiebube",
	"Nwa Onah": "Onah Leo Chinagorom"
}


print(f"These are list of people with nick name \n{nick_names}")

name = input("What is your nick name? \n")
print(nick_names.get(name, "Not among the listed"))