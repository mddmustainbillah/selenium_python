import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentinDollor(self):
        print("This is payment in dollor test.")
        self.assertTrue(True)

    def test_paymentinTaka(self):
        print("This is payment in taka test.")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
