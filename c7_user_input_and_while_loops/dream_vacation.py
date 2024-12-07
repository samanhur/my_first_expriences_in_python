message1 = ("\nWhat's your name? ")
message2 = "\nIf you could visit one place in the world, where would you go?"
message2 += "\n(if you want end it enter 'quit'): "
message3 = "\nDo you want to continue this program for other people(yes/no)? "

responses = dict()

active = True
while active :
    name = input(message1)
    location = input(message2)
    
    responses[name] = location
    
    repeat = input(message3)

    if repeat == 'no' :
        active = False

print("The result of this poll is:")
for name,location in sorted(responses.items()) :
    message = f"{name}'s favorite place for vacation is {location}."
    print(message)