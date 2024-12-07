sandwich_orders = [
    "turkey",
    "chicken",
    "pastarami",
    "meat",
    "beef",
    "veggie",
    "pastarami",
    "pastarami",
    "soshi",
]
finished_sandwiches = []

print("\nSorry, we are all out of pastarami today.\n")

# removing pastarami from sandwich orders
while "pastarami" in sandwich_orders:
    sandwich_orders.remove("pastarami")


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print()


for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich")