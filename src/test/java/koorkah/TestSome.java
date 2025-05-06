package koorkah;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.antlr.v4.runtime.misc.ParseCancellationException;
import org.junit.jupiter.api.Test;

class TestSome extends BaseT
{

    @Test
    void test()
    {
        String expression = koorkah.toRegEx("`a` some{`b`} `c`");
        assertRegexIs("ab+c", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexMatchesText(expression, "abbbc");
        assertRegexDoesntMatchText(expression, "ac");
        assertRegexDoesntMatchText(expression, "asc");      
    }
    
    @Test
    void testPosses()
    {
        String expression = koorkah.toRegEx("`a` some{`b`, posses} `c`");
        assertRegexIs("ab++c", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexMatchesText(expression, "abbbc");
        assertRegexDoesntMatchText(expression, "ac");
        assertRegexDoesntMatchText(expression, "asc");      
    }
    
    @Test
    void testReluct()
    {
        String expression = koorkah.toRegEx("`a` some{`b`, reluct} `c`");
        assertRegexIs("ab+?c", expression);
        assertRegexMatchesText(expression, "abc");
        assertRegexMatchesText(expression, "abbbc");
        assertRegexDoesntMatchText(expression, "ac");
        assertRegexDoesntMatchText(expression, "asc");      
    }
    
    @Test
    void testBadExpression()
    {
       Exception exception = assertThrows(ParseCancellationException.class, () -> koorkah.toRegEx("`a` some{`b` digit} `c`"));
       assertTrue(exception.getMessage().contains("extraneous input 'digit'") );
    }



}
