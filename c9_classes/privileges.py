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


class Admin(User):
    """Special access for admin."""

    def __init__(self, firs_name, last_name, user_name, age=""):
        """Initialaize the admin."""
        super().__init__(firs_name, last_name, user_name, age)

        # Initialize an empty sef of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Showing all privileges that admins have."""

        if self.privileges:
            print("This user as an admin has This privileges:")
            for privilege in self.privileges:
                print(f"\t- {privilege.title()}")
        else:
            print("\n\t- This user has no privileges.")


admin = Admin("saman", "ghasemi", "samanhur", 20)
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")

admin.privileges.privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
admin.privileges.show_privileges()
