import sys

states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
}

capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
}



def	main():
	if len(sys.argv) != 2:
		exit()
	capital = states.get(sys.argv[1], None)
	if not capital:
		print("Unknown state")
	else:
		print(capital_cities[capital])

if __name__ == "__main__":
	main()