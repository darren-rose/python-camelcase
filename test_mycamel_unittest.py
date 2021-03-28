import mycamel
import unittest

class TestSum(unittest.TestCase):

    def test_toCamel(self):
        self.assertEqual(mycamel.toCamel("hello world"), "Hello World", "Should be Hello World")

if __name__ == "__main__":
    unittest.main()


