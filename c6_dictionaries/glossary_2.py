glossary = {
    'print': "We use print as 'print()' for showing anything in python.", 
    'title': "To become each word to title we use 'title()'.", 
    'list': "We use lists for storing some information, usually they're related.", 
    'append': "We use append as 'append()' for appending what we want to lists.", 
    'if': "Ifs use for conditional situation like when we have two different "
    "choices.",
    'for': "Usually we use 'for' for looping most things in python.",
    'upper': "To become each word to upper case we use 'upper()'.",
    'lower': "To become each word to lower case we use 'lower()'.", 
    'dictionaries': "We can use dictionaries for storing even bilions datas.", 
    'set': "If we have some values and we don't want to see repeating, we can "
    "use 'set()'s."
    }

for term,meaning in glossary.items(): 
    print(f"{term.title()}:")
    print(f"\t{meaning}\n")