def city_country(city, country):
    "cities' names and their countries"
    
    return f'\n"{city.title()}, {country.title()}"'


indian = city_country("dehli", "india")
iranian = city_country("shiraz", "iran")
german = city_country("berlin", "germany")
print(indian)
print(iranian)
print(german)
