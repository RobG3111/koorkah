import unittest
from Utils import Utils 
from Refi import Refi


class TestLower(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("lower")
        self.utils.assertRegexIs("\\p{Lower}", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexDoesntMatchText(expression, "A")

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


