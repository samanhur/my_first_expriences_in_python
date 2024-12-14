from pathlib import Path

path = Path("learning_python.txt")

# printing entire file
text = path.read_text()
print(text)

print("...")

# printing file, line by line
lines_text = []
for line in text.splitlines():
    lines_text.append(line)
    
for line_text in lines_text:
    print(f"\n{line_text}")