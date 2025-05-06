package koorkah;

import org.junit.jupiter.api.Test;

class TestGreek extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("greek");
        assertRegexIs("\\p{InGreek}", expression);
        assertRegexMatchesText(expression, "\u0393");
        assertRegexDoesntMatchText(expression, "4");
        
    }

}
