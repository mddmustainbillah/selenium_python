########### Relational comparison #############

#### assertGreater
# assertGreater verifies whether first values greater than second value or not.
#
#### assertGreaterEqual
# assertGreaterEqual verifies whether first parameter is greater or equal to the second parameter
#
#### assertLess
# assertLess verifies whether first parameter is lesser than second parameter or not
#
#### assertLessEqual
# assertLessEqual verifies whether first parameter is lesser of equal to the second parameter.


import unittest


class Test(unittest.TestCase):
    def testName(self):
        # self.assertLess(10, 100)
        # self.assertLessEqual(10, 100)
        # self.assertLessEqual(100, 100)
        #
        # self.assertGreater(100, 10)
        # self.assertGreaterEqual(100, 10)
        self.assertGreaterEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
