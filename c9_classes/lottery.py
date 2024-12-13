from random import choice

win_codes = []
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "x", "y", "z", "s"]

print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a
#   while loop.
while len(win_codes) < 4:
    pulled_item = choice(possibilities)
    
    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in win_codes:
        print(f" We pulled a {pulled_item}")
        win_codes.append(pulled_item)
        
print(f"\nThe final winning ticket is: {win_codes}")