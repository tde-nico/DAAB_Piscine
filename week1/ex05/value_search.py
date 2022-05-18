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
	for key, capital in capital_cities.items():
		if sys.argv[1] == capital:
			for state, item in states.items():
				if key == item:
					print(state)
					break
			break
	else:
		print("Unknown capital city")

if __name__ == "__main__":
	main()