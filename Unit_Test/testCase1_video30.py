############ Python UnitTest Framework ###########

# In automation testing, oranization your code is very important and client expects us to
# write automation scripts according to the manual test cases.
#
# We can get good reporting structure if we can exactly map our automation code with
# manual test cases.
#
# In python we can use UnitTest testing framework to organize our automation code and
# to extract reports
#
# To use the methods present in the UnitTest framework, we have to extend the TestCase
# class present in the Unittest module

import unittest


class Test(unittest.TestCase):
    def test_FirstTest(self):
        print("This is my first unit test case.")


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
