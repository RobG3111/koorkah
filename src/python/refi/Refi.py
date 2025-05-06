import sys
from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream, InputStream
from refi import RefiLexer
from refi import RefiParser
from refi import RefiListener

class Refi:


    def Refi():

        pass

 

    def toRegEx(self, expression: str) -> str:

        inputStream = InputStream(expression)
        lexer = RefiLexer.RefiLexer(input=inputStream)
        tokens = CommonTokenStream(lexer)
        parser = RefiParser.RefiParser(tokens)
        walker = ParseTreeWalker()
        listener = RefiListener.RefiListener()
        walker.walk(listener, parser.expression())
        return listener.buffer



if __name__ == '__main__':
    Refi()