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
        """Display restaurant's open time."""
        print(f"{self.name.title()} is open at 8 a.m. to 11 p.m.")


sinor = Restaurant("sinor", "fried food")
print(f"My favorite restaurnt is {sinor.name.title()}.")
print(f"I like soo much {sinor.type}")

sinor.describe_restaurant()
sinor.open_restaurant()
