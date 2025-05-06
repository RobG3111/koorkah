import unittest
from Utils import Utils 
from Refi import Refi



class TestEither(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_Either(self):


        expression = self.refi.toRegEx("`a` either{`b`, `c`} `d`")
        self.utils.assertRegexIs("a[bc]d", expression)
        self.utils.assertRegexMatchesText(expression, "abd")
        self.utils.assertRegexMatchesText(expression, "acd")
        self.utils.assertRegexDoesntMatchText(expression, "ad")
        self.utils.assertRegexDoesntMatchText(expression, "amd")      
    
    def test_EitherComplex(self):

        expression = self.refi.toRegEx("`a` either{`b`, `c`, `d`} `e`")
        self.utils.assertRegexIs("a[bcd]e", expression)
        self.utils.assertRegexMatchesText(expression, "abe")
        self.utils.assertRegexMatchesText(expression, "ace")
        self.utils.assertRegexMatchesText(expression, "ade")
        self.utils.assertRegexDoesntMatchText(expression, "ad")
        self.utils.assertRegexDoesntMatchText(expression, "amd")      


    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


