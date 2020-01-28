"""
The purpose of test fixture is to provie a fixed baseline upon which tests can reliably
and repeatedly execute.

1. @pytest.fixture()
    --> executes specific method before every test method

2. @pytest.yield_fixture()
    --> execute specific method before and after every test method
"""
import pytest

@pytest.fixture()   # this method is considered as fixture
def setup():
    print('Once before every method')

def test_method1(setup):
    print('This is test method 1')

def test_method2(setup):
    print("This is test method 2")