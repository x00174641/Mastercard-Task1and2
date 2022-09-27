import unittest
from main import most_frequent_integer

class MostFrequentIntegerTest(unittest.TestCase):
    def test_most_frequent_integer(self):
        # Data
        array = [4,5,6,7,7,7,8,9,9]
        # Expected outcome
        expected_result = 7
        # Actual outcome
        result = most_frequent_integer(array)
        # Assert
        self.assertEquals(result, expected_result)