"""A collection of classes for medeling users."""


class User:
    """A simple program that shows users information and greet them."""

    def __init__(self, firs_name, last_name, user_name, age=""):
        """User informations:"""
        self.first = firs_name
        self.last = last_name
        self.username = user_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """printing a berif about users."""
        print(f"\nUser's first name:\n\t {self.first.title()}")
        print(f"User's Last name:\n\t {self.last.title()}")
        print(f"User name:\n\t {self.username.lower()}")
        if self.age != "":
            print(f"User's age:\n\t {self.age}")

    def greet_user(self):
        """A greeting message that showing to the user after logging in."""
        print(
            f"\nWelcome to your account " f"{self.first.title()} {self.last.title()}."
        )
        print("I hope you enjoy from using our services.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
