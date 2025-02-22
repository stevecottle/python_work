# Make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10).
# In Python, two asterisks (**) represent exponents.

# Start with an empty list called squares
# we tell Python to loop through each value from 1 to 10 using the range() function.
# Inside the loop, the current value is raised to the second power and assigned to the variable square
# Each new value of square is appended to the list squares
# When the loop has finished running, the list of squares is printed

squares =[] 

for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

    
# More concise version:

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)







