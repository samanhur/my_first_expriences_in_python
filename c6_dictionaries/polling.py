people = ['mina', 'rostam', 'jack', 'sarah', 'jen', 'saman', 'mobina', 'edward',
           'phill', 'sajede', 'saba', 'amir', 'hosein', 'nima', 'soheyl', 
           'noshin', 'farhad', 'nazanin', 'rima', 'yasna', 'yalda', 'poria', 
           'babak', 'samyar', 'ardalan', 'erin']

fav_lan = {
    'mina': 'java',
    'jen': 'python',
    'sarah': 'C', 
    'saman': 'python',
    'edward': 'rust', 
    'phil': 'python',
    'sajede': 'java script',
    'amir': 'matlab', 
    'soheyl': 'swift', 
    'noshin': 'C++', 
    'farhad': 'binary',
    'rima': 'R', 
    'yasna': 'java script',
    }

for person in people :
    if person in fav_lan.keys() :
        print(f"Thank you {person.upper()} for take our poll! We appriciate that")
    else:
        print(f"We'll be thanksfull if you taking the poll. Please do that.")