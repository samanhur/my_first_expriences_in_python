# region stop loop with break

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "


while True:
    topping = input(prompt)

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")

# endregion

# region stop loop with conditional test
prompt = "\nDo you want add topping on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while input(prompt) != "quit":
    topping = input("\nWhat topping would you like on your pizza?")

    print(f"I'll add {topping} to your pizza.")
    
# endregion

# region stop loop with variable
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

active = True
while active:
    topping = input(prompt)

    if topping == "quit":
        active = False

    print(f"I'll add {topping} to your pizza.")
    
# endregion
