import unittest
from Utils import Utils 
from Refi import Refi


class TestNonDigit(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("nondigit")
        self.utils.assertRegexIs("\\D", expression)
        self.utils.assertRegexMatchesText(expression, "x")
        self.utils.assertRegexDoesntMatchText(expression, "4")
        

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


