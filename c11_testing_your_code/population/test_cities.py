import city_functions
import city_functions_pop_optional

def test_city_country():
    city = city_functions.city_country("Tehran", "Iran", 15_000_000)
    assert city == "Tehran, Iran - population: 15000000"
    
def test_city_country_default_pop():
    city = city_functions_pop_optional.city_country("Tehran", "Iran")
    assert city == "Tehran, Iran"

def test_city_country_with_pop():
    city = city_functions_pop_optional.city_country("Tehran", "Iran", 15_000_000)
    assert city == "Tehran, Iran - population: 15000000"