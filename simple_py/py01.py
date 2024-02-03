import pytest
from prog import fact
def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800

# Run the tests
test_fact()


import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(1, 7), 8)
        self.assertEqual(add_numbers(5, 5), 10)
        self.assertEqual(add_numbers(10, 0), 10)

if __name__ == '__main__':
    unittest.main()
