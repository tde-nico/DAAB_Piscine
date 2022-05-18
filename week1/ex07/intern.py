

class Coffee:
	def	__str__(self):
		return "This is the worst coffee you ever tasted."

class	Intern:
	def	__init__(self, name=None):
		self.name = "My name? I’m nobody, an intern, I have no name." 
		if name != None:
			self.name = name

	def __str__(self):
		return self.name

	def	work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def	make_coffee(self):
		return Coffee()

def	main():
	this_guy = Intern()
	that_guy = Intern("Mark")
	print(this_guy)
	print(that_guy)
	print(that_guy.make_coffee())
	try:
		this_guy.work()
	except Exception as error:
		print(f"Exception caught: {error}")

if __name__ == "__main__":
	main()
