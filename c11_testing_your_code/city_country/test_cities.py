from city_functions import city_country_name

def test_city_country():
    """Testing the formatted name of the city and the country we want."""
    name = city_country_name('tehran', 'iran')
    assert name == 'Tehran, Iran'
