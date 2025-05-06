package koorkah;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class TestStrings extends BaseT
{

    @Test
    void testString()
    {
        String expression = koorkah.toRegEx("`ab`");
        assertRegexIs("ab", expression);
        
        expression = koorkah.toRegEx("`!`");
        assertRegexIs("!", expression);
        
        expression = koorkah.toRegEx("`!` `the` ` cat`");
        assertRegexIs("!the cat", expression);
        
        expression = koorkah.toRegEx("(`!` `the` ` cat`)");
        assertRegexIs("(!the cat)", expression);
    }
    
    @Test
    void testUnenclosedString()
    {
        Exception exception = assertThrows(RuntimeException.class, () ->
            (new Koorkah()).toRegEx("ab"));  
        assertTrue(exception.getMessage().contains("token recognition error at: 'ab'"));
    }

}
