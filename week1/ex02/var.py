
def	my_var():
	t1 = 42
	t2 = "42"
	t3 = "quarante-deux"
	t4 = 42.0
	t5 = True
	t6 = [42]
	t7 = {42: 42}
	t8 = (42,)
	t9 = set()
	print(t1, "has a type",type(t1))
	print(t2, "has a type",type(t2))
	print(t3, "has a type",type(t3))
	print(t4, "has a type",type(t4))
	print(t5, "has a type",type(t5))
	print(t6, "has a type",type(t6))
	print(t7, "has a type",type(t7))
	print(t8, "has a type",type(t8))
	print(t9, "has a type",type(t9))

if __name__ == "__main__":
	my_var()