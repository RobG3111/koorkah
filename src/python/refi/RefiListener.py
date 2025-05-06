from RefiParserListener import RefiParserListener
from RefiParser import RefiParser
from antlr4 import TerminalNode

class RefiListener(RefiParserListener):

    def __init__(self) -> None:
        self.emitClosingBracket = False
        self.bracketCount = 0
        self.buffer = ""
    
    def emit(self, text: str) -> None:
        self.buffer += text

    def exitAlphabetic(self, ctx: RefiParser.AlphabeticContext) -> None:
        self.emit("\\p{IsAlphabetic}")

    
    def exitBacktick(self, context: RefiParser.BacktickContext):
    
       self.emit("`")
    
    
  
    def exitBol(self, context: RefiParser.BolContext):
    
       self.emit("^")
    
    
    
  
    def exitEol(self, context: RefiParser.EolContext):
       self.emit("$")
    
    
  
    def exitMatcher_name(self, context: RefiParser.Matcher_nameContext):
       pass
    
    def visitTerminal(self, node:TerminalNode):
    
        terminal = node.getText()
        match (terminal):
        
            case "|":
                self.emit("|")
                
            case "(":
                if self.emitClosingBracket:
                    ++self.bracketCount
                
            case ")":
                if self.emitClosingBracket:
                
                    --self.bracketCount
                    if self.bracketCount == 0:
                       self.emit(")")
                
  
    def enterExpression(self, context: RefiParser.ExpressionContext):
        pass
  
    def exitExpression(self, context: RefiParser.ExpressionContext):
        pass
  
    def enterMatcher(self, context: RefiParser.MatcherContext):
        pass
    
    def exitMatcher(self, context: RefiParser.MatcherContext):
        pass
    

    
    def fixString(self, fix: str) -> str:
    
        return fix.replace("`", "").replace("\\", "\\\\")
  
    def exitWild(self, context: RefiParser.WildContext):
    
       self.emit(".")
    
    def exitExpr_param_matcher(self, context: RefiParser.Expr_param_matcherContext):
    
        child = context.getChild(0)
        name = child.getText().lower()

        match name:
        
            case "any":
               self.emit("*")
                
            case "optional":
               self.emit("?")
                    
            case "some":
               self.emit("+")
        
            case _:
                raise Exception("Unexpected matcher name: " + name)
        

        if context.matchType != None:
        
            match context.matchType.getText():
            
                case "reluct":
                   self.emit("?")
                    
                case "posses":
                   self.emit("+")
  
    def exitAnywild(self, context: RefiParser.AnywildContext):
    
       self.emit(".*")
    

    def exitRange_matcher(self, context: RefiParser.Range_matcherContext):
    
        self.emit("[")
        first = True
        for terminalNode in context.CHAR():
        
            self.emit(self.fixString(terminalNode.getText()))
            if first:
            
               self.emit("-")
            
            first = not first
        
        self.emit("]")
  
    def exitDigit(self, context: RefiParser.DigitContext):
    
       self.emit("\\d")
    
    def exitTab(self, context: RefiParser.TabContext):
    
       self.emit("\\t")
  
    def exitOctal_matcher(self, context: RefiParser.Octal_matcherContext):
    
       self.emit("\\\\O")
       self.emit(context.getChild(2).getText())
  
    def exitNewline(self, context: RefiParser.NewlineContext):
    
       self.emit("\\n")
  
    def exitFormfeed(self, context: RefiParser.FormfeedContext):
    
       self.emit("\\f")
  
    def exitReturn(self, context: RefiParser.ReturnContext):
    
       self.emit("\\r")
    
    def exitBell(self, context: RefiParser.BellContext):
    
       self.emit("\\a")
    
    def exitEscape(self, context: RefiParser.EscapeContext):
    
       self.emit("\\e")
  
    def exitCtrl_matcher(self, context: RefiParser.Ctrl_matcherContext):
    
       self.emit("\\c")
       self.emit(context.getChild(2).getText())
        
  
    def exitEither_matcher(self, context: RefiParser.Either_matcherContext):
        
        self.emit("[")
        for terminalNode in context.CHAR():
           self.emit(self.fixString(terminalNode.getText()))
        
        self.emit("]")      
    
    def exitChar(self, context: RefiParser.CharContext):
    
       self.emit(self.fixString(context.getText()))
    
    def exitString(self, context: RefiParser.StringContext):
    
       self.emit (self.fixString(context.getText()))

  
    def exitNot_matcher(self, context: RefiParser.Not_matcherContext):
    
        self.emit("[^")
        for terminalNode in context.CHAR():
           self.emit (self.fixString(terminalNode.getText()))
        
        self.emit("]")          

    def exitHex_matcher(self, context: RefiParser.Hex_matcherContext):
    
        self.emit("\\x")
        hexNumber = context.number.getText().substring(2)
        if len(hexNumber) == 1:
           self.emit("0")
        
        self.emit(hexNumber)
  
    def enterOr_matcher(self, context: RefiParser.Or_matcherContext):
    
        self.emit("(")    

  
    def exitOr_matcher(self, context: RefiParser.Or_matcherContext):

        self.emit(")")
    

    def enterCapture_matcher(self, context: RefiParser.Capture_matcherContext):
    
        
        self.emit("(")
        if context.name != None:
        
            name = context.name.text
            if len(name) > 0:
            
               self.emit("?<")
               self.emit (self.fixString(name))
               self.emit(">")
    

    def exitCapture_matcher(self, context: RefiParser.Capture_matcherContext):
    
       self.emit(")")
    
    def enterBacketed_matcher(self, context: RefiParser.Backeted_matcherContext):
    
       self.emit("(")
    
  
    def exitBacketed_matcher(self, context: RefiParser.Backeted_matcherContext):
    
       self.emit(")")
    
    def exitNondigit(self, context: RefiParser.NondigitContext):
    
       self.emit("\\D")
    
    def exitWordboundary(self, context: RefiParser.WordboundaryContext):
    
       self.emit("\\b")
    
    def exitCaseins(self, context: RefiParser.CaseinsContext):
    
       self.emit("(?i)")
  
    def exitUnicodecase(self, context: RefiParser.UnicodecaseContext):
        pass
    

    def exitUnixlines(self, context: RefiParser.UnixlinesContext):
    
        self.flagNameToRegExFlag("unixlines", True)
    

    def exitFlags(self, context: RefiParser.FlagsContext):
    
        offRules = []
        self.emit("(?")
        for flagnameContext in context.names:
        
            flagName = flagnameContext.getText().lower()
            if flagName.lower().endswith("off"):
                offRules.add(flagName)
            else:
                self.flagNameToRegExFlag(flagName, True)
        
        
        if len(offRules) != 0:
        
            self.emit("-")
            for flagName in offRules:
                self.flagNameToRegExFlag(flagName.replace("off", ""), False)
        
        self.emit(")")
    
    
    def flagNameToRegExFlag(self, flagName: str, on: bool) -> None:
    
        match(flagName):
        
            case "caseins":
                self.emit("i")

            case "unicodecase":
                self.changeFlag(1, on)
                
            case "unixlines":
                self.changeFlag(2, on)
        
    
    
    def changeFlag(self, flag: int, on: bool) -> int:
    
        if on:
            flags |= flag
        else:
            flags = flags & ( ~ flag)
    

    def exitCaseinsoff(self, context: RefiParser.CaseinsoffContext):
        pass
    
  
    def exitUnicodecaseoff(self, context: RefiParser.UnicodecaseoffContext):
        pass
  
    def exitUnixlinesoff(self, context: RefiParser.UnixlinesoffContext):
        pass
    
    def exitGreek(self, ctx: RefiParser.GreekContext):
    
       self.emit("\\p{InGreek}")
  
    def exitLatin(self, ctx: RefiParser.LatinContext):
    
       self.emit("\\p{IsLatin}")
    
  
    def exitAlphabetic(self, ctx: RefiParser.AlphabeticContext):
    
       self.emit("\\p{IsAlphabetic}")
    
  
    def exitCurrency(self, ctx: RefiParser.CurrencyContext):
    
       self.emit("\\p{Sc}")
    
    def exitUpper(self, ctx: RefiParser.UpperContext):
    
       self.emit("\\p{Upper}")

    def exitExactly(self, ctx: RefiParser.ExactlyContext):
    
       self.emit("{")
       self.emit(ctx.count.text)
       self.emit("}")    
    

    def exitAtleast(self, ctx: RefiParser.AtleastContext):
    
       self.emit("{")
       self.emit(ctx.count.text)
       self.emit(",}")    
  
    def exitBetween(self, ctx: RefiParser.BetweenContext):
    
       self.emit("{")
       self.emit(ctx.from_.text)
       self.emit(",")
       self.emit(ctx.to.text)
       self.emit("}")         
    
  
    def enterFlagged(self, context: RefiParser.FlaggedContext):
    
        offRules = []
        self.emit("(?")
        for flagnameContext in context.names:
        
            flagName = flagnameContext.getText().lower()
            if flagName.lower().endswith("off"):
                offRules.add(flagName)
            else:
                self.flagNameToRegExFlag(flagName, True)
        
        
        if len(offRules) > 0:
        
            self.emit("-")
            for flagName in offRules:
                self.flagNameToRegExFlag(flagName.replace("off", ""), False)
        
        self.emit(":")    
        self.emitClosingBracket = True
        self.bracketCount = 1
    
    def exitFlagged(self, context: RefiParser.FlaggedContext):
    
        if self.bracketCount == 1:
           self.emit(")")
        self.emitClosingBracket = False
  
    def exitSomespace(self, context: RefiParser.SomespaceContext):
    
       self.emit("\\p{Space}+")
    
  
    def exitUnion(self, context: RefiParser.UnionContext):
    
        self.emit("[")
        first = True
        count = 0
        for terminalNode in context.CHAR():
        
            self.emit (self.fixString(terminalNode.getText()))
            if first:
            
               self.emit("-")
            
            first = not first
            count = count + 1
            if count == 2:
                self.emit("[")
            else:
                if count == 4:
                   self.emit("]")
        
        self.emit("]")
    
  
    def exitLower(self, context: RefiParser.LowerContext):
    
       self.emit("\\\\p{Lower}")
    

