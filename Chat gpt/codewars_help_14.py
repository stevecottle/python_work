# Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
#SC Version:
#
#def function_name(string):
#	if letters in string == "a" "e" "i" "o" "u":
#		return letters
#
#result = function_name("animal")
#print(result)

# cgpt version:

def current_vowels(string):
	vowels = "aeiuoAEIOU"
	count = 0

	for letter in string:
			if letter in vowels:
				count += 1

	return count

result = current_vowels("animal")
print(result)

# Write a function that takes a string as input and returns the number of words in the string.


