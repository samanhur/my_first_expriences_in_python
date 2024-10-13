glossary = {
    'print': "We use print as 'print()' for showing anything in python.", 
    'title': "To become each word to title we use 'title()'.", 
    'list': "We use lists for storing some information, usually they're related.", 
    'append': "We use append as 'append()' for appending what we want to lists.", 
    'if': "Ifs use for conditional situation like when we have two different "
    "choices."
    }

glossary_keys = [key for key in glossary.keys()]

print(glossary_keys[0])
print(f"\t{glossary['print']}\n")

print(glossary_keys[1])
print(f"\t{glossary['title']}\n")

print(glossary_keys[2])
print(f'\t{glossary["list"]}\n')

print(glossary_keys[3])
print(f"\t{glossary['append']}\n")

print(glossary_keys[4])
print(f"\t{glossary['if']}\n")

