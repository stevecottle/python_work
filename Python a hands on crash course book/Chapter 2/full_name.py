first_name = "steve"
second_name = "cottle"
full_name = f"{first_name} {second_name}"

print(full_name)

#SC - Trying to add Capitalisation:
print("")
first_name = "steve"
second_name = "cottle"
full_name = f"{first_name} {second_name}"
print(f"{first_name} // {second_name} // {full_name}")

#SC - play:
print("")
print(f"What's going on {full_name.title()}? Great to see you!")
print(first_name, second_name, full_name)
print(f"f strings take the variable which is diplayed in a curly bracket (brace {{}}) and uses it in the sentence eg this: {{full_name.upper()}} will display this: {full_name.upper()}")

#Assign f string to a variable:

print("")
message = (f"Hello {full_name.upper()} I'm really pleased to see you!")
print(message)

print("")
print("Python")
print("\tPython")
print("Address:\nStreet\nTown\nPost Code")
print("List:\n\tIndent 1\n\tIndent 2\n\tIndent 3")

#Strip (right-hand-side) white space:

favourite_language = "Python   "
print(favourite_language)

favourite_language = "Python   "
print(favourite_language.rstrip())


#Strip white space (right-hand-side) permenantly
favourite_language = "Python   "
favourite_language = favourite_language.rstrip()
print(favourite_language)


#Strip wite space (right, left, both-hand side)
favourite_language = "  Python   "
favourite_language = favourite_language.rstrip()
favourite_language = favourite_language.lstrip()
favourite_language = favourite_language.strip()
print(f"Here's the result -{favourite_language}-")


