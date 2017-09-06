# imports
import random

################################################################################
# init2dArray
# Function to create a 2 dimensional array of values. This function creates an
# List of Lists to accomplish this. Each element in the list can be accedd like
# x, y grid coordinates with the notation of array[x][y]. This would access the
# List at index x and the element at index y of that list. This same element can
# also be accessed as array[x].index(y)
#
#       x: The number of elements in the x dimension of the array.
#       y: The number of elements in the y dimension of the array.
#   value: The value to initialize each element with.
#
# returns: A new List with x elements. Each one a list with a y number of 
#          elements. All elements are initialized with the value passed in.

def init2dArray(x, y, value = ''):
	array2d = []
	for i in range(x):
		array2d.append([])
		for j in range(y):
			array2d[i].append(value)
	
	return array2d

################################################################################
# Main program entry point

def main():
	H = 0
	V = 0

	while(H < 2 and V < 2):
		H, V = input("What are your width and length (width,length): ").split(',')
		H = int(H)
		V = int(V)
		if H < 2 and V < 2:
			print("Meaningless dimensions. Try again.")
	W = init2dArray(H, V)
	U = init2dArray(H, V)
	print("\n\n\n\n")
	Q = 0
	Z = 0
	X = random.randint(1, H)
	for I in range(H):
		if I == X:
			print(".  ")
		else:
			print(".--")
	print(".")
	C = 1
	W[X][1] = C
	C += 1
	#200
	R = X
	S = 1
	#260/265
	if R - 1 == 0 or W[R - 1][S] != 0:
		if S - 1 == 0 or W[R][S - 1] != 0:
			if R == H:
				if S != V:
					if W[R][S + 1] != 0:
						while R != H:
							R += 1
							if W[R][S] != 0:
								break
		elif R == H or W[R + 1][S] != 0:
			#610
			if S != V:
				#630
				if W[R][S + 1] != 0:
					#660 - goto 820
					#820
					W[R][S - 1] = C
					C += 1
					#840
				else:
					#640
					X = random.randint(1, 2)
					#650
			elif Z == 1:
				#660 - goto 820
				#820
				W[R][S - 1] = C
				C += 1
				#840
			else:
				Q = 1
				#640
				X = random.randint(1, 2)
				#650
		elif S != V:
			#560
			if W[R][S + 1] != 0:
				#590
				X = random.randint(1, 2)
				#600
			else:
				#570
				X = random.randint(1, 2)
				#580
		elif Z == 1:
			#590
			X = random.randint(1, 2)
			#600
		else:
			Q = 1
			#570
	#270/280
	elif S - 1 == 0 or W[R][S - 1] != 0:
		if R == H:
			if S != V:
				if W[R][S + 1] != 0:
					W[R - 1][S] == C
					C += 1
					U[R - 1][S] = 2
					R -= 1
					if C == H * V + 1:
						for J in range(V):
							print("I")
							for I in range(H):
								if U[I][J] < 2:
									print("  I")
								else:
									print("   ")
							print("\n")
							for I in range(H):
								if U[I][J] == 0 or U[I][J] == 2:
									print(":--")
								else:
									print(":  ")
							print(".")
	#290/300
	elif R == H or W[R + 1][S] != 0:
		#330
		if S != V:
			#340
			if W[R][S + 1] != 0:
				#370
				X = random.randint(1, 2)
				#380
		elif Z == 1:
			#370
			X = random.randint(1, 2)
			#380
		else:
			Q = 1
			#350
	#310
	else:
	   X = random.randint(1, 3)
	   #320

################################################################################
# Call main program

main()