import pytest


@pytest.yield_fixture()
def setUp():
    print('\nOpening URL to Login')
    yield
    print('\nClosing browser after Login')


def test_Loginbyemail(setUp):
    print('\nThis is Login by email')


def test_Loginbyfacebook(setUp):
    print('\nThis is Login by facebook')

"""
Run Tests
pytest -v -s test_Login.py::test_Loginbyfacebook


"""