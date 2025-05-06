package koorkah;

import org.junit.jupiter.api.Test;

class TestOptional extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("`a` optional{`b`} `c`");
        assertRegexIs("ab?c", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexMatchesText(expression, "ac");
        assertRegexDoesntMatchText(expression, "abbc"); 
    }
    
    @Test
    void testComplex()
    {
        String expression = koorkah.toRegEx("`a` optional{ (`b` digit) } `c`");
        assertRegexIs("a(b\\d)?c", expression);
        assertRegexMatchesText(expression, "ab3c");
        assertRegexMatchesText(expression, "ac");
        assertRegexDoesntMatchText(expression, "abbc"); 
    }


}
