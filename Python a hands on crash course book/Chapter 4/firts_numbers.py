# Print a range between two numbers
for value in range(1,4): #Prints 1 2 3 4 5 becuse it's off by one
	print(value)

# Range with a single argument - prints from zero up to the number decalared:
for value in range(4):
	print(value)

# make a range of numbers into a list

values = list(range(1,4))
print(values)

"""# vvv This doesn't work as I thought it might though (I thought it might return 1, 2, 3). 
I guess we havn't wrapped it in a list for it do do that:

values = range(1,4)
print(values)

"""
