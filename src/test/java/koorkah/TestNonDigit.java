package koorkah;

import org.junit.jupiter.api.Test;

class TestNonDigit extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("nondigit");
        assertRegexIs("\\D", expression);
        assertRegexMatchesText(expression, "x");
        assertRegexDoesntMatchText(expression, "4");
        
    }

}
