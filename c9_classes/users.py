class User:
    """A simple program that shows users information and greet them."""

    def __init__(self, firs_name, last_name):
        """User informations:"""
        self.first = firs_name
        self.last = last_name

    def describe_user(self):
        """printing a berif about users."""
        print(f"\nUser's first name:\n\t {self.first.title()}")
        print(f"User's Last name:\n\t {self.last.title()}")

    def greet_user(self):
        """A greeting message that showing to the user after logging in."""
        print(
            f"\nWelcome to your account " f"{self.first.title()} {self.last.title()}."
        )
        print("I hope you enjoy from using our services.")


user1 = User("saman", "ghasemi")
user1.describe_user()
user1.greet_user()

user2 = User("mehdi", "ghasemi")
user2.describe_user()
user2.greet_user()
