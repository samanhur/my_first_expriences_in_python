from pathlib import Path

filenames = ['cat.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    print(f"\nReading file: \"{filename}\"\n")


    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
        #print(f"We failed for finding '{filename}'.\n")
    else:
        print(f"{content}\n")