import unittest
from Utils import Utils 
from Refi import Refi


class TestExactly(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("exactly{7, `q`}")
        self.utils.assertRegexIs("q{7}", expression)
        self.utils.assertRegexMatchesText(expression, "qqqqqqq")
        self.utils.assertRegexDoesntMatchText(expression, "qqqqqq")
        self.utils.assertRegexDoesntMatchText(expression, "qqqqqqqq")

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


