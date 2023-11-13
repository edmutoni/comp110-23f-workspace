"""Dictionary Lesson"""
#dictionaries (map, hashmap, key-value store) are organized similarly like lists. indexes -> key, values -> values

#name: dict[<key type>, <value type>]
#temps: dict[str, float]

#construct an empty dict: dict() or dict{}
#temps: dict[str, float] = {"Florida": 72, "Raleigh": 56}

ice_cream: dict [str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary")
print(ice_cream)

#adding elements to a dictionary
#<dict name>[key] = <value>
print("Adding new key to dictionary")
ice_cream["mint"] = 3
print(ice_cream)

#removing elements, we use pop()
#<dict name>.pop(key)
print("Removing a key from dictionary")
ice_cream.pop("mint")
print(ice_cream)

#to access a value, use subscription notation
#<dict name>[<key>]

#to modify -> <dict name>[<key>] = new value
print("Printing a key, and modifying dictionary")
print(f"There are {ice_cream['chocolate']} orders of cholcate")

print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(ice_cream)

#length of dictionary -> len(<dict type), tells how many key-value pairs a dict has
print(len(ice_cream))

#check if key in dictionary -> <key> in <dict name>
print("mint" in ice_cream)
print("chocolate" in ice_cream)

if "mint" in ice_cream == True:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

#!! can't have mutliple of the same key

#to print all keys in dictionary
for key in ice_cream:
    print(key)

#to print all valukes in dictionary
for key in ice_cream:
    print(ice_cream[key])

#loop through and print out every flavor and its number of orders
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")