import unittest
from Utils import Utils 
from Refi import Refi



class TestStrings(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_String(self):

        expression = self.refi.toRegEx("`ab`")
        self.utils.assertRegexIs("ab", expression)
        
        expression = self.refi.toRegEx("`!`")
        self.utils.assertRegexIs("!", expression)
        
        expression = self.refi.toRegEx("`!` `the` ` cat`")
        self.utils.assertRegexIs("!the cat", expression)
        
        expression = self.refi.toRegEx("(`!` `the` ` cat`)")
        self.utils.assertRegexIs("(!the cat)", expression)
    
    def test_UnenclosedString(self):

        Exception exception = assertThrows(RuntimeException.class, (self):
 ->
            (new Refi(self):
).toRegEx("ab"))  
        assertTrue(exception.getMessage(self):
.contains("token recognition error at: 'ab'"))

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


