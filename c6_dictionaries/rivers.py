rivers = {
    'Nile': 'Egypt', 
    'Karon': 'Iran', 
    'Mississippi': 'The united states',
    }

for name,location in rivers.items() :
    print(f"{name.title()}: {name.title()} is a great river and it's in {location.title()}\n")

for name in rivers : #it could be rivers.keys()
    print(name)
print()

for location in rivers.values() :
    print(location)
