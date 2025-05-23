package koorkah;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TestEither extends BaseT
{

    @Test
    void testEither()
    {

        String expression = koorkah.toRegEx("`a` either{`b`, `c`} `d`");
        assertEquals("a[bc]d", expression);
        assertRegexMatchesText(expression, "abd");
        assertRegexMatchesText(expression, "acd");
        assertRegexDoesntMatchText(expression, "ad");
        assertRegexDoesntMatchText(expression, "amd");      
    }
    
    @Test
    void testEitherComplex()
    {
        String expression = koorkah.toRegEx("`a` either{`b`, `c`, `d`} `e`");
        assertEquals("a[bcd]e", expression);
        assertRegexMatchesText(expression, "abe");
        assertRegexMatchesText(expression, "ace");
        assertRegexMatchesText(expression, "ade");
        assertRegexDoesntMatchText(expression, "ad");
        assertRegexDoesntMatchText(expression, "amd");      
    }


}
