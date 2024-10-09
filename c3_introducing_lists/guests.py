# 3-4: Guest list
guests = ["shakespeare", "newton", "Socrates"]

print(
    f"Hello dear {guests[0].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[1].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[2].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)


# 3-5: Changing guest list
print(f"{guests[1].title()} can't be here for saturday.")

del guests[1]
guests.insert(1, "Jobs")
# or:
# guests[1]= 'Jobs'

print(
    f"Hello dear {guests[0].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[1].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[2].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)


# 3-6: More guests
print("\nWe got a bigger table!")
print("and new guests are: Freud, Hafez, Hawking")
guests.insert(0, "Freud")
guests.insert(-2, "Hafez")
guests.append("Hawking")

print(
    f"Hello dear {guests[0].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[1].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[2].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[3].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[4].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(
    f"Hello dear {guests[5].title()}. I will be happy if you can come to my house for dinner saturday night. I'm waiting for you!"
)
print(len(guests))


# 3-7: Shrinking guest list
print("\nSorry, we can only invite two people to dinner.")

noguest1 = guests.pop()
noguest2 = guests.pop(0)
noguest3 = guests.pop(3)
noguest4 = guests.pop(0)

print(
    f"I'm so sorry dear {noguest1}, I can't host you. I hope to see you another time."
)
print(
    f"I'm so sorry dear {noguest2}, I can't host you. I hope to see you another time."
)
print(
    f"I'm so sorry dear {noguest3}, I can't host you. I hope to see you another time."
)
print(
    f"I'm so sorry dear {noguest4}, I can't host you. I hope to see you another time."
)
print()

print(f"Dear {guests[0]}. Still I want to see you on saturday night!")
print(f"Dear {guests[1]}. Still I want to see you on saturday night!")

del guests[0]
del guests[0]

print(guests)