from pathlib import Path

path = Path("guest_book.txt")

prompt = "\nHi, what's your full name?"
prompt += "\n(Enter 'quit' if you're the last guest): "

guest_names = []
while True :
    name = input(prompt)
    if name == 'quit' :
        break

    print(f"Thanks {name.title()}, we'll add you to the guest book.")
    guest_names.append(name.title())

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"
    
path.write_text(file_string)