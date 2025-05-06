import unittest
from Utils import Utils 
from Refi import Refi


class TestCapture(unittest.TestCase):

    def setUp(self):
        self.refi = Refi()
        self.utils = Utils()


    def test_Capture(self):

        expression = self.refi.toRegEx("capture{ wild }")
        self.utils.assertRegexIs("(.)", expression)
    
    def test_CaptureComplex(self):

        expression = self.refi.toRegEx("capture{ wild `123` }")
        self.utils.assertRegexIs("(.123)", expression)
    
    def test_CaptureNamed(self):

        expression = self.refi.toRegEx("capture{ wild , `sam` }")
        self.utils.assertRegexIs("(?<sam>.)", expression)
    
    def test_CaptureNamedComplex(self):

        expression = self.refi.toRegEx("capture{ wild `animals` , `sam` }")
        self.utils.assertRegexIs("(?<sam>.animals)", expression)


    def runTest(self):
        pass  

if __name__ == '__main__':
    unittest.main()    
    


