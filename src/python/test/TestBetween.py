import unittest
from Utils import Utils 
from Refi import Refi


class TestBetween(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("between{2, 4, `q`}")
        self.utils.assertRegexIs("q{2,4}", expression)
        self.utils.assertRegexMatchesText(expression, "qq")
        self.utils.assertRegexMatchesText(expression, "qqq")
        self.utils.assertRegexMatchesText(expression, "qqqq")
        self.utils.assertRegexDoesntMatchText(expression, "q")    
        self.utils.assertRegexDoesntMatchText(expression, "qqqqq")    
    
    def test_Expression(self):

        expression = self.refi.toRegEx("between{2, 4, (digit wild)}")
        self.utils.assertRegexIs("(\\d.){2,4}", expression)
        self.utils.assertRegexMatchesText(expression, "2w3e")
        self.utils.assertRegexMatchesText(expression, "1a3t5j")
        self.utils.assertRegexMatchesText(expression, "7u4r5c2v")
        self.utils.assertRegexDoesntMatchText(expression, "1f")    
        self.utils.assertRegexDoesntMatchText(expression, "2r5c6b7m9l")    

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


