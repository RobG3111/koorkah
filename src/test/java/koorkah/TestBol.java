package koorkah;

import org.junit.jupiter.api.Test;

class TestBol  extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("bol `123`");
        assertRegexIs("^123", expression);
        assertRegexMatchesText(expression, "123");
        assertRegexDoesntMatchText(expression, "4123");    
    }

}
    