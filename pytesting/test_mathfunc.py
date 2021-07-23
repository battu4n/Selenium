import pytest

@pytest.yield_fixture()
def setup():
    print("Once before everymethod")
    yield
    print("Once after every method")
def testMethod1():
    print("This is test method1")
def testMethod2():
    print("This is test Method2")