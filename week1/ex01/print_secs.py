import sys

def	main():
	try:
		print(int(sys.argv[1]) * 3600 + int(sys.argv[2]) * 60 + int(sys.argv[3]))
	except Exception as error:
		print(f"[!!] Error: {error}")

if __name__ == "__main__":
	main()