class Restaurant:
    """Describing a restaurant that you want."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.name.title()} is a {self.type} restaurant.")

    def open_restaurant(self):
        """Display restaurant is open."""
        print(f"{self.name.title()} is open. Come on in!")


zhivan = Restaurant("Zhivan", "Fast food")
zhivan.describe_restaurant()

delvin = Restaurant("Delvin", "Cafe and restaurant")
delvin.describe_restaurant()

mahshid = Restaurant("Mahshid", "Iranian food")
mahshid.describe_restaurant()