import unittest
from Utils import Utils 
from Refi import Refi


class TestLatin(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("latin")
        self.utils.assertRegexIs("\\p{IsLatin}", expression)
        self.utils.assertRegexMatchesText(expression, "A")
        self.utils.assertRegexDoesntMatchText(expression, "\\u0393")

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


