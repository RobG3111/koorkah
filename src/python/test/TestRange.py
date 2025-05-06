import unittest
from Utils import Utils 
from Refi import Refi


class TestRange(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_Simple(self):

        expression = self.refi.toRegEx("range{`a`:`c`}")
        self.utils.assertRegexIs("[a-c]", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexMatchesText(expression, "c")
        self.utils.assertRegexDoesntMatchText(expression, "f")
        self.utils.assertRegexDoesntMatchText(expression, "2")      
    
    def test_Complex(self):

        expression = self.refi.toRegEx("range{`a`:`c`, `6`:`9`}")
        self.utils.assertRegexIs("[a-c6-9]", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexMatchesText(expression, "7")
        self.utils.assertRegexDoesntMatchText(expression, "f")
        self.utils.assertRegexDoesntMatchText(expression, "2")      

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


