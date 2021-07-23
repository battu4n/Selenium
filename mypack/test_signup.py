import pytest
@pytest.yield_fixture()
def setup():
    print("OPen url to open page")
    yield
    print("closing browser after login")

def test_signupbyemail():
    print("This is signup by emain")
def test_signupbyfacebook():
    print("This is signup by facebook")