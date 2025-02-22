# Write a function that takes a number as input and returns:

# "Positive" if the number is greater than zero
# "Negative" if the number is less than zero
# "Zero" if the number is exactly zero

def function_name(number):
	if number > 0:
		return "Positive"
	
	elif number < 0:
		return "Negative"

	else:
		return "Zero"

result = function_name(5)
print(result)

result = function_name(-3)
print(result)

result = function_name(0)
print(result)
