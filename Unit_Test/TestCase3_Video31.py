# ######### Python UnitTest Framework ###############
#     1. setUp
#     2. tearDown
#     3. setUpClass
#     4. tearDownClass
#     5. setUpModule
#     6. tearDownModule



import unittest


def setUpModule(): # Executed before executing any class or any method present in the test class
    print("setUpModule")


def teardownModule():  # Executed after completing everything present in the python module
    print('tearDownModule')


class AppTesting(unittest.TestCase):

    @classmethod  # Decorator
    def setUp(self):  # Execute before all test methods
        print("This is login test")

    @classmethod
    def tearDown(self) -> None:  # Execute after all test methods
        print("This is logout test.")

    @classmethod
    def setUpClass(cls) -> None:  # Execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls) -> None:  # Execute once after the class ended
        print("Close Application")

    def test_search(self):
        print("This is search test.")

    def test_advancesearch(self):
        print("This is advance search test.")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test.")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test.")


if __name__ == "__main__":
    unittest.main()
