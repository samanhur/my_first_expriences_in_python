from pathlib import Path

path = Path("guest.txt")

name = input("Please enter your full name: ")
path.write_text(name.title())
