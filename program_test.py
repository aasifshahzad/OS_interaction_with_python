# Start of Program

from program import rearrange_name
import unittest

class TestProgram(unittest.TestCase):
    def test_basic(self):
        testcase = 'M. Asif, Shahzad'
        expected  = 'Shahzad M. Asif'
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
