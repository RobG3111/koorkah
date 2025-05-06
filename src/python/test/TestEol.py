import unittest
from Utils import Utils 
from Refi import Refi


class TestEol(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_EolOnly(self):

        expression = self.refi.toRegEx("`abc` eol")
        self.utils.assertRegexIs("abc$", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexDoesntMatchText(expression, "abcd")
    
    def test_BolAndEol(self):

        expression = self.refi.toRegEx("bol `abc` eol")
        self.utils.assertRegexIs("^abc$", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexDoesntMatchText(expression, " abc ")
    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


