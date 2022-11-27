import unittest
import app as tapp
import json

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = tapp.app.test_client()

    def test_print_item(self):
        r = self.app.get('/')
        self.assertEqual(r.print_item(r.box, 'cheese'), 35)

    def test_print_basket_len(self):
        r = self.app.get('/')
        self.assertEqual(r.print_basket_len(r.box), 5)
if __name__ == '__main__':
    unittest.main()