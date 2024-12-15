"""A collection of functions for working with cities."""


def city_country(city, country, population=0):
    """
    Return a string that describe city's name,
    country's name and it's population(optional).
    """
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population: {population}"
    return output_string
