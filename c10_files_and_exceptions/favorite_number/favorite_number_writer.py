from pathlib import Path
import json

path = Path("favorite_number.json")
number = input("What's your favorite number? ")
content = json.dumps(number)
path.write_text(content)

print("Thanks! I'll remember that number.")
