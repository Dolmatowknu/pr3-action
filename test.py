import unittest
import app as tapp
import json

class FlaskAppTests(unittest.TestCase):
    def test_print_item(self):
        self.assertEqual(tapp.print_item(tapp.box, 'cheese'), 35)

    def test_print_basket_len(self):
        self.assertEqual(tapp.print_basket_len(tapp.box), 5)

    

if __name__ == '__main__':
    unittest.main()