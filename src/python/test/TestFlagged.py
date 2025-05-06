import unittest
from Utils import Utils 
from Refi import Refi

class TestFlagged(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_Flagged(self):

        expression = self.refi.toRegEx("`a` flagged { caseIns , `b` } `c`")
        self.utils.assertRegexIs("a(?i:b)c", expression)
        self.utils.assertRegexMatchesText(expression, "aBc")
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexDoesntMatchText(expression, "Axe") 
    
    def test_FlaggedComplex(self):

        expression = self.refi.toRegEx("`a` flagged { caseIns , (`b` digit) } `c`")
        self.utils.assertRegexIs("a(?i:(b\\d))c", expression)
        self.utils.assertRegexMatchesText(expression, "aB1c")
        self.utils.assertRegexMatchesText(expression, "ab1c")
        self.utils.assertRegexDoesntMatchText(expression, "Ax1e") 
    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


