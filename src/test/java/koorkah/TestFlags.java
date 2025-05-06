package koorkah;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.regex.*;

import org.junit.jupiter.api.Test;

class TestFlags extends BaseT
{

    @Test
    void testCaseInsens()
    {
        String expression = koorkah.toRegEx("`a` caseIns `a`");
        assertRegexIs("a(?i)a", expression);
        assertRegexMatchesText(expression, "aa");
        assertRegexMatchesText(expression, "aA");
        assertRegexDoesntMatchText(expression, "AA"); 
    }

    @Test
    void testFlagsVerb()
    {
        String expression = koorkah.toRegEx("`a` flags { caseIns } `a`");
        assertRegexIs("a(?i)a", expression);
        assertRegexMatchesText(expression, "aa");
        assertRegexMatchesText(expression, "aA");
        assertRegexDoesntMatchText(expression, "AA"); 
    }
    
    @Test
    void testFlagsVerbOff()
    {
        String expression = koorkah.toRegEx("`a` flags { caseIns , unixlines, unicodecase } `a` flags { caseInsOff, unixlinesoff, unicodecaseoff} `W`");
        assertRegexIs("a(?i)a(?-i)W", expression);
        assertRegexMatchesText(expression, "aaW");
        assertRegexMatchesText(expression, "aAW");
        assertRegexDoesntMatchText(expression, "aaw"); 
    }
    
    @Test
    void testFlagsJavaOnly()
    {
        String regex ="unixlines `aW`";
        Pattern pattern = koorkah.toPattern(regex);
        assertEquals(Pattern.UNIX_LINES, pattern.flags());
        String text = "aW";
        Matcher matcher = pattern.matcher(text); 
        assertTrue(matcher.matches(), () -> String.format("Expected %s to match %s", text, regex));

    }
}
