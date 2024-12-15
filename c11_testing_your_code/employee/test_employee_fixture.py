import pytest
from employee import Employee


@pytest.fixture
def test_raising():
    person = Employee("saman", "ghasemi", 60000)

    return person


def test_get_default_raise(test_raising):
    """Testing by the default value for raising."""
    test_raising.give_raise()
    assert test_raising.salary == 65000


def test_get_custom_raise(test_raising):
    """Testing by custom value for raising."""
    test_raising.give_raise(10000)
    assert test_raising.salary == 7_0000
