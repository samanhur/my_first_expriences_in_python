from employee import Employee


def test_get_default_raise():
    """Testing by the default value for raising."""

    person = Employee("saman", "ghasemi", 60_000)
    person.give_raise()
    assert person.salary == 65000


def test_get_custom_raise():
    """Testing by custom value for raising."""

    person = Employee("saman", "ghasemi", 70_000)
    person.give_raise(10_000)
    assert person.salary == 80_000
