package koorkah;

import org.junit.jupiter.api.Test;

class TestLower extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("lower");
        assertRegexIs("\\p{Lower}", expression);
        assertRegexMatchesText(expression, "a");
        assertRegexDoesntMatchText(expression, "A");
    }

}
