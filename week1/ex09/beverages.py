class	HotBeverage:
	price = 0.30
	name = "hot beverage"
	text = "Just some hot water in a cup."

	def description(self):
		return self.text

	def	__str__(self):
		return f"name : {self.name}\n" + \
			f"price : {format(self.price, '.2f')}\n" + \
			f"description : {self.description()}"

class	Coffee(HotBeverage):
	name = "coffee"
	price = 0.40
	text = "A coffee, to stay awake."

class	Tea(HotBeverage):
	name = "tea"

class	Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50
	text = "Chocolate, sweet chocolate..."

class	Cappuccino(HotBeverage):
	name = "cappuccino"
	price = 0.45
	text = "Un po' di Italia nella sua tazza!"


def	main():
	print(HotBeverage(), end="\n\n")
	print(Coffee(), end="\n\n")
	print(Tea(), end="\n\n")
	print(Chocolate(), end="\n\n")
	print(Cappuccino())

if __name__ == "__main__":
	main()
