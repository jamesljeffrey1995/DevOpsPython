
def tryAgain():
		while(True):
			status = input("\nGo again? y/n: ")
			if status.lower() =="n":
				exit()
			elif status.lower() == "y":
				main()
			else:
				print("Enter either y or n")

def calc(n):
	squares = {i : i*i for i in range(1, n+1)}
	return squares
def main ():
		n = int(input("Enter the value of n: "))
		print(calc(n))
		tryAgain()

if __name__ == "__main__":
	main()