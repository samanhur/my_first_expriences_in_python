favorite_palaces = {
    'saman0': ['Hormoz island', 'darak beach, chabahar', 'california'], 
    'saman1': ['shiraz', 'isfahan', 'tabtiz'],
    'saman2': ['ramsar'],
    }

for name, places in favorite_palaces.items():
    if len(places) > 1 :
        print(f"\n{name.title()}'s favorite palaces are:")

        for place in places : 
            print(f"\t{place.title()}")

    elif len(places) == 1 :
        print(f"\n{name.title()}'s favorite palaces is:")

        for place in places : 
            print(f"\t{place.title()}")
       