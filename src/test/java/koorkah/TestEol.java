package koorkah;

import org.junit.jupiter.api.Test;

class TestEol extends BaseT
{

    @Test
    void testEolOnly()
    {
        Koorkah koorkah = new Koorkah();
        String expression = koorkah.toRegEx("`abc` eol");
        assertRegexIs("abc$", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexDoesntMatchText(expression, "abcd");
    }
    
    @Test
    void testBolAndEol()
    {
        Koorkah koorkah = new Koorkah();
        String expression = koorkah.toRegEx("bol `abc` eol");
        assertRegexIs("^abc$", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexDoesntMatchText(expression, " abc ");
    }
}
