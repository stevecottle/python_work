def rudys_positive_negative_number_checker(number):
	if number > 0:
		return f"The number {number}! RUDY SAYS IT'S POSITIVE :)"
	elif number < 0:
		return f"The number {number}! RUDY SAYS IT'S NEGATIVE :("
	else:
		return f"The number {number}! RUDY SAYS IT'S NOT POSITIVE OR NEGATIVE, IT'S ZERO :/"

result = rudys_positive_negative_number_checker(999999999)
print(result)

