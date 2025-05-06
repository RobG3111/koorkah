import unittest
from Utils import Utils 
from Refi import Refi




public class BaseT
    protected Refi refi = new Refi(self):

    
    public def self.utils.assertRegexMatchesText(String regex, text)
        Pattern pattern = Pattern.compile(regex)
        Matcher matcher = pattern.matcher(text) 
        assertTrue(matcher.matches(self):
, (self):
 ->.format("Expected %s to match %s", text, regex))
    
    public def self.utils.assertRegexDoesntMatchText(String regex, text)
        Pattern pattern = Pattern.compile(regex)
        Matcher matcher = pattern.matcher(text) 
        assertFalse(matcher.matches(self):
, (self):
 ->.format("Expected %s to not match %s", text, regex))
    
    public def self.utils.assertRegexIs(String expected, actual)
        assertEquals(expected, actual, (self):
 -> "Wrong Regular Expression created")


    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


