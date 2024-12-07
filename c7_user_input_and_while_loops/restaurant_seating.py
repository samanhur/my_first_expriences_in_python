print('Welcome to Bita restaurant. We\'re happy for hosting you!')
seating = input("How many people are in your party? ")
num_seat = int(seating)
if num_seat > 8 :
    print("Sorry, You'll have to wait for a table.")
else:
    print("Your table is ready!")