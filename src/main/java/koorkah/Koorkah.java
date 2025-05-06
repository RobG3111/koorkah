package koorkah;

import java.util.regex.*;

public class Koorkah 
{

    
    
    private KoorkahWalker walker;


    public static void main(String[] args)
    {
        Koorkah koorkah = new Koorkah();
        Pattern pattern = koorkah.toPattern("capture{`a`, `zzz`}");
        String text = "a";
        Matcher matcher = pattern.matcher(text); 
        System.out.println("Matches " + text + " " + matcher.matches());
    }

    
    public Koorkah()
    {
        
    }
    
    public String toRegEx(String koorkahExpression)
    {
        walker = new KoorkahWalker();
        return walker.toRegEx(koorkahExpression);
    }
    
    public Pattern toPattern(String koorkahExpression)
    {
        return Pattern.compile(toRegEx(koorkahExpression), walker.getFlags());
    }
    
    public int getFlags()
    {
        return walker.getFlags();
    }
    
}
