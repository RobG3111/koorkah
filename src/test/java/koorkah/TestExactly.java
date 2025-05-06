package koorkah;

import org.junit.jupiter.api.Test;

class TestExactly extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("exactly{7, `q`}");
        assertRegexIs("q{7}", expression);
        assertRegexMatchesText(expression, "qqqqqqq");
        assertRegexDoesntMatchText(expression, "qqqqqq");
        assertRegexDoesntMatchText(expression, "qqqqqqqq");
    }

}
