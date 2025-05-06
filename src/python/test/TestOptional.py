import unittest
from Utils import Utils 
from Refi import Refi


class TestOptional(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("`a` optional{`b`} `c`")
        self.utils.assertRegexIs("ab?c", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexMatchesText(expression, "ac")
        self.utils.assertRegexDoesntMatchText(expression, "abbc") 
    
    def test_Complex(self):

        expression = self.refi.toRegEx("`a` optional{ (`b` digit) } `c`")
        self.utils.assertRegexIs("a(b\\d)?c", expression)
        self.utils.assertRegexMatchesText(expression, "ab3c")
        self.utils.assertRegexMatchesText(expression, "ac")
        self.utils.assertRegexDoesntMatchText(expression, "abbc") 


    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


