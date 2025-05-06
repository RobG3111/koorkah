import unittest
from Utils import Utils 
from Refi import Refi


class TestUpper(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("upper")
        self.utils.assertRegexIs("\\p{Upper}", expression)
        self.utils.assertRegexMatchesText(expression, "A")
        self.utils.assertRegexDoesntMatchText(expression, "a")

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


