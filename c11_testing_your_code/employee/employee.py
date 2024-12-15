class Employee:
    """Showing the salary of any of employee we want."""

    def __init__(self, f_name, l_name, salary):
        """Storing information about employees."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
