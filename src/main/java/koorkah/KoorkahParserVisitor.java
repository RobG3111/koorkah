// Generated from C:/Users/robg3/workspace/refi/src/refi/KoorkahParser.g4 by ANTLR 4.13.1

package koorkah;

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link KoorkahParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface KoorkahParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(KoorkahParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#backeted_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBacketed_matcher(KoorkahParser.Backeted_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMatcher(KoorkahParser.MatcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#literal_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral_matcher(KoorkahParser.Literal_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#atleast}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtleast(KoorkahParser.AtleastContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#between}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBetween(KoorkahParser.BetweenContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#capture_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCapture_matcher(KoorkahParser.Capture_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#caseins}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseins(KoorkahParser.CaseinsContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#caseinsoff}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseinsoff(KoorkahParser.CaseinsoffContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#char}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChar(KoorkahParser.CharContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#ctrl_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCtrl_matcher(KoorkahParser.Ctrl_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#either_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEither_matcher(KoorkahParser.Either_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#expr_param_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr_param_matcher(KoorkahParser.Expr_param_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#exactly}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExactly(KoorkahParser.ExactlyContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#flagged}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlagged(KoorkahParser.FlaggedContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#flags}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlags(KoorkahParser.FlagsContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#greek}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGreek(KoorkahParser.GreekContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#hex_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHex_matcher(KoorkahParser.Hex_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#nondigit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNondigit(KoorkahParser.NondigitContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#not_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNot_matcher(KoorkahParser.Not_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#octal_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOctal_matcher(KoorkahParser.Octal_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#or_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr_matcher(KoorkahParser.Or_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#range_matcher}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRange_matcher(KoorkahParser.Range_matcherContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#union}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnion(KoorkahParser.UnionContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#string}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(KoorkahParser.StringContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#matcher_name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMatcher_name(KoorkahParser.Matcher_nameContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#match_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMatch_type(KoorkahParser.Match_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#alphabetic}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlphabetic(KoorkahParser.AlphabeticContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#anywild}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnywild(KoorkahParser.AnywildContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#backtick}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBacktick(KoorkahParser.BacktickContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#bell}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBell(KoorkahParser.BellContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#bol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBol(KoorkahParser.BolContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#currency}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCurrency(KoorkahParser.CurrencyContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#digit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDigit(KoorkahParser.DigitContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#escape}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEscape(KoorkahParser.EscapeContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#eol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEol(KoorkahParser.EolContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#flagname}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlagname(KoorkahParser.FlagnameContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#formfeed}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormfeed(KoorkahParser.FormfeedContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#latin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLatin(KoorkahParser.LatinContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#lower}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLower(KoorkahParser.LowerContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#newline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNewline(KoorkahParser.NewlineContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#return}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn(KoorkahParser.ReturnContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#somespace}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSomespace(KoorkahParser.SomespaceContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#tab}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTab(KoorkahParser.TabContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#unicodecase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnicodecase(KoorkahParser.UnicodecaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#unicodecaseoff}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnicodecaseoff(KoorkahParser.UnicodecaseoffContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#unixlines}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnixlines(KoorkahParser.UnixlinesContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#unixlinesoff}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnixlinesoff(KoorkahParser.UnixlinesoffContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#upper}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUpper(KoorkahParser.UpperContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#wild}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWild(KoorkahParser.WildContext ctx);
	/**
	 * Visit a parse tree produced by {@link KoorkahParser#wordboundary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWordboundary(KoorkahParser.WordboundaryContext ctx);
}