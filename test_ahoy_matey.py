#import unittest
import unittest

#import or define method to be tested
from ahoy_matey import*

class Test(unittest.TestCase):

    def test_is_worth_it(self):
        titanic = Ship(15, 10)
        self.assertFalse(titanic.is_worth_it())

    def test_is_worth_it_greater_than_20(self):
        flying_dutchman = Ship(45, 5)
        self.assertTrue(flying_dutchman.is_worth_it())

    def test_is_worth_it_equal_to_20(self):
        titanic_2 = Ship(35, 10)
        self.assertFalse(titanic_2.is_worth_it())

if __name__ == '__main__':
    unittest.main()
