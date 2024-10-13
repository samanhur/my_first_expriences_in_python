saman_info = {
    'first': 'saman',
    'last': 'ghasemi',
    'age': 19, 
    'city': 'tehran',
    }
albert_info = {
    'first': 'albert',
    'last': 'einstein', 
    'age': 77, 
    'city': 'ulm'
    }
marie_info = {
    'first': 'marie',
    'last': 'curie', 
    'age': 68, 
    'city': 'warsaw'
    }

people = [saman_info, albert_info, marie_info]

for person in people :
    print(f"{person['last'].title()} :")
    full_name = f"{person['first']} {person['last']}"
    print(f"\tfull name : {full_name.title()}")
    print(f"\tlast age: {person['age']}")
    print(f"\tcity(born): {person['city'].title()}\n")