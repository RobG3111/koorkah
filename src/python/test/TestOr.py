import unittest
from Utils import Utils 
from Refi import Refi


class TestOr(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("or{ `r` | digit}")
        self.utils.assertRegexIs("r|\\d", expression)
        self.utils.assertRegexMatchesText(expression, "r")
        self.utils.assertRegexMatchesText(expression, "4")
        self.utils.assertRegexDoesntMatchText(expression, "abcd")
     }
    
    def test_OrComplex(self):

        expression = self.refi.toRegEx("or{ (wild `a`) | digit}")
        self.utils.assertRegexIs("(.a)|\\d", expression)
        self.utils.assertRegexMatchesText(expression, "wa")
        self.utils.assertRegexMatchesText(expression, "4")
        self.utils.assertRegexDoesntMatchText(expression, "abcd")
     }

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


