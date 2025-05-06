package koorkah;

import org.junit.jupiter.api.Test;

class TestOr extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("or{ `r` | digit}");
        assertRegexIs("r|\\d", expression);
        assertRegexMatchesText(expression, "r");
        assertRegexMatchesText(expression, "4");
        assertRegexDoesntMatchText(expression, "abcd");
     }
    
    @Test
    void testOrComplex()
    {
        String expression = koorkah.toRegEx("or{ (wild `a`) | digit}");
        assertRegexIs("(.a)|\\d", expression);
        assertRegexMatchesText(expression, "wa");
        assertRegexMatchesText(expression, "4");
        assertRegexDoesntMatchText(expression, "abcd");
     }

}
