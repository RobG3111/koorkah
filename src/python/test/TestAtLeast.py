import unittest
from Utils import Utils 
from Refi import Refi

class TestAtLeast(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()

    def test_AtLeast(self):
     
        expression = self.refi.toRegEx("atleast{2, `q`}")
        self.utils.assertRegexIs("q{2,}", expression)
        self.utils.assertRegexMatchesText(expression, "qq")
        self.utils.assertRegexMatchesText(expression, "qqqq")
        self.utils.assertRegexDoesntMatchText(expression, "q")

    def test_AtLeastComplex(self):

        expression = self.refi.toRegEx("atleast{2, digit}")
        self.utils.assertRegexIs("\\d{2,}", expression)
        self.utils.assertRegexMatchesText(expression, "12")
        self.utils.assertRegexMatchesText(expression, "1345")
        self.utils.assertRegexDoesntMatchText(expression, "0")

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()