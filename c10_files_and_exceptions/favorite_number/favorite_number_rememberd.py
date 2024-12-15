from pathlib import Path
import json

# First way to do this
# path = Path('favorite_number.json')
# if path.exists():
#     content = path.read_text()
#     number = json.loads(content)
#     print(f"I know your favorite number! It's {number}")
# else:
#     number = input("What's your favorite number? ")
#     content = json.dumps(number)
#     path.write_text(content)
#     print("Thanks, I'll remember that.")
    
    
# Second way to do this
path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
