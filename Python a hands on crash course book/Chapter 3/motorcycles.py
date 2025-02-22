motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#Change value of list item
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[2] = "fish"
print(motorcycles)

#Add to end of list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("sausage")
print(motorcycles)

#Start with empty list and add values into it
motorcycles = []
motorcycles.append("wheels")
motorcycles.append("tyres")
motorcycles.append("lights")
motorcycles.append("feet")
print(motorcycles)

#Insert new values to list
motorcycles = ["fast", "funny", "fluffy", "furry"]
motorcycles.insert(1,"choppy")
print(motorcycles)

#Permemnantly remove value from list
motorcycles = ["fast", "funny", "fluffy", "silly"]
del motorcycles[0]
del motorcycles[-1]
print(motorcycles)

#Remove last item from list and use item again
motorcycles = ["honada", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#Print a statement about the last motorcycle we bought:
motorcycles = ["honda", "yamaha", "sazuki"]
last_owned_motorcycle = motorcycles.pop()
print(f"{last_owned_motorcycle.title()} was the last owned motorcycle")

#Pop (remove) any item from the list
motorcycles = ["honda", "yamaha", "sazuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop(2)
print(popped_motorcycles)

#Remove an item by value (and not position like in .pop())
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

#Remove ducati and print a reason for removing it
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is being removed because it's out of budget")

# 3-4 Print a massage to each guest in the list
guests = ['rich', 'frank', 'phil']
print(f"{guests[1].title()}, I can't wait for you to come!")
print(f"Hi {guests[0].title()} it's amazing you're going to come!")
print(f"We're really loooking forward to you coming {guests[2]}, can't wait!")

# 3-5 Update the guestlist
guests = ['rich', 'frank', 'phil']
print(f"Oh no, {guests[2]}, can't make it :(")
guests.remove("frank")
guests.append("viv")
print(guests)
print(f"{guests[0].title()} You still coming?!")
print(f"{guests[1].title()} you coming as well?")
print(f"{guests[2].title()}, please say you're coming!")

#3-6 Bigger table so more guests!
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

# 3-7 Shirnk the list
popped_guests = guests.pop(5)
print(f"{popped_guests}, sorry, you're out")
popped_guests = guests.pop(4)
print(f"{popped_guests}, sorry, you're out")
popped_guests = guests.pop(3)
print(f"{popped_guests}, sorry, you're out")
popped_guests = guests.pop(2)
print(f"{popped_guests}, sorry, you're out")
print(f"{guests[0]}, you're finally finally coming!")
print(f"{guests[1]}, yaaaaay")
del guests[1]
del guests[0]
print(guests)








