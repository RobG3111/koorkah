import unittest
from Utils import Utils 
from Refi import Refi


class TestUnion(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("union{`a`:`c` , `5`:`9`}")
        self.utils.assertRegexIs("[a-c[5-9]]", expression)
        self.utils.assertRegexMatchesText(expression, "a")
        self.utils.assertRegexMatchesText(expression, "6")
        self.utils.assertRegexDoesntMatchText(expression, "f")
        self.utils.assertRegexDoesntMatchText(expression, "2")      

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


