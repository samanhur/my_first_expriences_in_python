#favorite_languages.py    p.109
favorite_foods = {
'iman': ['pizza', 'french fries', 'dolmeh'],
'melika': ['ghorme sabzi'],
'simin': ['kebab', 'pasta'],
'nastaran': ['doner kebab', 'hamburger', 'hotdog', 'omelet'],
'mehdi': [],
    }
for name, foods in favorite_foods.items():
    if len(foods) == 1 :
        print(f"\n{name.title()}'s favorite food is:")
        print(f"\t{food.title()}")

    elif len(foods) > 1 :
        print(f"\n{name.title()}'s favorite foods are:")
        for food in foods :
            print(f"\t{food.title()}")

    else:
        print(f"\n{name.title()} don't like any food!")