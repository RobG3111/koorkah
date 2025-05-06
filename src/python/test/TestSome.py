import unittest
from Utils import Utils 
from Refi import Refi



class TestSome(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("`a` some{`b`} `c`")
        self.utils.assertRegexIs("ab+c", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexMatchesText(expression, "abbbc")
        self.utils.assertRegexDoesntMatchText(expression, "ac")
        self.utils.assertRegexDoesntMatchText(expression, "asc")      
    
    def test_Posses(self):

        expression = self.refi.toRegEx("`a` some{`b`, posses} `c`")
        self.utils.assertRegexIs("ab++c", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexMatchesText(expression, "abbbc")
        self.utils.assertRegexDoesntMatchText(expression, "ac")
        self.utils.assertRegexDoesntMatchText(expression, "asc")      
    
    def test_Reluct(self):

        expression = self.refi.toRegEx("`a` some{`b`, reluct} `c`")
        self.utils.assertRegexIs("ab+?c", expression)
        self.utils.assertRegexMatchesText(expression, "abc")
        self.utils.assertRegexMatchesText(expression, "abbbc")
        self.utils.assertRegexDoesntMatchText(expression, "ac")
        self.utils.assertRegexDoesntMatchText(expression, "asc")      
    
    def test_BadExpression(self):

       Exception exception = assertThrows(ParseCancellationException.class, (self):
 -> self.refi.toRegEx("`a` some{`b` digit} `c`"))
       assertTrue(exception.getMessage(self):
.contains("extraneous input 'digit'") )



    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


