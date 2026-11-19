cities = ["Multan", "Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
print(cities)

# indexing
print(cities[3])

# slicing
print(cities[2:4])

# replacing
cities[1:3] = ["Faisalabad", "Sialkot"]
print(cities)

# deleting
cities[4:5] = []
print(cities)

# append
cities.append("Rawalpindi")
print(cities)

# insert
cities.insert(3 , "Bahawalpur")
print(cities)

# pop
cities.pop(2)
print(cities)

# remove by name, remove one value at a time
cities.remove("Bahawalpur")
print(cities)

# string is inserted so it treats each value as an item
cities[2:3] = "Sakkur"
print(cities)

# if-else condition
if "Karachi" in cities:
    print("Karachi Kings!")
else:
    print("Karachi is not in the list.")

# for loop
