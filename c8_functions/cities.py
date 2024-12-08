def describe_city(city, country="the united states"):
    """Describe a city."""
    print(f"\n{city.title()} is in {country.title()}.")


describe_city("tehran", "iran")
describe_city(city="new york")
describe_city("moscow", "russia")
