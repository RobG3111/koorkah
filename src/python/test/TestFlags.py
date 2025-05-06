import unittest
from Utils import Utils 
from Refi import Refi


class TestFlags (unittest.TestCase):


    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()
    
    def  testCaseInsens(self):
    
        expression = self.refi.toRegEx("caseins `a`")
        self.utils.assertRegexIs("(?i)a", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexMatchesText(expression, "A")
    
    def  testFlagsVerb(self):
    
        expression = self.refi.toRegEx("`flags{caseIns}  `a`")
        self.utils.assertRegexIs("(?i)a", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexMatchesText(expression, "A")
    
    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


    

