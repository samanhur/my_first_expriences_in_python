class Restaurant:
    """Describing a restaurant that you want."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.name = restaurant_name.lower()
        self.type = cuisine_type.lower()
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.name.title()} is a {self.type.title()} restaurant.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.name.title()} is open now.")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, number_increased):
        """Allow users to increment the number of served."""
        self.number_served += number_increased


restaurant = Restaurant("shamim", "pizza")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 230
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(480)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"\nNumber served: {restaurant.number_served}")
