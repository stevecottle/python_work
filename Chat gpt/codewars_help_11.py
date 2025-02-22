#Write a function that takes a distance in kilometers and converts it to miles.

def function_name(kilometers):
	return f"{kilometers} kilometers is equal to {kilometers * 0.621371} miles"

result = function_name(5)
print(result)

result = function_name(10)
print(result)

result = function_name(1)
print(result)

#cgpt improvement code (round to 2 decimals)


def function_name(kilometers):
	return f"{kilometers} kilometers is equal to {round(kilometers * 0.621371, 2)} miles"

result = function_name(5)
print(result)

result = function_name(10)
print(result)

result = function_name(1)
print(result)