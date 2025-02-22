# Write a function that takes three numbers and returns their average.
# Formula for average: average =  num1 + num2 + num3
#                                 ------------------
#                                        3



def average_number_calculator(number_1, number_2, number_3):
		return (number_1 + number_2 + number_3) / 3

result = average_number_calculator(3, 6, 9)
print(result)



def average_number_calculator(number_1, number_2, number_3):
		return f"The average of {number_1}, {number_2} and {number_3} is {((number_1) + (number_2) + (number_3)) / 3}"

result = average_number_calculator(3, 6, 9)
print(result)

result = average_number_calculator(10, 20, 30)
print(result)

result = average_number_calculator(4, 5, 6)
print(result)