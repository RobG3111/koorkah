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
    
    public String toRegEx(String refiExpression)
    {
        walker = new KoorkahWalker();
        return walker.toRegEx(refiExpression);
    }
    
    public Pattern toPattern(String refiExpression)
    {
        return Pattern.compile(toRegEx(refiExpression), walker.getFlags());
    }
    
    public int getFlags()
    {
        return walker.getFlags();
    }
    
}
