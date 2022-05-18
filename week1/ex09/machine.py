from beverages import *
import random

class	EmptyCup(HotBeverage):
	name = "empty cup"
	price = 0.90
	text = "An empty cup?! Gimme my money back!"

class	BrokenMachineException(Exception):
	def __init__(self):
		super().__init__("This coffee machine has to be repaired.")

class	CoffeeMachine:
	def	__init__(self):
		self.endurance = 10

	def	repair(self):
		self.endurance = 10

	def	serve(self, beverage):
		if self.endurance <= 0:
			raise BrokenMachineException()
		selected = random.choice([beverage(), EmptyCup()])
		self.endurance -= 1
		return selected

def	main():
	machine = CoffeeMachine()
	try:
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
	except BrokenMachineException as err:
		print(f"\n{err}")
	machine.repair()
	print("\nMachine repaired\n")
	try:
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
	except BrokenMachineException as err:
		print(f"\n{err}\n")

if __name__ == "__main__":
	main()
