import unittest
from Utils import Utils 
from Refi import Refi


class TestBol (unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_(self):

        expression = self.refi.toRegEx("bol `123`")
        self.utils.assertRegexIs("^123", expression)
        self.utils.assertRegexMatchesText(expression, "123")
        self.utils.assertRegexDoesntMatchText(expression, "4123")    

    
    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


