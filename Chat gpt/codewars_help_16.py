# Identify the Data Type

var1 = "Hello, World!"  
var2 = 42  
var3 = 3.14  
var4 = True  
var5 = [1, 2, 3, 4, 5]  
var6 = {"name": "Alice", "age": 30}  

print(type(var1))  
print(type(var2))  
print(type(var3))  
print(type(var4))  
print(type(var5))  
print(type(var6))  

# str (string) → "Hello" (text enclosed in quotes)
# int (integer) → 42 (whole numbers)
# float (floating point) → 3.14 (numbers with decimals)
# bool (boolean) → True or False (logical values)
# list → [1, 2, 3] (ordered collection, mutable)
# dict (dictionary) → {"key": "value"} (key-value pairs)# 1. Intersection: Both workshops

fruits = {"apples", "bananas", "pear", "pear", "peach"} # A set is a list which doesn't allow duplicates

fruits.add("pie") #adds one only to set
fruits.update(["orange", "grapes", "pear"]) #adds more than one to set ([]) means it's adding a list or could be another set eg ({})
fruits.update({"bread", "butter"}) #adding more that one to set, here it's adding a list to a set ({})
for these_items in ["peach", "apples"]:
	fruits.discard(these_items) # .discard() won't cause an error if the item isn't found
fruits.remove("bananas")# can remove only one item from set

print(fruits)


set1 = {"blue", "pink", "red"}
set2 = {"green", "yellow", "blue"}

result = set1 | set2 # Union (|) - Combines two sets (removes duplicates)
print(result)


colours_1 = {"blue", "pink", "red"}
colours_2 = {"green", "yellow", "blue"}
result = colours_1 & colours_2 #Intersection (&) - Finds common elements
print(result)

shades_1 = {"blue", "pink", "red"}
shades_2 = {"green", "yellow", "blue"}
result = shades_1 - shades_2 #Difference (-) - Finds items in one set but not the other
print(result)

shades_1 = {"blue", "pink", "red"}
shades_2 = {"green", "yellow", "blue"}
result = shades_2 ^ shades_1 #Symmetric Difference (^) - Finds items in either set, but not both
print(result)



def function_name(challenge_set_1 , challenge_set_2):
	return challenge_set_1 ^ challenge_set_2

challenge_set_1 = {"dog", "cat", "mouse"}
challenge_set_2 = {"cat", "elephant", "mouse"}

result=function_name(challenge_set_1, challenge_set_2)
print(result)


def subset_task(small_set, big_set):
	return big_set.issubset(small_set)

small_set = {"cat", "mouse"}
big_set = {"dog", "cat", "mouse", "elephant" }

result = subset_task(small_set, big_set)
print(result)

def subset_task(small_set, big_set):
	return big_set.issuperset(small_set) #Superset does the opposite of subset

small_set = {"cat", "mouse"}
big_set = {"dog", "cat", "mouse", "elephant" }

result = subset_task(small_set, big_set)
print(result)


def function_name2(small_set2 , big_set2):
	if small_set2.issubset(big_set2):
		return small_set2 ^ big_set2
	else:
		return "small_set2 is not a subset of big_set2"

small_set2 = {"cat", "mouse"}
big_set2 = {"dog", "cat", "mouse", "elephant"}

result = function_name2(small_set2, big_set2)
print(result)



