package koorkah;

import org.junit.jupiter.api.Test;

class TestAtLeast extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("atleast{2, `q`}");
        assertRegexIs("q{2,}", expression);;
        assertRegexMatchesText(expression, "qq");
        assertRegexMatchesText(expression, "qqqq");
        assertRegexDoesntMatchText(expression, "q");
    }
    
    @Test
    void testComplex()
    {
        String expression = koorkah.toRegEx("atleast{2, digit}");
        assertRegexIs("\\d{2,}", expression);;
        assertRegexMatchesText(expression, "12");
        assertRegexMatchesText(expression, "1345");
        assertRegexDoesntMatchText(expression, "0");
    }


}
