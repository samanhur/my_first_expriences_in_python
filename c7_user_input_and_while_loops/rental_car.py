car = input("What kind of car you like? ")
print(f"Let me see if I can find you a {car.title()}.")

our_cars = ['bmw', 'benz', 'subaru', 'toyota', 'ford']

if car.lower() in our_cars :
    print(f"We have {car.title()}. We'll be happy if you want rent it!")
elif car not in our_cars :
    print(f"Sorry, we don't have {car.title()} right now. Do you want another?")