##### Work with PyTest Fixtures   ###########

# The purpose of test fixtures is to provide a dixed baseline upon which tests can
# reliably and repeatedly execute.

###   @pytest.fixture()
#       --- Executes specific method before every test method.

###   @pytest.yield_fixture()
#       --- Execute specific method before & After every test method.

import pytest

@pytest.fixture()
def setup():
    print("Once before every method.")

def testmethod1(setup): # setup passed  # here have to pass the method name
    print("This is the test method.")

def testmethod2():  # setup not passed. so fixture not applicable here.
    print("This is test method2.")
