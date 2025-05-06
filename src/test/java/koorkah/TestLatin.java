package koorkah;

import org.junit.jupiter.api.Test;

class TestLatin extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("latin");
        assertRegexIs("\\p{IsLatin}", expression);
        assertRegexMatchesText(expression, "A");
        assertRegexDoesntMatchText(expression, "\\u0393");
    }

}
