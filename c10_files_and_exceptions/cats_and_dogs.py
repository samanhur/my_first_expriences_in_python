from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    print(f"\nReading file: \"{filename}\"\n")
    
    try:
        path = Path(filename)
        content = path.read_text()
    except FileNotFoundError:
        print(f"We failed for finding '{filename}'.\n")
    else:
        print(f"{content}\n")
