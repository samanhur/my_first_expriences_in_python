message = "pizza, is so delicious! I like that very much."

favorite_pizzas = ["special", "peperoni", "vegetables"]

for pizza in favorite_pizzas:
    print(pizza)
print("\n")


for pizza in favorite_pizzas:
    print(f"{pizza.title()} {message}")

print("\nI ate every of them in this week.")
