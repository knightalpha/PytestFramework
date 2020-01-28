import pytest


@pytest.yield_fixture()
def setUp():
    print('Opening URL to Signup')
    yield
    print('Closing browser after Signup')


def test_Signupbyemail(setUp):
    print('This is Signup by email')


def test_Signupbyfacebook(setUp):
    print('This is Signup by facebook')
