import unittest
from Utils import Utils 
from Refi import Refi


class TestBacktick(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_OneBacktick(self):

        expression = self.refi.toRegEx("backtick")
        self.utils.assertRegexIs("`", expression)
    
    def test_ManyBacktick(self):

        expression = self.refi.toRegEx("backtick `green` backtick")
        self.utils.assertRegexIs("`green`", expression)
    

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


