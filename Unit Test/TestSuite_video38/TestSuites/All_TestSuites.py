import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturns import PaymentReturnsTest

# Get all tests from LoginTest, SignupTest, PaymentTest and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creation test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # Sanity test suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # functional test suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # master test suite (returns all)

unittest.TextTestRunner(verbosity=2).run(sanityTestSuite) # verbosity give logs details in console window.

