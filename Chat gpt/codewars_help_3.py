# Goal: Write a function that takes a person's name and returns a greeting.
def personal_greeting(person_name):
	return(f"Hello, {person_name} how are you?")

result = personal_greeting("Rick")

print(result)

#Chat gpt bonus version
def personal_greeting(person_name="stranger"):
	return (f"Hello, {person_name} how are you?")

print(personal_greeting())
print(personal_greeting("Jane"))

#Steve play
def function_name(placeholder1, placeholder2):
	return placeholder1 * placeholder2

result = function_name(6, 6)
print(result)

