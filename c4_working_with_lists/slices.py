# animals
animals = [
    "cat",
    "lion",
    "tiger",
    "cheetah",
    "leopard",
    "snow leopard",
    "wild cat",
    "caracal",
    "jaguar",
]

# for animal in animals :
#    print(f"{animal.title()}s are so beautiful!\n")
# message= 'probably you have noticed that they look like the same. all of them are Feliformia'
# print(message)

print(animals[:3])
print(animals[3:6])
print(animals[6:])

message1 = "\nThe first three items in the list are:"
message2 = "Three items from the middle of the list are:"
message3 = "The last three items in the list are:"

first = animals[:3]
print(message1, first)
middle = animals[3:6]
print(message2, middle)
last = animals[6:]
print(message3, last)
