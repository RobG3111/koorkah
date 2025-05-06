package koorkah;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.regex.*;

import org.junit.jupiter.api.*;

@TestMethodOrder(MethodOrderer.MethodName.class)
public class BaseT
{
    protected Koorkah koorkah = new Koorkah();
    
    public void assertRegexMatchesText(String regex, String text)
    {
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text); 
        assertTrue(matcher.matches(), () -> String.format("Expected %s to match %s", text, regex));
    }
    
    public void assertRegexDoesntMatchText(String regex, String text)
    {
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text); 
        assertFalse(matcher.matches(), () -> String.format("Expected %s to not match %s", text, regex));
    }
    
    public void assertRegexIs(String expected, String actual)
    {
        assertEquals(expected, actual, () -> "Wrong Regular Expression created;");
    }


}