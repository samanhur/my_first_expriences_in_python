sandwich_orders = [
    "chicken sandwich",
    "egg sandwich",
    "seafood sandwich",
    "roast beef sandwich",
    "greilled cheese",
    "ham sandwich",
    "nutella sandwich",
    "grilled chicken sandwich",
    "meatball " "sandwich",
    "ice cream sandwich",
    "prawn sandwich",
]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I', working on your {current_sandwich.title()}.")

    finished_sandwiches.append(current_sandwich)
    print(f"Mading {current_sandwich} finished!\n")

print("\n Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
