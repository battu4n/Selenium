import pytest
@pytest.yield_fixture()
def setup():
    print("OPen url to open page")
    yield
    print("closing browser after login")
def test_loginbyemail():
    print("This is login by emain")
def test_lgoinbyfacebook():
    print("This is login by facebook")