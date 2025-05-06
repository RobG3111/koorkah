// Generated from KoorkahParser.g4 by ANTLR 4.13.1
package koorkah;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link KoorkahParser}.
 */
public interface KoorkahParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(KoorkahParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(KoorkahParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#backeted_matcher}.
	 * @param ctx the parse tree
	 */
	void enterBacketed_matcher(KoorkahParser.Backeted_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#backeted_matcher}.
	 * @param ctx the parse tree
	 */
	void exitBacketed_matcher(KoorkahParser.Backeted_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#matcher}.
	 * @param ctx the parse tree
	 */
	void enterMatcher(KoorkahParser.MatcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#matcher}.
	 * @param ctx the parse tree
	 */
	void exitMatcher(KoorkahParser.MatcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#literal_matcher}.
	 * @param ctx the parse tree
	 */
	void enterLiteral_matcher(KoorkahParser.Literal_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#literal_matcher}.
	 * @param ctx the parse tree
	 */
	void exitLiteral_matcher(KoorkahParser.Literal_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#atleast}.
	 * @param ctx the parse tree
	 */
	void enterAtleast(KoorkahParser.AtleastContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#atleast}.
	 * @param ctx the parse tree
	 */
	void exitAtleast(KoorkahParser.AtleastContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#between}.
	 * @param ctx the parse tree
	 */
	void enterBetween(KoorkahParser.BetweenContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#between}.
	 * @param ctx the parse tree
	 */
	void exitBetween(KoorkahParser.BetweenContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#capture_matcher}.
	 * @param ctx the parse tree
	 */
	void enterCapture_matcher(KoorkahParser.Capture_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#capture_matcher}.
	 * @param ctx the parse tree
	 */
	void exitCapture_matcher(KoorkahParser.Capture_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#caseins}.
	 * @param ctx the parse tree
	 */
	void enterCaseins(KoorkahParser.CaseinsContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#caseins}.
	 * @param ctx the parse tree
	 */
	void exitCaseins(KoorkahParser.CaseinsContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#caseinsoff}.
	 * @param ctx the parse tree
	 */
	void enterCaseinsoff(KoorkahParser.CaseinsoffContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#caseinsoff}.
	 * @param ctx the parse tree
	 */
	void exitCaseinsoff(KoorkahParser.CaseinsoffContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#char}.
	 * @param ctx the parse tree
	 */
	void enterChar(KoorkahParser.CharContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#char}.
	 * @param ctx the parse tree
	 */
	void exitChar(KoorkahParser.CharContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#ctrl_matcher}.
	 * @param ctx the parse tree
	 */
	void enterCtrl_matcher(KoorkahParser.Ctrl_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#ctrl_matcher}.
	 * @param ctx the parse tree
	 */
	void exitCtrl_matcher(KoorkahParser.Ctrl_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#either_matcher}.
	 * @param ctx the parse tree
	 */
	void enterEither_matcher(KoorkahParser.Either_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#either_matcher}.
	 * @param ctx the parse tree
	 */
	void exitEither_matcher(KoorkahParser.Either_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#expr_param_matcher}.
	 * @param ctx the parse tree
	 */
	void enterExpr_param_matcher(KoorkahParser.Expr_param_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#expr_param_matcher}.
	 * @param ctx the parse tree
	 */
	void exitExpr_param_matcher(KoorkahParser.Expr_param_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#exactly}.
	 * @param ctx the parse tree
	 */
	void enterExactly(KoorkahParser.ExactlyContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#exactly}.
	 * @param ctx the parse tree
	 */
	void exitExactly(KoorkahParser.ExactlyContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#flagged}.
	 * @param ctx the parse tree
	 */
	void enterFlagged(KoorkahParser.FlaggedContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#flagged}.
	 * @param ctx the parse tree
	 */
	void exitFlagged(KoorkahParser.FlaggedContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#flags}.
	 * @param ctx the parse tree
	 */
	void enterFlags(KoorkahParser.FlagsContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#flags}.
	 * @param ctx the parse tree
	 */
	void exitFlags(KoorkahParser.FlagsContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#greek}.
	 * @param ctx the parse tree
	 */
	void enterGreek(KoorkahParser.GreekContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#greek}.
	 * @param ctx the parse tree
	 */
	void exitGreek(KoorkahParser.GreekContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#hex_matcher}.
	 * @param ctx the parse tree
	 */
	void enterHex_matcher(KoorkahParser.Hex_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#hex_matcher}.
	 * @param ctx the parse tree
	 */
	void exitHex_matcher(KoorkahParser.Hex_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#nondigit}.
	 * @param ctx the parse tree
	 */
	void enterNondigit(KoorkahParser.NondigitContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#nondigit}.
	 * @param ctx the parse tree
	 */
	void exitNondigit(KoorkahParser.NondigitContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#not_matcher}.
	 * @param ctx the parse tree
	 */
	void enterNot_matcher(KoorkahParser.Not_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#not_matcher}.
	 * @param ctx the parse tree
	 */
	void exitNot_matcher(KoorkahParser.Not_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#octal_matcher}.
	 * @param ctx the parse tree
	 */
	void enterOctal_matcher(KoorkahParser.Octal_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#octal_matcher}.
	 * @param ctx the parse tree
	 */
	void exitOctal_matcher(KoorkahParser.Octal_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#or_matcher}.
	 * @param ctx the parse tree
	 */
	void enterOr_matcher(KoorkahParser.Or_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#or_matcher}.
	 * @param ctx the parse tree
	 */
	void exitOr_matcher(KoorkahParser.Or_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#range_matcher}.
	 * @param ctx the parse tree
	 */
	void enterRange_matcher(KoorkahParser.Range_matcherContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#range_matcher}.
	 * @param ctx the parse tree
	 */
	void exitRange_matcher(KoorkahParser.Range_matcherContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#union}.
	 * @param ctx the parse tree
	 */
	void enterUnion(KoorkahParser.UnionContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#union}.
	 * @param ctx the parse tree
	 */
	void exitUnion(KoorkahParser.UnionContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(KoorkahParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(KoorkahParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#matcher_name}.
	 * @param ctx the parse tree
	 */
	void enterMatcher_name(KoorkahParser.Matcher_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#matcher_name}.
	 * @param ctx the parse tree
	 */
	void exitMatcher_name(KoorkahParser.Matcher_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#match_type}.
	 * @param ctx the parse tree
	 */
	void enterMatch_type(KoorkahParser.Match_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#match_type}.
	 * @param ctx the parse tree
	 */
	void exitMatch_type(KoorkahParser.Match_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#alphabetic}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetic(KoorkahParser.AlphabeticContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#alphabetic}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetic(KoorkahParser.AlphabeticContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#anywild}.
	 * @param ctx the parse tree
	 */
	void enterAnywild(KoorkahParser.AnywildContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#anywild}.
	 * @param ctx the parse tree
	 */
	void exitAnywild(KoorkahParser.AnywildContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#backtick}.
	 * @param ctx the parse tree
	 */
	void enterBacktick(KoorkahParser.BacktickContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#backtick}.
	 * @param ctx the parse tree
	 */
	void exitBacktick(KoorkahParser.BacktickContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#bell}.
	 * @param ctx the parse tree
	 */
	void enterBell(KoorkahParser.BellContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#bell}.
	 * @param ctx the parse tree
	 */
	void exitBell(KoorkahParser.BellContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#bol}.
	 * @param ctx the parse tree
	 */
	void enterBol(KoorkahParser.BolContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#bol}.
	 * @param ctx the parse tree
	 */
	void exitBol(KoorkahParser.BolContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#currency}.
	 * @param ctx the parse tree
	 */
	void enterCurrency(KoorkahParser.CurrencyContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#currency}.
	 * @param ctx the parse tree
	 */
	void exitCurrency(KoorkahParser.CurrencyContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#digit}.
	 * @param ctx the parse tree
	 */
	void enterDigit(KoorkahParser.DigitContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#digit}.
	 * @param ctx the parse tree
	 */
	void exitDigit(KoorkahParser.DigitContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#escape}.
	 * @param ctx the parse tree
	 */
	void enterEscape(KoorkahParser.EscapeContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#escape}.
	 * @param ctx the parse tree
	 */
	void exitEscape(KoorkahParser.EscapeContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#eol}.
	 * @param ctx the parse tree
	 */
	void enterEol(KoorkahParser.EolContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#eol}.
	 * @param ctx the parse tree
	 */
	void exitEol(KoorkahParser.EolContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#flagname}.
	 * @param ctx the parse tree
	 */
	void enterFlagname(KoorkahParser.FlagnameContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#flagname}.
	 * @param ctx the parse tree
	 */
	void exitFlagname(KoorkahParser.FlagnameContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#formfeed}.
	 * @param ctx the parse tree
	 */
	void enterFormfeed(KoorkahParser.FormfeedContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#formfeed}.
	 * @param ctx the parse tree
	 */
	void exitFormfeed(KoorkahParser.FormfeedContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#latin}.
	 * @param ctx the parse tree
	 */
	void enterLatin(KoorkahParser.LatinContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#latin}.
	 * @param ctx the parse tree
	 */
	void exitLatin(KoorkahParser.LatinContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#lower}.
	 * @param ctx the parse tree
	 */
	void enterLower(KoorkahParser.LowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#lower}.
	 * @param ctx the parse tree
	 */
	void exitLower(KoorkahParser.LowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#newline}.
	 * @param ctx the parse tree
	 */
	void enterNewline(KoorkahParser.NewlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#newline}.
	 * @param ctx the parse tree
	 */
	void exitNewline(KoorkahParser.NewlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#return}.
	 * @param ctx the parse tree
	 */
	void enterReturn(KoorkahParser.ReturnContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#return}.
	 * @param ctx the parse tree
	 */
	void exitReturn(KoorkahParser.ReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#somespace}.
	 * @param ctx the parse tree
	 */
	void enterSomespace(KoorkahParser.SomespaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#somespace}.
	 * @param ctx the parse tree
	 */
	void exitSomespace(KoorkahParser.SomespaceContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#tab}.
	 * @param ctx the parse tree
	 */
	void enterTab(KoorkahParser.TabContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#tab}.
	 * @param ctx the parse tree
	 */
	void exitTab(KoorkahParser.TabContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#unicodecase}.
	 * @param ctx the parse tree
	 */
	void enterUnicodecase(KoorkahParser.UnicodecaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#unicodecase}.
	 * @param ctx the parse tree
	 */
	void exitUnicodecase(KoorkahParser.UnicodecaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#unicodecaseoff}.
	 * @param ctx the parse tree
	 */
	void enterUnicodecaseoff(KoorkahParser.UnicodecaseoffContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#unicodecaseoff}.
	 * @param ctx the parse tree
	 */
	void exitUnicodecaseoff(KoorkahParser.UnicodecaseoffContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#unixlines}.
	 * @param ctx the parse tree
	 */
	void enterUnixlines(KoorkahParser.UnixlinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#unixlines}.
	 * @param ctx the parse tree
	 */
	void exitUnixlines(KoorkahParser.UnixlinesContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#unixlinesoff}.
	 * @param ctx the parse tree
	 */
	void enterUnixlinesoff(KoorkahParser.UnixlinesoffContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#unixlinesoff}.
	 * @param ctx the parse tree
	 */
	void exitUnixlinesoff(KoorkahParser.UnixlinesoffContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#upper}.
	 * @param ctx the parse tree
	 */
	void enterUpper(KoorkahParser.UpperContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#upper}.
	 * @param ctx the parse tree
	 */
	void exitUpper(KoorkahParser.UpperContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#wild}.
	 * @param ctx the parse tree
	 */
	void enterWild(KoorkahParser.WildContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#wild}.
	 * @param ctx the parse tree
	 */
	void exitWild(KoorkahParser.WildContext ctx);
	/**
	 * Enter a parse tree produced by {@link KoorkahParser#wordboundary}.
	 * @param ctx the parse tree
	 */
	void enterWordboundary(KoorkahParser.WordboundaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link KoorkahParser#wordboundary}.
	 * @param ctx the parse tree
	 */
	void exitWordboundary(KoorkahParser.WordboundaryContext ctx);
}