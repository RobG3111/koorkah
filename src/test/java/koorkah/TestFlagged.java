package koorkah;

import org.junit.jupiter.api.Test;

class TestFlagged extends BaseT
{

    @Test
    void testFlagged()
    {
        String expression = koorkah.toRegEx("`a` flagged { caseIns , `b` } `c`");
        assertRegexIs("a(?i:b)c", expression);
        assertRegexMatchesText(expression, "aBc");
        assertRegexMatchesText(expression, "abc");
        assertRegexDoesntMatchText(expression, "Axe"); 
    }
    
    @Test
    void testFlaggedComplex()
    {
        String expression = koorkah.toRegEx("`a` flagged { caseIns , (`b` digit) } `c`");
        assertRegexIs("a(?i:(b\\d))c", expression);
        assertRegexMatchesText(expression, "aB1c");
        assertRegexMatchesText(expression, "ab1c");
        assertRegexDoesntMatchText(expression, "Ax1e"); 
    }
}
