# Generated from RefiParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RefiParser import RefiParser
else:
    from RefiParser import RefiParser

# This class defines a complete listener for a parse tree produced by RefiParser.
class RefiParserListener(ParseTreeListener):

    # Enter a parse tree produced by RefiParser#expression.
    def enterExpression(self, ctx:RefiParser.ExpressionContext):
        pass

    # Exit a parse tree produced by RefiParser#expression.
    def exitExpression(self, ctx:RefiParser.ExpressionContext):
        pass


    # Enter a parse tree produced by RefiParser#backeted_matcher.
    def enterBacketed_matcher(self, ctx:RefiParser.Backeted_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#backeted_matcher.
    def exitBacketed_matcher(self, ctx:RefiParser.Backeted_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#matcher.
    def enterMatcher(self, ctx:RefiParser.MatcherContext):
        pass

    # Exit a parse tree produced by RefiParser#matcher.
    def exitMatcher(self, ctx:RefiParser.MatcherContext):
        pass


    # Enter a parse tree produced by RefiParser#literal_matcher.
    def enterLiteral_matcher(self, ctx:RefiParser.Literal_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#literal_matcher.
    def exitLiteral_matcher(self, ctx:RefiParser.Literal_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#atleast.
    def enterAtleast(self, ctx:RefiParser.AtleastContext):
        pass

    # Exit a parse tree produced by RefiParser#atleast.
    def exitAtleast(self, ctx:RefiParser.AtleastContext):
        pass


    # Enter a parse tree produced by RefiParser#between.
    def enterBetween(self, ctx:RefiParser.BetweenContext):
        pass

    # Exit a parse tree produced by RefiParser#between.
    def exitBetween(self, ctx:RefiParser.BetweenContext):
        pass


    # Enter a parse tree produced by RefiParser#capture_matcher.
    def enterCapture_matcher(self, ctx:RefiParser.Capture_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#capture_matcher.
    def exitCapture_matcher(self, ctx:RefiParser.Capture_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#caseins.
    def enterCaseins(self, ctx:RefiParser.CaseinsContext):
        pass

    # Exit a parse tree produced by RefiParser#caseins.
    def exitCaseins(self, ctx:RefiParser.CaseinsContext):
        pass


    # Enter a parse tree produced by RefiParser#caseinsoff.
    def enterCaseinsoff(self, ctx:RefiParser.CaseinsoffContext):
        pass

    # Exit a parse tree produced by RefiParser#caseinsoff.
    def exitCaseinsoff(self, ctx:RefiParser.CaseinsoffContext):
        pass


    # Enter a parse tree produced by RefiParser#char.
    def enterChar(self, ctx:RefiParser.CharContext):
        pass

    # Exit a parse tree produced by RefiParser#char.
    def exitChar(self, ctx:RefiParser.CharContext):
        pass


    # Enter a parse tree produced by RefiParser#ctrl_matcher.
    def enterCtrl_matcher(self, ctx:RefiParser.Ctrl_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#ctrl_matcher.
    def exitCtrl_matcher(self, ctx:RefiParser.Ctrl_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#either_matcher.
    def enterEither_matcher(self, ctx:RefiParser.Either_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#either_matcher.
    def exitEither_matcher(self, ctx:RefiParser.Either_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#expr_param_matcher.
    def enterExpr_param_matcher(self, ctx:RefiParser.Expr_param_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#expr_param_matcher.
    def exitExpr_param_matcher(self, ctx:RefiParser.Expr_param_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#exactly.
    def enterExactly(self, ctx:RefiParser.ExactlyContext):
        pass

    # Exit a parse tree produced by RefiParser#exactly.
    def exitExactly(self, ctx:RefiParser.ExactlyContext):
        pass


    # Enter a parse tree produced by RefiParser#flagged.
    def enterFlagged(self, ctx:RefiParser.FlaggedContext):
        pass

    # Exit a parse tree produced by RefiParser#flagged.
    def exitFlagged(self, ctx:RefiParser.FlaggedContext):
        pass


    # Enter a parse tree produced by RefiParser#flags.
    def enterFlags(self, ctx:RefiParser.FlagsContext):
        pass

    # Exit a parse tree produced by RefiParser#flags.
    def exitFlags(self, ctx:RefiParser.FlagsContext):
        pass


    # Enter a parse tree produced by RefiParser#greek.
    def enterGreek(self, ctx:RefiParser.GreekContext):
        pass

    # Exit a parse tree produced by RefiParser#greek.
    def exitGreek(self, ctx:RefiParser.GreekContext):
        pass


    # Enter a parse tree produced by RefiParser#hex_matcher.
    def enterHex_matcher(self, ctx:RefiParser.Hex_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#hex_matcher.
    def exitHex_matcher(self, ctx:RefiParser.Hex_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#nondigit.
    def enterNondigit(self, ctx:RefiParser.NondigitContext):
        pass

    # Exit a parse tree produced by RefiParser#nondigit.
    def exitNondigit(self, ctx:RefiParser.NondigitContext):
        pass


    # Enter a parse tree produced by RefiParser#not_matcher.
    def enterNot_matcher(self, ctx:RefiParser.Not_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#not_matcher.
    def exitNot_matcher(self, ctx:RefiParser.Not_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#octal_matcher.
    def enterOctal_matcher(self, ctx:RefiParser.Octal_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#octal_matcher.
    def exitOctal_matcher(self, ctx:RefiParser.Octal_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#or_matcher.
    def enterOr_matcher(self, ctx:RefiParser.Or_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#or_matcher.
    def exitOr_matcher(self, ctx:RefiParser.Or_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#range_matcher.
    def enterRange_matcher(self, ctx:RefiParser.Range_matcherContext):
        pass

    # Exit a parse tree produced by RefiParser#range_matcher.
    def exitRange_matcher(self, ctx:RefiParser.Range_matcherContext):
        pass


    # Enter a parse tree produced by RefiParser#union.
    def enterUnion(self, ctx:RefiParser.UnionContext):
        pass

    # Exit a parse tree produced by RefiParser#union.
    def exitUnion(self, ctx:RefiParser.UnionContext):
        pass


    # Enter a parse tree produced by RefiParser#string.
    def enterString(self, ctx:RefiParser.StringContext):
        pass

    # Exit a parse tree produced by RefiParser#string.
    def exitString(self, ctx:RefiParser.StringContext):
        pass


    # Enter a parse tree produced by RefiParser#matcher_name.
    def enterMatcher_name(self, ctx:RefiParser.Matcher_nameContext):
        pass

    # Exit a parse tree produced by RefiParser#matcher_name.
    def exitMatcher_name(self, ctx:RefiParser.Matcher_nameContext):
        pass


    # Enter a parse tree produced by RefiParser#match_type.
    def enterMatch_type(self, ctx:RefiParser.Match_typeContext):
        pass

    # Exit a parse tree produced by RefiParser#match_type.
    def exitMatch_type(self, ctx:RefiParser.Match_typeContext):
        pass


    # Enter a parse tree produced by RefiParser#alphabetic.
    def enterAlphabetic(self, ctx:RefiParser.AlphabeticContext):
        pass

    # Exit a parse tree produced by RefiParser#alphabetic.
    def exitAlphabetic(self, ctx:RefiParser.AlphabeticContext):
        pass


    # Enter a parse tree produced by RefiParser#anywild.
    def enterAnywild(self, ctx:RefiParser.AnywildContext):
        pass

    # Exit a parse tree produced by RefiParser#anywild.
    def exitAnywild(self, ctx:RefiParser.AnywildContext):
        pass


    # Enter a parse tree produced by RefiParser#backtick.
    def enterBacktick(self, ctx:RefiParser.BacktickContext):
        pass

    # Exit a parse tree produced by RefiParser#backtick.
    def exitBacktick(self, ctx:RefiParser.BacktickContext):
        pass


    # Enter a parse tree produced by RefiParser#bell.
    def enterBell(self, ctx:RefiParser.BellContext):
        pass

    # Exit a parse tree produced by RefiParser#bell.
    def exitBell(self, ctx:RefiParser.BellContext):
        pass


    # Enter a parse tree produced by RefiParser#bol.
    def enterBol(self, ctx:RefiParser.BolContext):
        pass

    # Exit a parse tree produced by RefiParser#bol.
    def exitBol(self, ctx:RefiParser.BolContext):
        pass


    # Enter a parse tree produced by RefiParser#currency.
    def enterCurrency(self, ctx:RefiParser.CurrencyContext):
        pass

    # Exit a parse tree produced by RefiParser#currency.
    def exitCurrency(self, ctx:RefiParser.CurrencyContext):
        pass


    # Enter a parse tree produced by RefiParser#digit.
    def enterDigit(self, ctx:RefiParser.DigitContext):
        pass

    # Exit a parse tree produced by RefiParser#digit.
    def exitDigit(self, ctx:RefiParser.DigitContext):
        pass


    # Enter a parse tree produced by RefiParser#escape.
    def enterEscape(self, ctx:RefiParser.EscapeContext):
        pass

    # Exit a parse tree produced by RefiParser#escape.
    def exitEscape(self, ctx:RefiParser.EscapeContext):
        pass


    # Enter a parse tree produced by RefiParser#eol.
    def enterEol(self, ctx:RefiParser.EolContext):
        pass

    # Exit a parse tree produced by RefiParser#eol.
    def exitEol(self, ctx:RefiParser.EolContext):
        pass


    # Enter a parse tree produced by RefiParser#flagname.
    def enterFlagname(self, ctx:RefiParser.FlagnameContext):
        pass

    # Exit a parse tree produced by RefiParser#flagname.
    def exitFlagname(self, ctx:RefiParser.FlagnameContext):
        pass


    # Enter a parse tree produced by RefiParser#formfeed.
    def enterFormfeed(self, ctx:RefiParser.FormfeedContext):
        pass

    # Exit a parse tree produced by RefiParser#formfeed.
    def exitFormfeed(self, ctx:RefiParser.FormfeedContext):
        pass


    # Enter a parse tree produced by RefiParser#latin.
    def enterLatin(self, ctx:RefiParser.LatinContext):
        pass

    # Exit a parse tree produced by RefiParser#latin.
    def exitLatin(self, ctx:RefiParser.LatinContext):
        pass


    # Enter a parse tree produced by RefiParser#lower.
    def enterLower(self, ctx:RefiParser.LowerContext):
        pass

    # Exit a parse tree produced by RefiParser#lower.
    def exitLower(self, ctx:RefiParser.LowerContext):
        pass


    # Enter a parse tree produced by RefiParser#newline.
    def enterNewline(self, ctx:RefiParser.NewlineContext):
        pass

    # Exit a parse tree produced by RefiParser#newline.
    def exitNewline(self, ctx:RefiParser.NewlineContext):
        pass


    # Enter a parse tree produced by RefiParser#return.
    def enterReturn(self, ctx:RefiParser.ReturnContext):
        pass

    # Exit a parse tree produced by RefiParser#return.
    def exitReturn(self, ctx:RefiParser.ReturnContext):
        pass


    # Enter a parse tree produced by RefiParser#somespace.
    def enterSomespace(self, ctx:RefiParser.SomespaceContext):
        pass

    # Exit a parse tree produced by RefiParser#somespace.
    def exitSomespace(self, ctx:RefiParser.SomespaceContext):
        pass


    # Enter a parse tree produced by RefiParser#tab.
    def enterTab(self, ctx:RefiParser.TabContext):
        pass

    # Exit a parse tree produced by RefiParser#tab.
    def exitTab(self, ctx:RefiParser.TabContext):
        pass


    # Enter a parse tree produced by RefiParser#unicodecase.
    def enterUnicodecase(self, ctx:RefiParser.UnicodecaseContext):
        pass

    # Exit a parse tree produced by RefiParser#unicodecase.
    def exitUnicodecase(self, ctx:RefiParser.UnicodecaseContext):
        pass


    # Enter a parse tree produced by RefiParser#unicodecaseoff.
    def enterUnicodecaseoff(self, ctx:RefiParser.UnicodecaseoffContext):
        pass

    # Exit a parse tree produced by RefiParser#unicodecaseoff.
    def exitUnicodecaseoff(self, ctx:RefiParser.UnicodecaseoffContext):
        pass


    # Enter a parse tree produced by RefiParser#unixlines.
    def enterUnixlines(self, ctx:RefiParser.UnixlinesContext):
        pass

    # Exit a parse tree produced by RefiParser#unixlines.
    def exitUnixlines(self, ctx:RefiParser.UnixlinesContext):
        pass


    # Enter a parse tree produced by RefiParser#unixlinesoff.
    def enterUnixlinesoff(self, ctx:RefiParser.UnixlinesoffContext):
        pass

    # Exit a parse tree produced by RefiParser#unixlinesoff.
    def exitUnixlinesoff(self, ctx:RefiParser.UnixlinesoffContext):
        pass


    # Enter a parse tree produced by RefiParser#upper.
    def enterUpper(self, ctx:RefiParser.UpperContext):
        pass

    # Exit a parse tree produced by RefiParser#upper.
    def exitUpper(self, ctx:RefiParser.UpperContext):
        pass


    # Enter a parse tree produced by RefiParser#wild.
    def enterWild(self, ctx:RefiParser.WildContext):
        pass

    # Exit a parse tree produced by RefiParser#wild.
    def exitWild(self, ctx:RefiParser.WildContext):
        pass


    # Enter a parse tree produced by RefiParser#wordboundary.
    def enterWordboundary(self, ctx:RefiParser.WordboundaryContext):
        pass

    # Exit a parse tree produced by RefiParser#wordboundary.
    def exitWordboundary(self, ctx:RefiParser.WordboundaryContext):
        pass



del RefiParser