cities = [
    "tehran",
    "isfahan",
    "shiraz",
    "mashhad",
    "tabriz",
    "yazd",
    "ardabil",
    "boshehr",
    "anzali",
    "arak",
    "khomein",
    "sari",
    "yasoj",
    "birjand",
    "qazvin",
    "ahvaz",
    "chabahar",
]
print(cities)
print(f"\n{cities[-1].upper()}\t   ".rstrip())

# favorite= cities[0]
# print(favorite)

message = f"I like to visit {cities[-1].title()}"
print(message.lower())
print(cities[6].upper())

cities[6] = "yasoj"
print(cities[6].upper())
cities.append("ardabil")
cities.append("ramsar")
cities.append("shazand")
cities.insert(2, "gilan")
cities.insert(-3, "semnan")
print(cities)

# next two lines: order matter
del cities[1]
del cities[7]
print(cities)
favorite = cities.pop(0)
print(favorite.upper())
popped_city = cities.pop()
print(popped_city)
cities.remove("tabriz")
myoriginally = "khomein"
cities.remove(myoriginally)
print(f"\tI'm originally form {myoriginally.title()}!")
print(cities)
cities.remove("yasoj")

# cities.sort(reverse=True)
print(sorted(cities))
print(sorted(cities, reverse=True))
cities.reverse()
print(f"\n\t{cities}")
cities.sort()
print(cities)
print(len(cities))
