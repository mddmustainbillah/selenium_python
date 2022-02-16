# ######### Python UnitTest Framework ###############
#### Skiping test
# 1. Skip test
# 2. Skip test with reason
# 3. Skip test based on condition

import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest # decorator
    def test_search(self):
        print("This is search test.")

    @unittest.skip("I am skipping this test method because it is not ready")
    def test_advancesearch(self):
        print("This is advance search test.")

    @unittest.skipIf(1==1, 'Numbers are not equals')
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test.")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test.")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ == "__main__":
    unittest.main()
