import sys

def	main():
	try:
		print(int(sys.argv[1]) + int(sys.argv[2]))
	except Exception as error:
		print(f"[!!] Error: {error}")

if __name__ == "__main__":
	main()