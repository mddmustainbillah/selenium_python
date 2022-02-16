######## assertIn & assertNotIn ##########

#### assertIn
# assertIn method verifies whether the first element is present in the second element, if
# first element is present in second element then test is passed otherwise test is failed.
#
##### assertNotIn
# assertNotIn method verifies whether the first element is not present in the second element
# or not, if first element is present then test will be failed otherwise test is passed.
#
# This two methods will be helpful when you want to verify presence of a value
# in a list, tuple, set and dictionary.

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list = ["python", "selenium", "java"]

        # self.assertIn("python", list)  # passed
        # self.assertIn("ruby", list)  # failed

        # self.assertNotIn("python", list)  # failed
        self.assertNotIn("ruby", list)   # passed

if __name__ == "__main__":
    unittest.main()












