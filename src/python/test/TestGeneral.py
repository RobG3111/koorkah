import unittest
from Utils import Utils 
from Refi import Refi
 
class TestGeneral(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()

    def test_UnknownToken(self):

        with self.assertRaises(Exception):
            self.refi.toRegEx("green")
    
    def test_Example(self):
          
        expression = self.refi.toRegEx("bol capture{ somespace `cat` somespace } eol")
        self.utils.assertRegexIs(r"^(\p{Space}+cat\p{Space}+)$", expression)
        self.utils.assertRegexMatchesText(expression, " cat ")
        self.utils.assertRegexMatchesText(expression, "   cat   ")
        self.utils.assertRegexDoesntMatchText(expression, "cat  ") 
        self.utils.assertRegexDoesntMatchText(expression, "   cat") 


    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


