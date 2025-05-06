package koorkah;

import org.junit.jupiter.api.Test;

class TestAny extends BaseT
{

    @Test
    void testAny()
    {
        String expression = koorkah.toRegEx("`a` any{`b`} `c`");
        assertRegexIs("ab*c", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexMatchesText(expression, "abbbc");
        assertRegexMatchesText(expression, "ac");
        assertRegexDoesntMatchText(expression, "asc");       
    }

}
