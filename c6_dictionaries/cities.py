cities = {
    'tehran' :{
        'country': 'iran',
        'population': '8.6 million',
        'fact': 'Tehran is the capital of Iran',
        },
    'new york' :{
        'country': 'the united states',
        'population': '8.4 million',
        'fact': 'New york is famous for city has no night.',
        },
    'tokyo' :{
        'country': 'japan',
        'population': '13.9 million',
        'fact': "It's area is 2,194 square kilometers. ",
        }    
    }
for name, info in cities.items() :
    print(f"{name.upper()}:")
    print(f"\tcountry: {info['country'].title()}")
    print(f"\tpopulation: {info['population'].title()}")
    print(f"\tinteresting fact: {info['fact']}\n")