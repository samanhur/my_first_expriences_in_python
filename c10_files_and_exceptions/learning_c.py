from pathlib import Path

# this is a practice for 'replace()'. the text that printed is not right!

path = Path("learning_python.txt")
text = path.read_text()

for line in text.splitlines():
    line = line.replace("Python", "C")
    print(line)
