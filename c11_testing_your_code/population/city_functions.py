"""A collection of functions for working with cities."""


def city_country(city, country, population):
    """
    Return a string that describe city's name,
    country's name and it's population.
    """
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" - population: {population}"
    return output_string
