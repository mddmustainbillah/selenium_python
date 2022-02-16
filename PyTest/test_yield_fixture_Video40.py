##### Work with PyTest Fixtures   ###########

# The purpose of test fixtures is to provide a dixed baseline upon which tests can
# reliably and repeatedly execute.

###   @pytest.fixture()
#       --- Executes specific method before every test method.

###   @pytest.yield_fixture()
#       --- Execute specific method before & After every test method.



import pytest


@pytest.yield_fixture()
def setup():
    print("Once before every method.")
    yield
    print("Once after every method.")


def testMethod1(setup):   # yield_fixture applied here
    print("This is test method - 1")


def testMethod2():    # yield_fixture not applied here
    print("This is test method - 2")
