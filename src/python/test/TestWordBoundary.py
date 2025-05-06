import unittest
from Utils import Utils 
from Refi import Refi


class TestWordBoundary(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("` ` wordboundary `word`")
        self.utils.assertRegexIs(" \\bword", expression)
        self.utils.assertRegexMatchesText(expression, " word")
        self.utils.assertRegexDoesntMatchText(expression, "4")       

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


