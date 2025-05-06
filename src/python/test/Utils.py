import unittest
import re

class Utils(unittest.TestCase):

    def assertRegexMatchesText(self, expression: str, text:str) -> None:
        compiledEx = re.compile(expression)
        self.assertTrue(compiledEx.match(text), f"Expected {text} to match {expression}")

    def assertRegexDoesntMatchText(self, expression: str, text:str) -> None:
        compiledEx = re.compile(expression)
        self.assertFalse(compiledEx.match(text), f"Expected {text} to not match {expression}")

    def assertRegexIs(self, expected: str, actual: str) -> None:
        self.assertEqual(expected, actual, "Wrong Regular Expression created;")