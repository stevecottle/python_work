#Write a Python function that takes a name (string) and an age (integer) and returns a sentence

def function(string_name, age_integer):
		if age_integer < 18:
			return f"Hello {string_name}, I didn't know you were {age_integer}, you're so young!!"
		else:
			return f"Hello {string_name}, I didn't know you were {age_integer}!!"

result = function("Alice", 12)
print(result)

result = function("Alice", 44)
print(result)
