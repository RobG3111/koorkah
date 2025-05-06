package koorkah;

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class FileConvertor
{
    private List<String> lines = new ArrayList<>();


    public FileConvertor(String[] args) throws IOException
    {
        File sourceDir = new File(args[0]);
        if (! sourceDir.exists())
            throw new IOException("Source directory does not exist");
        
        if ( ! sourceDir.isDirectory())
            throw new IOException("Source directory is not a directory");
        
        File targetDir = new File(args[1]);
        if (! targetDir.exists())
            throw new IOException("Target directory does not exist");
        
        if ( ! targetDir.isDirectory())
            throw new IOException("Target directory is not a directory");
        
        for (File javaFile : sourceDir.listFiles())
        {
            if (javaFile.isFile())
            {
                String name = javaFile.getName();
                String pyName = name.replace(".java", ".py");
                File pyFile = new File(targetDir, pyName);
                if (pyFile.exists())
                    System.out.println("Skipped " + pyFile);
                else
                {
                    convertAFile(javaFile, pyFile);
                    System.out.println("Created " + pyFile);
                }
            }
        }
    }
    
    private void convertAFile(File source, File target)
    {
        lines = new ArrayList<>();
        try(BufferedReader reader = new BufferedReader(new FileReader(source)))
        {
            String text;
            while ((text = reader.readLine()) != null)
            {
                lines.add(text);
            }
            
        }
        catch (IOException exception)
        {
            exception.printStackTrace();
        }
        
        replace(" extends BaseT", "(unittest.TestCase):");
        replace(" String", "");
        replace(" refi.", " self.refi.");
        replace(" assertRegex", " self.utils.assertRegex");
        replace(" void ", " def ");
        replace("()", "(self):\n");
        replace(" def test", " def test_");
        replace(";", "");
        replaceRegex(";$", "");
        deleteLineWith("@Test");
        deleteLineWith("package koorkah");
        deleteLineWith("import ");
        deleteLineMatchRegex("^\\{");
        deleteLineMatchRegex("^\\}");
        deleteLineMatchRegex("^    \\{");
        deleteLineMatchRegex("^    \\}");
        
        insertAtTop("import unittest\r\n"
                + "from Utils import Utils \r\n"
                + "from Koorkah import Koorkah");
        
        insertAtEnd("    def runTest(self):\r\n"
                + "        pass  \r\n"
                + "\r\n"
                + "if __name__ == '__main__':\r\n"
                + "    unittest.main()    \r\n"
                + "    \r\n"
                + "\r\n");
        
        insertAfterMatch("(unittest.TestCase):", 
                "\r\n"
                + "    def setUp(self):\r\n"
                + "        self.refi = Koorkah()\r\n"
                + "        self.utils = Utils()\r\n");

        try(PrintWriter writer = new PrintWriter(new FileWriter(target)))
        {
            for (String line : lines)
            {
                writer.println(line);
            }
        }
        catch (IOException exception)
        {
            exception.printStackTrace();
        }
        
    }
    

    private void replace(String search, String with)
    {
        for (int i = 0; i < lines.size(); i++)
        {
            String line = lines.get(i);
            lines.set(i, line.replace(search, with));
        }
    }
    
    private void replaceRegex(String regex, String with)
    {
        Pattern pattern = Pattern.compile(regex);
        for (int i = 0; i < lines.size(); i++)
        {
            String line = lines.get(i);
            Matcher matcher = pattern.matcher(lines.get(i));
            if (matcher.matches())
            {
                lines.set(i, matcher.replaceAll(with));
            }
        }
    }
    
    private void deleteLineWith(String search)
    {
        int i =0;
        while (i < lines.size())
        {
            if (lines.get(i).contains(search))
                lines.remove(i);
            else
                ++i;
        }
    }
    
    private void deleteLineMatchRegex(String regex)
    {
        Pattern pattern = Pattern.compile(regex);
        
        int i =0;
        while (i < lines.size())
        {
            if (pattern.matcher(lines.get(i)).matches())
                lines.remove(i);
            else
                ++i;
        }
    }
    
    private void insertAtTop(String text)
    {
        lines.add(0, text);
    }
    
    private void insertAtEnd(String text)
    {
        lines.add(text);
    }

    private void insertAfterMatch(String search, String text)
    {
        int i =0;
        while (i < lines.size())
        {
            if (lines.get(i).contains(search))
            {
                lines.add(i+1, text);
                break;
            }
            else
                ++i;
        }        
    }



    public static void main(String[] args)
    {
        try
        {
            new FileConvertor(args);
        }
        catch (IOException exception)
        {
            exception.printStackTrace();
        }
        
    }

}
