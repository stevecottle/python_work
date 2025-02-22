# You need to return the middle character(s) of a string.

def get_middle_character(word):
    length = len(word)
    middle = length // 2

    if length % 2 == 1:
    	return word[middle]
    else:
    	return word[middle -1:middle +1]

result = get_middle_character("abracadabra")
print(result)


# Write a function that takes a string and returns the count of vowels (a, e, i, o, u) in it.

def vowel_counter(word):
	vowels = ("aeiou")
	return sum(1 for letter in word if letter in vowels)

result = vowel_counter("abracadabra")
print(result)



# Modify the function to return a dictionary with vowel counts instead of just a number

def vowel_counter2(word):
	vowels = "aeiou"
	dictionary = {vowel: 0 for vowel in vowels}

	for letter in word:
		if letter in vowels:
			dictionary[letter] += 1

	return dictionary

print(vowel_counter2("wonderful"))




# An isogram is a word with no repeating letters (case-insensitive). 
# Write a function that checks whether a given word is an isogram.



def is_isogram(word):
	word = word.lower()
	seen_letters = set()

	for letter in word:
		if letter in seen_letters:
			return False
		seen_letters.add(letter)


	return True

print(is_isogram("machine"))
print(is_isogram("AbraCADaBra"))


# Write a function that takes an integer num and counts how many times a given digit d appears in that number.

def count_digit(num, d):
	num_str = str(num)
	return num_str.count(str(d))

print(count_digit(1234567890, 3))  # Should return 1
print(count_digit(987654321, 5))   # Should return 1
print(count_digit(11111111, 1))    # Should return 8
print(count_digit(55555, 7))       # Should return 0

# Write a function that takes a string as an argument and returns the string reversed, without using Python’s built-in reverse() method or slicing.

def string_reverser(input_string):
	result = ""
	for digit in range(len(input_string) -1, -1, -1):
		result += input_string[digit]
	return result

print(string_reverser("hello"))
print(string_reverser("world"))


# Write a function getDivisors(n) that takes a positive integer n and returns the number of divisors of n.


def get_divsors(n):
	result = 0

	for number in range(1, n+1):
		if n % number == 0:
			result += 1

	return result

print(get_divsors(12))



# Find the longest word in a string

# IN -> "lkjbfkjwf lnfn flf f"
# 
# - get string
# - split string into words
# - count letters in each word
# - assign letter count to each word
# - calculate biggest number
# - return word with biggest number
# 
# OUT -> longest_word

def longest_word_in_string(string):
	words = string.split()
	longest_word = ""

	for word in words:
		if len(word) > len(longest_word):
			longest_word = word

	return longest_word

print(longest_word_in_string("The quick brown fox jumped over the lazy dog"))



# Remove all the vowels from a string
def remove_vowels(input_string):
	vowels = "aeiou"
	result = ""

	for letter in input_string:
		if letter not in vowels:
			result += letter

	return result

print(remove_vowels("abracadabra"))



# Count the number of occurrences of each character in a string.

def how_many_letter_occurances_in_string(string):
	dictionary = {}          	 		# Create an empty dictionary

	for letter in string:         		# Loop through each letter
		if letter in dictionary:   		# If the letter is in the dictionary ...
			dictionary[letter] += 1 	# ... add 1 to the count
		else:                        	# or else / if not (if it's not in the dictionary)
			dictionary[letter] = 1      # Give the letter a 1

	return dictionary

print(how_many_letter_occurances_in_string("fygdwedgyewxbwgxoibaehun;enxf"))


# Write a function that takes a string and returns the first character that does not repeat. 
# If all characters repeat, return None.

def function_name(string):
	dictionary = {}

	for letter in string:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1

	for letter in string:
		if dictionary[letter] == 1:
			return letter

	return None

print(function_name("swiss"))

# For the below vvv function: Write a function that determines whether all characters in a given string are unique.

def are_characters_unique(string):
	dictionary = {}

	for letter in string:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1

	for letter in dictionary:
		if dictionary[letter] > 1:
			return False

	return True

print(are_characters_unique("qwertyuiop"))


# ^^^ For the above function  
# loop thruough each of the letters
# if the letter is in the dictionary
# add 1
# if not in the dictionary
# give the letter a 1
# 
# loop through the dictionary
# if a letter has a value of > 1
# return False

# Return True


# vvv Check for Anagrams


"""def anagram_checker(string1, string2):
	dictionary = []

	for letter in string1:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1

	for letter in string2:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1

	for letter in dictionary:
		if letter in dictionary:
			dictionary[letter] == dictionary[letter]
			return False
		else: 
			return True

print(anagram_checker("listen", "silent"))"""



# ^^^ 
# loop through the letters
# Store letters in a dictionary
# If the letter is in the dictionary
# add 1
# Loop through the dictionary
# If each letter has an equal value = True
# else False

# Chat gpt version vvvv


def anagram_checker(string1,string2):
	dictionary1 = {}
	dictionary2 = {}

	for letter in string1:
		if letter in dictionary1:
			dictionary1[letter] += 1
		else: 
			dictionary1[letter] = 1

	for letter in string2:
		if letter in dictionary2:
			dictionary2[letter] += 1
		else: 
			dictionary2[letter] = 1

	return dictionary1 == dictionary2

print(anagram_checker("listen", "silent"))
print(anagram_checker("hello", "world"))


# Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def function(string):
	vowels = "aeiou"

	if vowels in string:
		return string

print(function("banana"))











