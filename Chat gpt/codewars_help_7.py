#Goal: Write a function that takes two numbers and an operator (+, -, *, /) and performs the corresponding operation.

#def function_name(number_input):
	#if number_input == 0:
		#return "Zero"
	#elif number_input < 0:
		#eturn "Negative"
	#else number_input > 0:
		#return "Positive"

#result = number_input(-1234)
#print(result)



# Correct dode:
def function_name(number_input):
	if number_input == 0:
		return "Zero"
	elif number_input < 0:
		return "Negative"
	else:
		return "Positive"

result = function_name(0)
print(result)