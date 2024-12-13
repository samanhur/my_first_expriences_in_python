"""A collection of classes for medeling users."""

from user import User


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
            for privilege in self.privileges:
                print(f"\t- {privilege.title()}")
        else:
            print("\n\t- This user has no privileges.")
