import unittest
from Utils import Utils 
from Refi import Refi


class TestGreek(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("greek")
        self.utils.assertRegexIs("\\p{InGreek}", expression)
        self.utils.assertRegexMatchesText(expression, "\u0393")
        self.utils.assertRegexDoesntMatchText(expression, "4")
        

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


