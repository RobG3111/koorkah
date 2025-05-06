package koorkah;

import org.junit.jupiter.api.Test;

class TestBacktick extends BaseT
{

    @Test
    void testOneBacktick()
    {
        String expression = koorkah.toRegEx("backtick");
        assertRegexIs("`", expression);;
    }
    
    @Test
    void testManyBacktick()
    {
        String expression = koorkah.toRegEx("backtick `green` backtick");
        assertRegexIs("`green`", expression);;
    }
    

}
