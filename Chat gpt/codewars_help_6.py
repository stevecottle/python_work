#Goal: Write a function that takes two numbers and returns the larger one.

def function_name(number_1, number_2):
		if number_1 > number_2:
			return number_1
		else:
			return number_2

result = function_name(10, 2)
print(result)
result = function_name(1, 2)
print(result)
result = function_name(100, 2)
print(result)
result = function_name(1, 100)
print(result)
result = function_name(1234567890, 123456789)
print(result)