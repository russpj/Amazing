def main():
	H = 0
	V = 0

	while(H < 2 and V < 2):
		H, V = input("What are your width and length (width,length): ").split(',')
		if H < 2 and V < 2:
			print("Meaningless dimensions. Try again.")
	
	