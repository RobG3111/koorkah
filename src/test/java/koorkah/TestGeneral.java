package koorkah;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

 
class TestGeneral extends BaseT
{
    @Test
    void testUnknownToken()
    {
        Exception exception = assertThrows(RuntimeException.class, () ->       
            koorkah.toRegEx("green"));
        assertTrue(exception.getMessage().contains("token recognition error at: 'green'"));
    }
    
    @Test
    void testExample()
    {
          
        String expression = koorkah.toRegEx("bol capture{ somespace `cat` somespace } eol");
        assertRegexIs("^(\\p{Space}+cat\\p{Space}+)$", expression);
        assertRegexMatchesText(expression, " cat ");
        assertRegexMatchesText(expression, "   cat   ");
        assertRegexDoesntMatchText(expression, "cat  "); 
        assertRegexDoesntMatchText(expression, "   cat"); 
    }


}
