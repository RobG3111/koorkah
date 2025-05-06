

import unittest

import Utils
import Refi

class TestAny(unittest.TestCase):

    def setUp(self):
        self.refi = Refi.Refi()
        self.utils = Utils.Utils();

    def test_Any(self):
     
        expression = self.refi.toRegEx("`a` any{`b`} `c`")
        self.utils.assertRegexIs("ab*c", expression);
        self.utils.assertRegexMatchesText(expression, "abc");
        self.utils.assertRegexMatchesText(expression, "abbbc");
        self.utils.assertRegexMatchesText(expression, "ac");
        self.utils.assertRegexDoesntMatchText(expression, "asc"); 

    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()