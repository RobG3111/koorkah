package koorkah;

import org.junit.jupiter.api.Test;

class TestWordBoundary extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("` ` wordboundary `word`");
        assertRegexIs(" \\bword", expression);
        assertRegexMatchesText(expression, " word");
        assertRegexDoesntMatchText(expression, "4");       
    }

}
