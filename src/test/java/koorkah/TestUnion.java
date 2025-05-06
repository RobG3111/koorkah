package koorkah;

import org.junit.jupiter.api.Test;

class TestUnion extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("union{`a`:`c` , `5`:`9`}");
        assertRegexIs("[a-c[5-9]]", expression);
        assertRegexMatchesText(expression, "a");
        assertRegexMatchesText(expression, "6");
        assertRegexDoesntMatchText(expression, "f");
        assertRegexDoesntMatchText(expression, "2");      
    }

}
