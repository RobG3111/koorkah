package koorkah;

import org.junit.jupiter.api.Test;

class TestUpper extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("upper");
        assertRegexIs("\\p{Upper}", expression);
        assertRegexMatchesText(expression, "A");
        assertRegexDoesntMatchText(expression, "a");
    }

}
