#message= 'pizza, is so delicious! I like that very much.'
pizzas = ['special', 'peperoni', 'vegetables']

#for pizza in pizzas :
#    print(f"{pizza.title()} {message}")
#print('\nI ate every of them in this week.')

friend_pizzas = pizzas[:]

pizzas.append('meat')
friend_pizzas.append('sezar')

print("My favorite pizzas are:")
for piza in pizzas:
    print(f"- {piza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas :
    print(f"- {pizza}")
