
#For-Loops - print each magicians name
magicians = ["alice", "david", "carolina"]

for magician in magicians:
	print(magician)

#For-Loops - Magician did a greate trick
magicians = ["alice", "david", "carolina"]

for magician in magicians:

	print(f"Hey, {magician.title()} you did a great trick!!") # indented - so part of each individual loop (will perform this action on value 1, then value 2 then value three etc)
	print(f"{magician}, I can't wait to see your next trick!\n") # indented - so part of each individual loop along woth the previous instruction

print("Thank you everyone, great show!") # Not indented so doesn't for part of the loop. This action happens indipendantly, once, after the loop has finished

#4-1 Print the name of each pizza from a list of pizzas

pizzas = ["hawiian", "chicken", "el-boro"]

for pizza in pizzas:
	print(pizza)

	# Modify the loop to make it return a sentence
pizzas = ["hawiian", "chicken", "el-boro"]

for pizza in pizzas:
	print(f"I like {pizza.title()} pizza")

# Add a single like to state how much I like pizza

pizzas = ["hawiian", "chicken", "el-boro"]

for pizza in pizzas:
	print(f"I like {pizza.title()} pizza")
print("I really love pizza")


#4-2 Print differnt types of animals with similar characteristics in a for-loop

animals = ["dog", "cat", "hamster", "snake"]

for animal in animals:
	print(animal)

# Modify to explain they'd make a great pet
# Then add a single finishing statement

for animal in animals:
	print(f"A {animal} would make a great pet!")
print("They all look great around the house!")























