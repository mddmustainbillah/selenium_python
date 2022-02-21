########## Multiple ways to Run Test Case #########
# pytest test_mod.py   # run tests in module
# pytest some-path     # run all tests below some-path
# py.test test_module.py::test_method  # only run test_method in test_module
#
# -s to print statement
# -v verbose


import pytest


@pytest.yield_fixture()
def setUp():
    print("Opening URL in login.")
    yield
    print("Closing browser after login.")


def test_loginbyEmail(setup):
    print("This is Login by email test.")


def test_loginbyfacebook(setup):
    print("This login by facebook test.")
