#Sort permenantly, can't be reverted to original list
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.sort()
print(cars)

#Sort in reverse alphabetical, permenantly, can't be reverted to original list
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse = True)
print(cars)

# Maintain original order, temporarily sort(ED)
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print("\nHere's the sortED list:")
print(sorted(cars))
print("\nHere's the original list:")
print(cars)

#Reversing the list order
cars = ["bmw", "audi", "toyota", "subaru"]
print("\nReversing the order:")
print(cars)
cars.reverse()
print(cars)

#Find the length of something
cars = ["bmw", "audi", "toyota", "subaru"]
len(cars)

result = len(cars)
print(len(cars))

# or
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

# 3-8 Write list of places in the world

places_i_want_to_visit = ["london", "catford", "maldeves", "italy"]
print(f"Original list: {places_i_want_to_visit}")
print(f"SortED list{sorted(places_i_want_to_visit)}")
print(f"Original list: {places_i_want_to_visit}")

places_i_want_to_visit.reverse()
print(f"Reversed list: {places_i_want_to_visit}")

places_i_want_to_visit.reverse()
print(f"Reversed again (back to original): {places_i_want_to_visit}")

places_i_want_to_visit.sort()
print(f"List with 'sort' (permenant sort): {places_i_want_to_visit}")

places_i_want_to_visit.sort(reverse = True)
print(f"List with sort, which has been reversed: {places_i_want_to_visit}")



# 3-9 Use guest list to send a message detailing how many guests:
#3-6 Bigger table so more guests!
guests = ['rich', 'frank', 'phil']
print(f"{guests} We've found a bigger table!!!!")
guests.insert(0, "juan")
guests.insert(2, "william")
guests.append("birtchearth")
print(f"{guests[0].title()}, our party is happening!")
print(f"{guests[1].title()}, come to our part!!!")
print(f"{guests[2].title()} PARTYYYY!")
print(f"{guests[3].title()}, it's time!")
print(f"{guests[4].title()}, Hi")
print(f"{guests[5]}, come if you can")
print(f"Hi fam, we have {len(guests)} guests invited so far!! :D")











