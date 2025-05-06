package koorkah;

import org.junit.jupiter.api.Test;

class TestCapture extends BaseT
{

    @Test
    void testCapture()
    {
        String expression = koorkah.toRegEx("capture{ wild }");
        assertRegexIs("(.)", expression);
    }
    
    @Test
    void testCaptureComplex()
    {
        String expression = koorkah.toRegEx("capture{ wild `123` }");
        assertRegexIs("(.123)", expression);
    }
    
    @Test
    void testCaptureNamed()
    {
        String expression = koorkah.toRegEx("capture{ wild , `sam` }");
        assertRegexIs("(?<sam>.)", expression);
    }
    
    @Test
    void testCaptureNamedComplex()
    {
        String expression = koorkah.toRegEx("capture{ wild `animals` , `sam` }");
        assertRegexIs("(?<sam>.animals)", expression);
    }


}
