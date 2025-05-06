# Generated from RefiParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,400,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,4,0,104,8,0,11,
        0,12,0,105,1,0,1,0,1,1,1,1,4,1,112,8,1,11,1,12,1,113,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,163,8,2,1,3,
        1,3,1,3,3,3,168,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,176,8,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,188,8,5,1,5,1,5,1,6,1,6,1,6,
        1,6,4,6,196,8,6,11,6,12,6,197,1,6,1,6,3,6,202,8,6,1,6,1,6,1,7,1,
        7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,5,11,224,8,11,10,11,12,11,227,9,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,3,12,236,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,246,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,255,
        8,14,10,14,12,14,258,9,14,1,14,1,14,1,14,3,14,263,8,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,5,15,272,8,15,10,15,12,15,275,9,15,1,15,
        1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,295,8,19,10,19,12,19,298,9,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,4,21,310,8,21,11,21,12,21,
        311,1,21,1,21,4,21,316,8,21,11,21,12,21,317,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,331,8,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,25,
        1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,
        1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,
        1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,50,
        5,197,256,273,311,317,0,51,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,0,4,2,0,1,1,11,11,
        3,0,16,16,47,47,53,53,2,0,49,49,51,51,3,0,24,25,56,57,59,60,411,
        0,103,1,0,0,0,2,109,1,0,0,0,4,162,1,0,0,0,6,167,1,0,0,0,8,169,1,
        0,0,0,10,179,1,0,0,0,12,191,1,0,0,0,14,205,1,0,0,0,16,207,1,0,0,
        0,18,209,1,0,0,0,20,211,1,0,0,0,22,216,1,0,0,0,24,230,1,0,0,0,26,
        239,1,0,0,0,28,249,1,0,0,0,30,266,1,0,0,0,32,278,1,0,0,0,34,280,
        1,0,0,0,36,285,1,0,0,0,38,287,1,0,0,0,40,301,1,0,0,0,42,306,1,0,
        0,0,44,321,1,0,0,0,46,334,1,0,0,0,48,345,1,0,0,0,50,347,1,0,0,0,
        52,349,1,0,0,0,54,351,1,0,0,0,56,353,1,0,0,0,58,355,1,0,0,0,60,357,
        1,0,0,0,62,359,1,0,0,0,64,361,1,0,0,0,66,363,1,0,0,0,68,365,1,0,
        0,0,70,367,1,0,0,0,72,369,1,0,0,0,74,371,1,0,0,0,76,373,1,0,0,0,
        78,375,1,0,0,0,80,377,1,0,0,0,82,379,1,0,0,0,84,381,1,0,0,0,86,383,
        1,0,0,0,88,385,1,0,0,0,90,387,1,0,0,0,92,389,1,0,0,0,94,391,1,0,
        0,0,96,393,1,0,0,0,98,395,1,0,0,0,100,397,1,0,0,0,102,104,3,4,2,
        0,103,102,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,
        0,106,107,1,0,0,0,107,108,5,0,0,1,108,1,1,0,0,0,109,111,5,7,0,0,
        110,112,3,4,2,0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,
        113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,10,0,0,116,3,1,0,0,0,117,
        163,3,8,4,0,118,163,3,2,1,0,119,163,3,10,5,0,120,163,3,54,27,0,121,
        163,3,56,28,0,122,163,3,60,30,0,123,163,3,62,31,0,124,163,3,58,29,
        0,125,163,3,12,6,0,126,163,3,14,7,0,127,163,3,16,8,0,128,163,3,18,
        9,0,129,163,3,20,10,0,130,163,3,64,32,0,131,163,3,66,33,0,132,163,
        3,22,11,0,133,163,3,70,35,0,134,163,3,68,34,0,135,163,3,26,13,0,
        136,163,3,24,12,0,137,163,3,74,37,0,138,163,3,28,14,0,139,163,3,
        30,15,0,140,163,3,32,16,0,141,163,3,34,17,0,142,163,3,76,38,0,143,
        163,3,78,39,0,144,163,3,80,40,0,145,163,3,36,18,0,146,163,3,38,19,
        0,147,163,3,40,20,0,148,163,3,42,21,0,149,163,3,44,22,0,150,163,
        3,82,41,0,151,163,3,84,42,0,152,163,3,48,24,0,153,163,3,86,43,0,
        154,163,3,88,44,0,155,163,3,90,45,0,156,163,3,46,23,0,157,163,3,
        92,46,0,158,163,3,94,47,0,159,163,3,96,48,0,160,163,3,98,49,0,161,
        163,3,100,50,0,162,117,1,0,0,0,162,118,1,0,0,0,162,119,1,0,0,0,162,
        120,1,0,0,0,162,121,1,0,0,0,162,122,1,0,0,0,162,123,1,0,0,0,162,
        124,1,0,0,0,162,125,1,0,0,0,162,126,1,0,0,0,162,127,1,0,0,0,162,
        128,1,0,0,0,162,129,1,0,0,0,162,130,1,0,0,0,162,131,1,0,0,0,162,
        132,1,0,0,0,162,133,1,0,0,0,162,134,1,0,0,0,162,135,1,0,0,0,162,
        136,1,0,0,0,162,137,1,0,0,0,162,138,1,0,0,0,162,139,1,0,0,0,162,
        140,1,0,0,0,162,141,1,0,0,0,162,142,1,0,0,0,162,143,1,0,0,0,162,
        144,1,0,0,0,162,145,1,0,0,0,162,146,1,0,0,0,162,147,1,0,0,0,162,
        148,1,0,0,0,162,149,1,0,0,0,162,150,1,0,0,0,162,151,1,0,0,0,162,
        152,1,0,0,0,162,153,1,0,0,0,162,154,1,0,0,0,162,155,1,0,0,0,162,
        156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,162,159,1,0,0,0,162,
        160,1,0,0,0,162,161,1,0,0,0,163,5,1,0,0,0,164,168,3,58,29,0,165,
        168,3,2,1,0,166,168,3,98,49,0,167,164,1,0,0,0,167,165,1,0,0,0,167,
        166,1,0,0,0,168,7,1,0,0,0,169,170,5,15,0,0,170,171,5,6,0,0,171,172,
        5,5,0,0,172,175,5,3,0,0,173,176,3,4,2,0,174,176,3,2,1,0,175,173,
        1,0,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,178,5,9,0,0,178,9,1,
        0,0,0,179,180,5,21,0,0,180,181,5,6,0,0,181,182,5,5,0,0,182,183,5,
        3,0,0,183,184,5,5,0,0,184,187,5,3,0,0,185,188,3,4,2,0,186,188,3,
        2,1,0,187,185,1,0,0,0,187,186,1,0,0,0,188,189,1,0,0,0,189,190,5,
        9,0,0,190,11,1,0,0,0,191,192,5,23,0,0,192,195,5,6,0,0,193,196,3,
        4,2,0,194,196,3,2,1,0,195,193,1,0,0,0,195,194,1,0,0,0,196,197,1,
        0,0,0,197,198,1,0,0,0,197,195,1,0,0,0,198,201,1,0,0,0,199,200,5,
        3,0,0,200,202,7,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,203,1,
        0,0,0,203,204,5,9,0,0,204,13,1,0,0,0,205,206,5,24,0,0,206,15,1,0,
        0,0,207,208,5,25,0,0,208,17,1,0,0,0,209,210,5,1,0,0,210,19,1,0,0,
        0,211,212,5,27,0,0,212,213,5,6,0,0,213,214,5,5,0,0,214,215,5,9,0,
        0,215,21,1,0,0,0,216,217,5,31,0,0,217,218,5,6,0,0,218,219,5,1,0,
        0,219,220,5,3,0,0,220,225,5,1,0,0,221,222,5,3,0,0,222,224,5,1,0,
        0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,
        0,226,228,1,0,0,0,227,225,1,0,0,0,228,229,5,9,0,0,229,23,1,0,0,0,
        230,231,3,50,25,0,231,232,5,6,0,0,232,235,3,4,2,0,233,234,5,3,0,
        0,234,236,3,52,26,0,235,233,1,0,0,0,235,236,1,0,0,0,236,237,1,0,
        0,0,237,238,5,9,0,0,238,25,1,0,0,0,239,240,5,34,0,0,240,241,5,6,
        0,0,241,242,5,5,0,0,242,245,5,3,0,0,243,246,3,4,2,0,244,246,3,2,
        1,0,245,243,1,0,0,0,245,244,1,0,0,0,246,247,1,0,0,0,247,248,5,9,
        0,0,248,27,1,0,0,0,249,250,5,35,0,0,250,251,5,6,0,0,251,256,3,72,
        36,0,252,253,5,3,0,0,253,255,3,72,36,0,254,252,1,0,0,0,255,258,1,
        0,0,0,256,257,1,0,0,0,256,254,1,0,0,0,257,259,1,0,0,0,258,256,1,
        0,0,0,259,262,5,3,0,0,260,263,3,4,2,0,261,263,3,2,1,0,262,260,1,
        0,0,0,262,261,1,0,0,0,263,264,1,0,0,0,264,265,5,9,0,0,265,29,1,0,
        0,0,266,267,5,36,0,0,267,268,5,6,0,0,268,273,3,72,36,0,269,270,5,
        3,0,0,270,272,3,72,36,0,271,269,1,0,0,0,272,275,1,0,0,0,273,274,
        1,0,0,0,273,271,1,0,0,0,274,276,1,0,0,0,275,273,1,0,0,0,276,277,
        5,9,0,0,277,31,1,0,0,0,278,279,5,38,0,0,279,33,1,0,0,0,280,281,5,
        39,0,0,281,282,5,6,0,0,282,283,5,4,0,0,283,284,5,9,0,0,284,35,1,
        0,0,0,285,286,5,44,0,0,286,37,1,0,0,0,287,288,5,45,0,0,288,289,5,
        6,0,0,289,290,5,1,0,0,290,291,5,3,0,0,291,296,5,1,0,0,292,293,5,
        3,0,0,293,295,5,1,0,0,294,292,1,0,0,0,295,298,1,0,0,0,296,294,1,
        0,0,0,296,297,1,0,0,0,297,299,1,0,0,0,298,296,1,0,0,0,299,300,5,
        9,0,0,300,39,1,0,0,0,301,302,5,46,0,0,302,303,5,6,0,0,303,304,5,
        8,0,0,304,305,5,9,0,0,305,41,1,0,0,0,306,307,5,48,0,0,307,309,5,
        6,0,0,308,310,3,4,2,0,309,308,1,0,0,0,310,311,1,0,0,0,311,312,1,
        0,0,0,311,309,1,0,0,0,312,313,1,0,0,0,313,315,5,12,0,0,314,316,3,
        4,2,0,315,314,1,0,0,0,316,317,1,0,0,0,317,318,1,0,0,0,317,315,1,
        0,0,0,318,319,1,0,0,0,319,320,5,9,0,0,320,43,1,0,0,0,321,322,5,50,
        0,0,322,323,5,6,0,0,323,324,5,1,0,0,324,325,5,2,0,0,325,330,5,1,
        0,0,326,327,5,3,0,0,327,328,5,1,0,0,328,329,5,2,0,0,329,331,5,1,
        0,0,330,326,1,0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,332,333,5,9,
        0,0,333,45,1,0,0,0,334,335,5,58,0,0,335,336,5,6,0,0,336,337,5,1,
        0,0,337,338,5,2,0,0,338,339,5,1,0,0,339,340,5,3,0,0,340,341,5,1,
        0,0,341,342,5,2,0,0,342,343,5,1,0,0,343,344,5,9,0,0,344,47,1,0,0,
        0,345,346,5,11,0,0,346,49,1,0,0,0,347,348,7,1,0,0,348,51,1,0,0,0,
        349,350,7,2,0,0,350,53,1,0,0,0,351,352,5,14,0,0,352,55,1,0,0,0,353,
        354,5,17,0,0,354,57,1,0,0,0,355,356,5,19,0,0,356,59,1,0,0,0,357,
        358,5,20,0,0,358,61,1,0,0,0,359,360,5,22,0,0,360,63,1,0,0,0,361,
        362,5,28,0,0,362,65,1,0,0,0,363,364,5,29,0,0,364,67,1,0,0,0,365,
        366,5,32,0,0,366,69,1,0,0,0,367,368,5,33,0,0,368,71,1,0,0,0,369,
        370,7,3,0,0,370,73,1,0,0,0,371,372,5,37,0,0,372,75,1,0,0,0,373,374,
        5,40,0,0,374,77,1,0,0,0,375,376,5,41,0,0,376,79,1,0,0,0,377,378,
        5,43,0,0,378,81,1,0,0,0,379,380,5,52,0,0,380,83,1,0,0,0,381,382,
        5,54,0,0,382,85,1,0,0,0,383,384,5,55,0,0,384,87,1,0,0,0,385,386,
        5,56,0,0,386,89,1,0,0,0,387,388,5,57,0,0,388,91,1,0,0,0,389,390,
        5,59,0,0,390,93,1,0,0,0,391,392,5,60,0,0,392,95,1,0,0,0,393,394,
        5,61,0,0,394,97,1,0,0,0,395,396,5,62,0,0,396,99,1,0,0,0,397,398,
        5,63,0,0,398,101,1,0,0,0,19,105,113,162,167,175,187,195,197,201,
        225,235,245,256,262,273,296,311,317,330
    ]

class RefiParser ( Parser ):

    grammarFileName = "RefiParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "':'", "','", "<INVALID>", 
                     "<INVALID>", "'{'", "'('", "<INVALID>", "'}'", "')'", 
                     "<INVALID>", "'|'", "<INVALID>", "'alphabetic'", "'atleast'", 
                     "'any'", "'anywild'", "'ascii'", "'backtick'", "'bell'", 
                     "'between'", "'bol'", "'capture'", "'caseins'", "'caseinsoff'", 
                     "'Comments'", "'ctrl'", "'currency'", "'digit'", "'DotAll'", 
                     "'either'", "'escape'", "'eol'", "'exactly'", "'flagged'", 
                     "'flags'", "'formfeed'", "'greek'", "'hex'", "'latin'", 
                     "'lower'", "'MultiLine'", "'newline'", "'nondigit'", 
                     "'not'", "'octal'", "'optional'", "'or'", "'posses'", 
                     "'range'", "'reluct'", "'return'", "'some'", "'somespace'", 
                     "'tab'", "'UnicodeCase'", "'UnicodeCaseOff'", "'union'", 
                     "'UnixLines'", "'UnixLinesOff'", "'upper'", "'wild'", 
                     "'wordboundary'", "'zz'" ]

    symbolicNames = [ "<INVALID>", "CHAR", "COLON", "COMMA", "HEX_NUMBER", 
                      "INT", "LEFTCURLY", "LEFTPAREN", "OCTAL_NUMBER", "RIGHTCURLY", 
                      "RIGHTPAREN", "STRING", "VERTICAL", "WS", "ALPHABETIC", 
                      "ATLEAST", "ANY", "ANYWILD", "ASCII", "BACKTICK", 
                      "BELL", "BETWEEN", "BOL", "CAPTURE", "CASEINS", "CASEINSOFF", 
                      "COMMENTS", "CTRL", "CURRENCY", "DIGIT", "DOTALL", 
                      "EITHER", "ESCAPE", "EOL", "EXACTLY", "FLAGGED", "FLAGS", 
                      "FORMFEED", "GREEK", "HEX", "LATIN", "LOWER", "MULTILINE", 
                      "NEWLINE", "NONDIGIT", "NOT", "OCTAL", "OPTIONAL", 
                      "OR", "POSSES", "RANGE", "RELUCT", "RETURN", "SOME", 
                      "SOMESPACE", "TAB", "UNICODECASE", "UNICODECASEOFF", 
                      "UNION", "UNIXLINES", "UNIXLINESOFF", "UPPER", "WILD", 
                      "WORDBOUNDARY", "ZZ" ]

    RULE_expression = 0
    RULE_backeted_matcher = 1
    RULE_matcher = 2
    RULE_literal_matcher = 3
    RULE_atleast = 4
    RULE_between = 5
    RULE_capture_matcher = 6
    RULE_caseins = 7
    RULE_caseinsoff = 8
    RULE_char = 9
    RULE_ctrl_matcher = 10
    RULE_either_matcher = 11
    RULE_expr_param_matcher = 12
    RULE_exactly = 13
    RULE_flagged = 14
    RULE_flags = 15
    RULE_greek = 16
    RULE_hex_matcher = 17
    RULE_nondigit = 18
    RULE_not_matcher = 19
    RULE_octal_matcher = 20
    RULE_or_matcher = 21
    RULE_range_matcher = 22
    RULE_union = 23
    RULE_string = 24
    RULE_matcher_name = 25
    RULE_match_type = 26
    RULE_alphabetic = 27
    RULE_anywild = 28
    RULE_backtick = 29
    RULE_bell = 30
    RULE_bol = 31
    RULE_currency = 32
    RULE_digit = 33
    RULE_escape = 34
    RULE_eol = 35
    RULE_flagname = 36
    RULE_formfeed = 37
    RULE_latin = 38
    RULE_lower = 39
    RULE_newline = 40
    RULE_return = 41
    RULE_somespace = 42
    RULE_tab = 43
    RULE_unicodecase = 44
    RULE_unicodecaseoff = 45
    RULE_unixlines = 46
    RULE_unixlinesoff = 47
    RULE_upper = 48
    RULE_wild = 49
    RULE_wordboundary = 50

    ruleNames =  [ "expression", "backeted_matcher", "matcher", "literal_matcher", 
                   "atleast", "between", "capture_matcher", "caseins", "caseinsoff", 
                   "char", "ctrl_matcher", "either_matcher", "expr_param_matcher", 
                   "exactly", "flagged", "flags", "greek", "hex_matcher", 
                   "nondigit", "not_matcher", "octal_matcher", "or_matcher", 
                   "range_matcher", "union", "string", "matcher_name", "match_type", 
                   "alphabetic", "anywild", "backtick", "bell", "bol", "currency", 
                   "digit", "escape", "eol", "flagname", "formfeed", "latin", 
                   "lower", "newline", "return", "somespace", "tab", "unicodecase", 
                   "unicodecaseoff", "unixlines", "unixlinesoff", "upper", 
                   "wild", "wordboundary" ]

    EOF = Token.EOF
    CHAR=1
    COLON=2
    COMMA=3
    HEX_NUMBER=4
    INT=5
    LEFTCURLY=6
    LEFTPAREN=7
    OCTAL_NUMBER=8
    RIGHTCURLY=9
    RIGHTPAREN=10
    STRING=11
    VERTICAL=12
    WS=13
    ALPHABETIC=14
    ATLEAST=15
    ANY=16
    ANYWILD=17
    ASCII=18
    BACKTICK=19
    BELL=20
    BETWEEN=21
    BOL=22
    CAPTURE=23
    CASEINS=24
    CASEINSOFF=25
    COMMENTS=26
    CTRL=27
    CURRENCY=28
    DIGIT=29
    DOTALL=30
    EITHER=31
    ESCAPE=32
    EOL=33
    EXACTLY=34
    FLAGGED=35
    FLAGS=36
    FORMFEED=37
    GREEK=38
    HEX=39
    LATIN=40
    LOWER=41
    MULTILINE=42
    NEWLINE=43
    NONDIGIT=44
    NOT=45
    OCTAL=46
    OPTIONAL=47
    OR=48
    POSSES=49
    RANGE=50
    RELUCT=51
    RETURN=52
    SOME=53
    SOMESPACE=54
    TAB=55
    UNICODECASE=56
    UNICODECASEOFF=57
    UNION=58
    UNIXLINES=59
    UNIXLINESOFF=60
    UPPER=61
    WILD=62
    WORDBOUNDARY=63
    ZZ=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RefiParser.EOF, 0)

        def matcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.MatcherContext)
            else:
                return self.getTypedRuleContext(RefiParser.MatcherContext,i)


        def getRuleIndex(self):
            return RefiParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = RefiParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.matcher()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -2819148954744702) != 0)):
                    break

            self.state = 107
            self.match(RefiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Backeted_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTPAREN(self):
            return self.getToken(RefiParser.LEFTPAREN, 0)

        def RIGHTPAREN(self):
            return self.getToken(RefiParser.RIGHTPAREN, 0)

        def matcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.MatcherContext)
            else:
                return self.getTypedRuleContext(RefiParser.MatcherContext,i)


        def getRuleIndex(self):
            return RefiParser.RULE_backeted_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBacketed_matcher" ):
                listener.enterBacketed_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBacketed_matcher" ):
                listener.exitBacketed_matcher(self)




    def backeted_matcher(self):

        localctx = RefiParser.Backeted_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_backeted_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(RefiParser.LEFTPAREN)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.matcher()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -2819148954744702) != 0)):
                    break

            self.state = 115
            self.match(RefiParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast(self):
            return self.getTypedRuleContext(RefiParser.AtleastContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def between(self):
            return self.getTypedRuleContext(RefiParser.BetweenContext,0)


        def alphabetic(self):
            return self.getTypedRuleContext(RefiParser.AlphabeticContext,0)


        def anywild(self):
            return self.getTypedRuleContext(RefiParser.AnywildContext,0)


        def bell(self):
            return self.getTypedRuleContext(RefiParser.BellContext,0)


        def bol(self):
            return self.getTypedRuleContext(RefiParser.BolContext,0)


        def backtick(self):
            return self.getTypedRuleContext(RefiParser.BacktickContext,0)


        def capture_matcher(self):
            return self.getTypedRuleContext(RefiParser.Capture_matcherContext,0)


        def caseins(self):
            return self.getTypedRuleContext(RefiParser.CaseinsContext,0)


        def caseinsoff(self):
            return self.getTypedRuleContext(RefiParser.CaseinsoffContext,0)


        def char(self):
            return self.getTypedRuleContext(RefiParser.CharContext,0)


        def ctrl_matcher(self):
            return self.getTypedRuleContext(RefiParser.Ctrl_matcherContext,0)


        def currency(self):
            return self.getTypedRuleContext(RefiParser.CurrencyContext,0)


        def digit(self):
            return self.getTypedRuleContext(RefiParser.DigitContext,0)


        def either_matcher(self):
            return self.getTypedRuleContext(RefiParser.Either_matcherContext,0)


        def eol(self):
            return self.getTypedRuleContext(RefiParser.EolContext,0)


        def escape(self):
            return self.getTypedRuleContext(RefiParser.EscapeContext,0)


        def exactly(self):
            return self.getTypedRuleContext(RefiParser.ExactlyContext,0)


        def expr_param_matcher(self):
            return self.getTypedRuleContext(RefiParser.Expr_param_matcherContext,0)


        def formfeed(self):
            return self.getTypedRuleContext(RefiParser.FormfeedContext,0)


        def flagged(self):
            return self.getTypedRuleContext(RefiParser.FlaggedContext,0)


        def flags(self):
            return self.getTypedRuleContext(RefiParser.FlagsContext,0)


        def greek(self):
            return self.getTypedRuleContext(RefiParser.GreekContext,0)


        def hex_matcher(self):
            return self.getTypedRuleContext(RefiParser.Hex_matcherContext,0)


        def latin(self):
            return self.getTypedRuleContext(RefiParser.LatinContext,0)


        def lower(self):
            return self.getTypedRuleContext(RefiParser.LowerContext,0)


        def newline(self):
            return self.getTypedRuleContext(RefiParser.NewlineContext,0)


        def nondigit(self):
            return self.getTypedRuleContext(RefiParser.NondigitContext,0)


        def not_matcher(self):
            return self.getTypedRuleContext(RefiParser.Not_matcherContext,0)


        def octal_matcher(self):
            return self.getTypedRuleContext(RefiParser.Octal_matcherContext,0)


        def or_matcher(self):
            return self.getTypedRuleContext(RefiParser.Or_matcherContext,0)


        def range_matcher(self):
            return self.getTypedRuleContext(RefiParser.Range_matcherContext,0)


        def return_(self):
            return self.getTypedRuleContext(RefiParser.ReturnContext,0)


        def somespace(self):
            return self.getTypedRuleContext(RefiParser.SomespaceContext,0)


        def string(self):
            return self.getTypedRuleContext(RefiParser.StringContext,0)


        def tab(self):
            return self.getTypedRuleContext(RefiParser.TabContext,0)


        def unicodecase(self):
            return self.getTypedRuleContext(RefiParser.UnicodecaseContext,0)


        def unicodecaseoff(self):
            return self.getTypedRuleContext(RefiParser.UnicodecaseoffContext,0)


        def union(self):
            return self.getTypedRuleContext(RefiParser.UnionContext,0)


        def unixlines(self):
            return self.getTypedRuleContext(RefiParser.UnixlinesContext,0)


        def unixlinesoff(self):
            return self.getTypedRuleContext(RefiParser.UnixlinesoffContext,0)


        def upper(self):
            return self.getTypedRuleContext(RefiParser.UpperContext,0)


        def wild(self):
            return self.getTypedRuleContext(RefiParser.WildContext,0)


        def wordboundary(self):
            return self.getTypedRuleContext(RefiParser.WordboundaryContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcher" ):
                listener.enterMatcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcher" ):
                listener.exitMatcher(self)




    def matcher(self):

        localctx = RefiParser.MatcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matcher)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.atleast()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.backeted_matcher()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.between()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.alphabetic()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.anywild()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.bell()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.bol()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 124
                self.backtick()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 9)
                self.state = 125
                self.capture_matcher()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 10)
                self.state = 126
                self.caseins()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 11)
                self.state = 127
                self.caseinsoff()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 12)
                self.state = 128
                self.char()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 13)
                self.state = 129
                self.ctrl_matcher()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 14)
                self.state = 130
                self.currency()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 15)
                self.state = 131
                self.digit()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 16)
                self.state = 132
                self.either_matcher()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 17)
                self.state = 133
                self.eol()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 18)
                self.state = 134
                self.escape()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 19)
                self.state = 135
                self.exactly()
                pass
            elif token in [16, 47, 53]:
                self.enterOuterAlt(localctx, 20)
                self.state = 136
                self.expr_param_matcher()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 21)
                self.state = 137
                self.formfeed()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 22)
                self.state = 138
                self.flagged()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 23)
                self.state = 139
                self.flags()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 24)
                self.state = 140
                self.greek()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 25)
                self.state = 141
                self.hex_matcher()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 26)
                self.state = 142
                self.latin()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 27)
                self.state = 143
                self.lower()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 28)
                self.state = 144
                self.newline()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 29)
                self.state = 145
                self.nondigit()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 30)
                self.state = 146
                self.not_matcher()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 31)
                self.state = 147
                self.octal_matcher()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 32)
                self.state = 148
                self.or_matcher()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 33)
                self.state = 149
                self.range_matcher()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 34)
                self.state = 150
                self.return_()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 35)
                self.state = 151
                self.somespace()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 36)
                self.state = 152
                self.string()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 37)
                self.state = 153
                self.tab()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 38)
                self.state = 154
                self.unicodecase()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 39)
                self.state = 155
                self.unicodecaseoff()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 40)
                self.state = 156
                self.union()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 41)
                self.state = 157
                self.unixlines()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 42)
                self.state = 158
                self.unixlinesoff()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 43)
                self.state = 159
                self.upper()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 44)
                self.state = 160
                self.wild()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 45)
                self.state = 161
                self.wordboundary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def backtick(self):
            return self.getTypedRuleContext(RefiParser.BacktickContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def wild(self):
            return self.getTypedRuleContext(RefiParser.WildContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_literal_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_matcher" ):
                listener.enterLiteral_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_matcher" ):
                listener.exitLiteral_matcher(self)




    def literal_matcher(self):

        localctx = RefiParser.Literal_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal_matcher)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.backtick()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.backeted_matcher()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.wild()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtleastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None # Token

        def ATLEAST(self):
            return self.getToken(RefiParser.ATLEAST, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def INT(self):
            return self.getToken(RefiParser.INT, 0)

        def matcher(self):
            return self.getTypedRuleContext(RefiParser.MatcherContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_atleast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtleast" ):
                listener.enterAtleast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtleast" ):
                listener.exitAtleast(self)




    def atleast(self):

        localctx = RefiParser.AtleastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atleast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(RefiParser.ATLEAST)
            self.state = 170
            self.match(RefiParser.LEFTCURLY)
            self.state = 171
            localctx.count = self.match(RefiParser.INT)
            self.state = 172
            self.match(RefiParser.COMMA)
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 173
                self.matcher()
                pass

            elif la_ == 2:
                self.state = 174
                self.backeted_matcher()
                pass


            self.state = 177
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BetweenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.from_ = None # Token
            self.to = None # Token

        def BETWEEN(self):
            return self.getToken(RefiParser.BETWEEN, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COMMA)
            else:
                return self.getToken(RefiParser.COMMA, i)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.INT)
            else:
                return self.getToken(RefiParser.INT, i)

        def matcher(self):
            return self.getTypedRuleContext(RefiParser.MatcherContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_between

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetween" ):
                listener.enterBetween(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetween" ):
                listener.exitBetween(self)




    def between(self):

        localctx = RefiParser.BetweenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_between)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(RefiParser.BETWEEN)
            self.state = 180
            self.match(RefiParser.LEFTCURLY)
            self.state = 181
            localctx.from_ = self.match(RefiParser.INT)
            self.state = 182
            self.match(RefiParser.COMMA)
            self.state = 183
            localctx.to = self.match(RefiParser.INT)
            self.state = 184
            self.match(RefiParser.COMMA)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 185
                self.matcher()
                pass

            elif la_ == 2:
                self.state = 186
                self.backeted_matcher()
                pass


            self.state = 189
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capture_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def CAPTURE(self):
            return self.getToken(RefiParser.CAPTURE, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def matcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.MatcherContext)
            else:
                return self.getTypedRuleContext(RefiParser.MatcherContext,i)


        def backeted_matcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.Backeted_matcherContext)
            else:
                return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,i)


        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def STRING(self):
            return self.getToken(RefiParser.STRING, 0)

        def CHAR(self):
            return self.getToken(RefiParser.CHAR, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_capture_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture_matcher" ):
                listener.enterCapture_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture_matcher" ):
                listener.exitCapture_matcher(self)




    def capture_matcher(self):

        localctx = RefiParser.Capture_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_capture_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(RefiParser.CAPTURE)
            self.state = 192
            self.match(RefiParser.LEFTCURLY)
            self.state = 195 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 193
                        self.matcher()
                        pass

                    elif la_ == 2:
                        self.state = 194
                        self.backeted_matcher()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 197 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 199
                self.match(RefiParser.COMMA)
                self.state = 200
                localctx.name = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==11):
                    localctx.name = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 203
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseinsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASEINS(self):
            return self.getToken(RefiParser.CASEINS, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_caseins

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseins" ):
                listener.enterCaseins(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseins" ):
                listener.exitCaseins(self)




    def caseins(self):

        localctx = RefiParser.CaseinsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_caseins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(RefiParser.CASEINS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseinsoffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASEINSOFF(self):
            return self.getToken(RefiParser.CASEINSOFF, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_caseinsoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseinsoff" ):
                listener.enterCaseinsoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseinsoff" ):
                listener.exitCaseinsoff(self)




    def caseinsoff(self):

        localctx = RefiParser.CaseinsoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_caseinsoff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(RefiParser.CASEINSOFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(RefiParser.CHAR, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = RefiParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(RefiParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ctrl_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTRL(self):
            return self.getToken(RefiParser.CTRL, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def INT(self):
            return self.getToken(RefiParser.INT, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_ctrl_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtrl_matcher" ):
                listener.enterCtrl_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtrl_matcher" ):
                listener.exitCtrl_matcher(self)




    def ctrl_matcher(self):

        localctx = RefiParser.Ctrl_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ctrl_matcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(RefiParser.CTRL)
            self.state = 212
            self.match(RefiParser.LEFTCURLY)
            self.state = 213
            self.match(RefiParser.INT)
            self.state = 214
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Either_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EITHER(self):
            return self.getToken(RefiParser.EITHER, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.CHAR)
            else:
                return self.getToken(RefiParser.CHAR, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COMMA)
            else:
                return self.getToken(RefiParser.COMMA, i)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_either_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEither_matcher" ):
                listener.enterEither_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEither_matcher" ):
                listener.exitEither_matcher(self)




    def either_matcher(self):

        localctx = RefiParser.Either_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_either_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(RefiParser.EITHER)
            self.state = 217
            self.match(RefiParser.LEFTCURLY)
            self.state = 218
            self.match(RefiParser.CHAR)
            self.state = 219
            self.match(RefiParser.COMMA)
            self.state = 220
            self.match(RefiParser.CHAR)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 221
                self.match(RefiParser.COMMA)
                self.state = 222
                self.match(RefiParser.CHAR)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_param_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.matchType = None # Match_typeContext

        def matcher_name(self):
            return self.getTypedRuleContext(RefiParser.Matcher_nameContext,0)


        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def matcher(self):
            return self.getTypedRuleContext(RefiParser.MatcherContext,0)


        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def match_type(self):
            return self.getTypedRuleContext(RefiParser.Match_typeContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_expr_param_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_param_matcher" ):
                listener.enterExpr_param_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_param_matcher" ):
                listener.exitExpr_param_matcher(self)




    def expr_param_matcher(self):

        localctx = RefiParser.Expr_param_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_param_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.matcher_name()
            self.state = 231
            self.match(RefiParser.LEFTCURLY)
            self.state = 232
            self.matcher()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 233
                self.match(RefiParser.COMMA)
                self.state = 234
                localctx.matchType = self.match_type()


            self.state = 237
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExactlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None # Token

        def EXACTLY(self):
            return self.getToken(RefiParser.EXACTLY, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def INT(self):
            return self.getToken(RefiParser.INT, 0)

        def matcher(self):
            return self.getTypedRuleContext(RefiParser.MatcherContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_exactly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExactly" ):
                listener.enterExactly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExactly" ):
                listener.exitExactly(self)




    def exactly(self):

        localctx = RefiParser.ExactlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exactly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RefiParser.EXACTLY)
            self.state = 240
            self.match(RefiParser.LEFTCURLY)
            self.state = 241
            localctx.count = self.match(RefiParser.INT)
            self.state = 242
            self.match(RefiParser.COMMA)
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 243
                self.matcher()
                pass

            elif la_ == 2:
                self.state = 244
                self.backeted_matcher()
                pass


            self.state = 247
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlaggedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._flagname = None # FlagnameContext
            self.names = list() # of FlagnameContexts

        def FLAGGED(self):
            return self.getToken(RefiParser.FLAGGED, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COMMA)
            else:
                return self.getToken(RefiParser.COMMA, i)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def flagname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.FlagnameContext)
            else:
                return self.getTypedRuleContext(RefiParser.FlagnameContext,i)


        def matcher(self):
            return self.getTypedRuleContext(RefiParser.MatcherContext,0)


        def backeted_matcher(self):
            return self.getTypedRuleContext(RefiParser.Backeted_matcherContext,0)


        def getRuleIndex(self):
            return RefiParser.RULE_flagged

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagged" ):
                listener.enterFlagged(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagged" ):
                listener.exitFlagged(self)




    def flagged(self):

        localctx = RefiParser.FlaggedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_flagged)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(RefiParser.FLAGGED)
            self.state = 250
            self.match(RefiParser.LEFTCURLY)
            self.state = 251
            localctx._flagname = self.flagname()
            localctx.names.append(localctx._flagname)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 252
                    self.match(RefiParser.COMMA)
                    self.state = 253
                    localctx._flagname = self.flagname()
                    localctx.names.append(localctx._flagname) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 259
            self.match(RefiParser.COMMA)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 260
                self.matcher()
                pass

            elif la_ == 2:
                self.state = 261
                self.backeted_matcher()
                pass


            self.state = 264
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._flagname = None # FlagnameContext
            self.names = list() # of FlagnameContexts

        def FLAGS(self):
            return self.getToken(RefiParser.FLAGS, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def flagname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.FlagnameContext)
            else:
                return self.getTypedRuleContext(RefiParser.FlagnameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COMMA)
            else:
                return self.getToken(RefiParser.COMMA, i)

        def getRuleIndex(self):
            return RefiParser.RULE_flags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlags" ):
                listener.enterFlags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlags" ):
                listener.exitFlags(self)




    def flags(self):

        localctx = RefiParser.FlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_flags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(RefiParser.FLAGS)
            self.state = 267
            self.match(RefiParser.LEFTCURLY)
            self.state = 268
            localctx._flagname = self.flagname()
            localctx.names.append(localctx._flagname)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 269
                    self.match(RefiParser.COMMA)
                    self.state = 270
                    localctx._flagname = self.flagname()
                    localctx.names.append(localctx._flagname) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 276
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GreekContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREEK(self):
            return self.getToken(RefiParser.GREEK, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_greek

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreek" ):
                listener.enterGreek(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreek" ):
                listener.exitGreek(self)




    def greek(self):

        localctx = RefiParser.GreekContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_greek)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(RefiParser.GREEK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hex_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number = None # Token

        def HEX(self):
            return self.getToken(RefiParser.HEX, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def HEX_NUMBER(self):
            return self.getToken(RefiParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_hex_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex_matcher" ):
                listener.enterHex_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex_matcher" ):
                listener.exitHex_matcher(self)




    def hex_matcher(self):

        localctx = RefiParser.Hex_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_hex_matcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(RefiParser.HEX)
            self.state = 281
            self.match(RefiParser.LEFTCURLY)
            self.state = 282
            localctx.number = self.match(RefiParser.HEX_NUMBER)
            self.state = 283
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NondigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONDIGIT(self):
            return self.getToken(RefiParser.NONDIGIT, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_nondigit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNondigit" ):
                listener.enterNondigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNondigit" ):
                listener.exitNondigit(self)




    def nondigit(self):

        localctx = RefiParser.NondigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nondigit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(RefiParser.NONDIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(RefiParser.NOT, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.CHAR)
            else:
                return self.getToken(RefiParser.CHAR, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COMMA)
            else:
                return self.getToken(RefiParser.COMMA, i)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_not_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_matcher" ):
                listener.enterNot_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_matcher" ):
                listener.exitNot_matcher(self)




    def not_matcher(self):

        localctx = RefiParser.Not_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_not_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(RefiParser.NOT)
            self.state = 288
            self.match(RefiParser.LEFTCURLY)
            self.state = 289
            self.match(RefiParser.CHAR)
            self.state = 290
            self.match(RefiParser.COMMA)
            self.state = 291
            self.match(RefiParser.CHAR)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 292
                self.match(RefiParser.COMMA)
                self.state = 293
                self.match(RefiParser.CHAR)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 299
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Octal_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCTAL(self):
            return self.getToken(RefiParser.OCTAL, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def OCTAL_NUMBER(self):
            return self.getToken(RefiParser.OCTAL_NUMBER, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_octal_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctal_matcher" ):
                listener.enterOctal_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctal_matcher" ):
                listener.exitOctal_matcher(self)




    def octal_matcher(self):

        localctx = RefiParser.Octal_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_octal_matcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(RefiParser.OCTAL)
            self.state = 302
            self.match(RefiParser.LEFTCURLY)
            self.state = 303
            self.match(RefiParser.OCTAL_NUMBER)
            self.state = 304
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(RefiParser.OR, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def VERTICAL(self):
            return self.getToken(RefiParser.VERTICAL, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def matcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RefiParser.MatcherContext)
            else:
                return self.getTypedRuleContext(RefiParser.MatcherContext,i)


        def getRuleIndex(self):
            return RefiParser.RULE_or_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_matcher" ):
                listener.enterOr_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_matcher" ):
                listener.exitOr_matcher(self)




    def or_matcher(self):

        localctx = RefiParser.Or_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_or_matcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(RefiParser.OR)
            self.state = 307
            self.match(RefiParser.LEFTCURLY)
            self.state = 309 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 308
                    self.matcher()

                else:
                    raise NoViableAltException(self)
                self.state = 311 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 313
            self.match(RefiParser.VERTICAL)
            self.state = 315 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 314
                    self.matcher()

                else:
                    raise NoViableAltException(self)
                self.state = 317 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 319
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_matcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(RefiParser.RANGE, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.CHAR)
            else:
                return self.getToken(RefiParser.CHAR, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COLON)
            else:
                return self.getToken(RefiParser.COLON, i)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_range_matcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_matcher" ):
                listener.enterRange_matcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_matcher" ):
                listener.exitRange_matcher(self)




    def range_matcher(self):

        localctx = RefiParser.Range_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_range_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(RefiParser.RANGE)
            self.state = 322
            self.match(RefiParser.LEFTCURLY)
            self.state = 323
            self.match(RefiParser.CHAR)
            self.state = 324
            self.match(RefiParser.COLON)
            self.state = 325
            self.match(RefiParser.CHAR)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 326
                self.match(RefiParser.COMMA)
                self.state = 327
                self.match(RefiParser.CHAR)
                self.state = 328
                self.match(RefiParser.COLON)
                self.state = 329
                self.match(RefiParser.CHAR)


            self.state = 332
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNION(self):
            return self.getToken(RefiParser.UNION, 0)

        def LEFTCURLY(self):
            return self.getToken(RefiParser.LEFTCURLY, 0)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.CHAR)
            else:
                return self.getToken(RefiParser.CHAR, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(RefiParser.COLON)
            else:
                return self.getToken(RefiParser.COLON, i)

        def COMMA(self):
            return self.getToken(RefiParser.COMMA, 0)

        def RIGHTCURLY(self):
            return self.getToken(RefiParser.RIGHTCURLY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_union

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)




    def union(self):

        localctx = RefiParser.UnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_union)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(RefiParser.UNION)
            self.state = 335
            self.match(RefiParser.LEFTCURLY)
            self.state = 336
            self.match(RefiParser.CHAR)
            self.state = 337
            self.match(RefiParser.COLON)
            self.state = 338
            self.match(RefiParser.CHAR)
            self.state = 339
            self.match(RefiParser.COMMA)
            self.state = 340
            self.match(RefiParser.CHAR)
            self.state = 341
            self.match(RefiParser.COLON)
            self.state = 342
            self.match(RefiParser.CHAR)
            self.state = 343
            self.match(RefiParser.RIGHTCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RefiParser.STRING, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = RefiParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(RefiParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matcher_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY(self):
            return self.getToken(RefiParser.ANY, 0)

        def OPTIONAL(self):
            return self.getToken(RefiParser.OPTIONAL, 0)

        def SOME(self):
            return self.getToken(RefiParser.SOME, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_matcher_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcher_name" ):
                listener.enterMatcher_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcher_name" ):
                listener.exitMatcher_name(self)




    def matcher_name(self):

        localctx = RefiParser.Matcher_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_matcher_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9147936743161856) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSSES(self):
            return self.getToken(RefiParser.POSSES, 0)

        def RELUCT(self):
            return self.getToken(RefiParser.RELUCT, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_match_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch_type" ):
                listener.enterMatch_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch_type" ):
                listener.exitMatch_type(self)




    def match_type(self):

        localctx = RefiParser.Match_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_match_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(_la==49 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlphabeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHABETIC(self):
            return self.getToken(RefiParser.ALPHABETIC, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_alphabetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlphabetic" ):
                listener.enterAlphabetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlphabetic" ):
                listener.exitAlphabetic(self)




    def alphabetic(self):

        localctx = RefiParser.AlphabeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_alphabetic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(RefiParser.ALPHABETIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnywildContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANYWILD(self):
            return self.getToken(RefiParser.ANYWILD, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_anywild

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnywild" ):
                listener.enterAnywild(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnywild" ):
                listener.exitAnywild(self)




    def anywild(self):

        localctx = RefiParser.AnywildContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_anywild)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(RefiParser.ANYWILD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BacktickContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKTICK(self):
            return self.getToken(RefiParser.BACKTICK, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_backtick

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBacktick" ):
                listener.enterBacktick(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBacktick" ):
                listener.exitBacktick(self)




    def backtick(self):

        localctx = RefiParser.BacktickContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_backtick)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(RefiParser.BACKTICK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BELL(self):
            return self.getToken(RefiParser.BELL, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_bell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBell" ):
                listener.enterBell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBell" ):
                listener.exitBell(self)




    def bell(self):

        localctx = RefiParser.BellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_bell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(RefiParser.BELL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOL(self):
            return self.getToken(RefiParser.BOL, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_bol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBol" ):
                listener.enterBol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBol" ):
                listener.exitBol(self)




    def bol(self):

        localctx = RefiParser.BolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_bol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(RefiParser.BOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CurrencyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURRENCY(self):
            return self.getToken(RefiParser.CURRENCY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_currency

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurrency" ):
                listener.enterCurrency(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurrency" ):
                listener.exitCurrency(self)




    def currency(self):

        localctx = RefiParser.CurrencyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_currency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(RefiParser.CURRENCY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(RefiParser.DIGIT, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = RefiParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(RefiParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCAPE(self):
            return self.getToken(RefiParser.ESCAPE, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_escape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscape" ):
                listener.enterEscape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscape" ):
                listener.exitEscape(self)




    def escape(self):

        localctx = RefiParser.EscapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_escape)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(RefiParser.ESCAPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOL(self):
            return self.getToken(RefiParser.EOL, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_eol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEol" ):
                listener.enterEol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEol" ):
                listener.exitEol(self)




    def eol(self):

        localctx = RefiParser.EolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_eol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(RefiParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASEINS(self):
            return self.getToken(RefiParser.CASEINS, 0)

        def CASEINSOFF(self):
            return self.getToken(RefiParser.CASEINSOFF, 0)

        def UNICODECASE(self):
            return self.getToken(RefiParser.UNICODECASE, 0)

        def UNICODECASEOFF(self):
            return self.getToken(RefiParser.UNICODECASEOFF, 0)

        def UNIXLINES(self):
            return self.getToken(RefiParser.UNIXLINES, 0)

        def UNIXLINESOFF(self):
            return self.getToken(RefiParser.UNIXLINESOFF, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_flagname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagname" ):
                listener.enterFlagname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagname" ):
                listener.exitFlagname(self)




    def flagname(self):

        localctx = RefiParser.FlagnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_flagname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1945555039074385920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormfeedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORMFEED(self):
            return self.getToken(RefiParser.FORMFEED, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_formfeed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormfeed" ):
                listener.enterFormfeed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormfeed" ):
                listener.exitFormfeed(self)




    def formfeed(self):

        localctx = RefiParser.FormfeedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_formfeed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(RefiParser.FORMFEED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LatinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LATIN(self):
            return self.getToken(RefiParser.LATIN, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_latin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatin" ):
                listener.enterLatin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatin" ):
                listener.exitLatin(self)




    def latin(self):

        localctx = RefiParser.LatinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_latin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(RefiParser.LATIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWER(self):
            return self.getToken(RefiParser.LOWER, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_lower

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLower" ):
                listener.enterLower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLower" ):
                listener.exitLower(self)




    def lower(self):

        localctx = RefiParser.LowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_lower)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(RefiParser.LOWER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(RefiParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)




    def newline(self):

        localctx = RefiParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(RefiParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(RefiParser.RETURN, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = RefiParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(RefiParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SomespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOMESPACE(self):
            return self.getToken(RefiParser.SOMESPACE, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_somespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSomespace" ):
                listener.enterSomespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSomespace" ):
                listener.exitSomespace(self)




    def somespace(self):

        localctx = RefiParser.SomespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_somespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(RefiParser.SOMESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TabContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAB(self):
            return self.getToken(RefiParser.TAB, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_tab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab" ):
                listener.enterTab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab" ):
                listener.exitTab(self)




    def tab(self):

        localctx = RefiParser.TabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_tab)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(RefiParser.TAB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnicodecaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNICODECASE(self):
            return self.getToken(RefiParser.UNICODECASE, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_unicodecase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnicodecase" ):
                listener.enterUnicodecase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnicodecase" ):
                listener.exitUnicodecase(self)




    def unicodecase(self):

        localctx = RefiParser.UnicodecaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_unicodecase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(RefiParser.UNICODECASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnicodecaseoffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNICODECASEOFF(self):
            return self.getToken(RefiParser.UNICODECASEOFF, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_unicodecaseoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnicodecaseoff" ):
                listener.enterUnicodecaseoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnicodecaseoff" ):
                listener.exitUnicodecaseoff(self)




    def unicodecaseoff(self):

        localctx = RefiParser.UnicodecaseoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unicodecaseoff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(RefiParser.UNICODECASEOFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnixlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIXLINES(self):
            return self.getToken(RefiParser.UNIXLINES, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_unixlines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnixlines" ):
                listener.enterUnixlines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnixlines" ):
                listener.exitUnixlines(self)




    def unixlines(self):

        localctx = RefiParser.UnixlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_unixlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(RefiParser.UNIXLINES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnixlinesoffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIXLINESOFF(self):
            return self.getToken(RefiParser.UNIXLINESOFF, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_unixlinesoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnixlinesoff" ):
                listener.enterUnixlinesoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnixlinesoff" ):
                listener.exitUnixlinesoff(self)




    def unixlinesoff(self):

        localctx = RefiParser.UnixlinesoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_unixlinesoff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(RefiParser.UNIXLINESOFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPPER(self):
            return self.getToken(RefiParser.UPPER, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_upper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpper" ):
                listener.enterUpper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpper" ):
                listener.exitUpper(self)




    def upper(self):

        localctx = RefiParser.UpperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_upper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(RefiParser.UPPER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WILD(self):
            return self.getToken(RefiParser.WILD, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_wild

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWild" ):
                listener.enterWild(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWild" ):
                listener.exitWild(self)




    def wild(self):

        localctx = RefiParser.WildContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_wild)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(RefiParser.WILD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordboundaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORDBOUNDARY(self):
            return self.getToken(RefiParser.WORDBOUNDARY, 0)

        def getRuleIndex(self):
            return RefiParser.RULE_wordboundary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordboundary" ):
                listener.enterWordboundary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordboundary" ):
                listener.exitWordboundary(self)




    def wordboundary(self):

        localctx = RefiParser.WordboundaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_wordboundary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(RefiParser.WORDBOUNDARY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





