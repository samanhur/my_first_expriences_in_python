from pathlib import Path

def read_from_text_file(file_path):
    try:
        path = Path(file_path)
    except FileNotFoundError:
        print(f"\nFile not found in {file_path}!\n")
    else:
        content = path.read_text()
    return content


content = read_from_text_file("macbeth.txt")

# find 'the' in macbeth.txt regardless of it's format(it will also count 
#   'then', 'there',...).
word_count = content.lower().count('the')
print("\nCount 'the' in the text:", word_count)

# find ' the ' in macbeth.txt regardless of it's format(it'll doesn't count 
#   'then', 'there',...).
word_count = content.lower().count(' the ')
print("\nCount ' the ' in the text:", word_count)
