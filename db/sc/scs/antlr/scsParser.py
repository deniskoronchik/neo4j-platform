# Generated from sc/scs/scs.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from sc.scs.types import *

def create_token_context(ctx: any) -> TokenContext:
	return TokenContext(line=ctx.line, column=ctx.column, text=ctx.text)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u00d4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\5\2\64\n\2\3\2\3\2\3\3\3\3\3\3\7\3;\n\3\f\3")
        buf.write("\16\3>\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\7\5G\n\5\f\5\16")
        buf.write("\5J\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\5\7T\n\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5")
        buf.write("\16p\n\16\3\16\3\16\3\16\3\17\3\17\5\17w\n\17\3\17\3\17")
        buf.write("\3\17\5\17|\n\17\3\17\7\17\177\n\17\f\17\16\17\u0082\13")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u008c")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u0098\n\22\3\23\3\23\5\23\u009c\n\23\3\23\3\23\3")
        buf.write("\23\5\23\u00a1\n\23\7\23\u00a3\n\23\f\23\16\23\u00a6\13")
        buf.write("\23\3\24\3\24\5\24\u00aa\n\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\6\25\u00b2\n\25\r\25\16\25\u00b3\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u00c1\n")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\7\30\u00c9\n\30\f\30")
        buf.write("\16\30\u00cc\13\30\3\31\3\31\6\31\u00d0\n\31\r\31\16\31")
        buf.write("\u00d1\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\2\5\3\2\4+\4\2--<<\3\2/\62\2\u00d2\2\63")
        buf.write("\3\2\2\2\4\67\3\2\2\2\6B\3\2\2\2\bH\3\2\2\2\nM\3\2\2\2")
        buf.write("\fS\3\2\2\2\16U\3\2\2\2\20X\3\2\2\2\22[\3\2\2\2\24`\3")
        buf.write("\2\2\2\26c\3\2\2\2\30h\3\2\2\2\32k\3\2\2\2\34t\3\2\2\2")
        buf.write("\36\u008b\3\2\2\2 \u008d\3\2\2\2\"\u0097\3\2\2\2$\u0099")
        buf.write("\3\2\2\2&\u00a7\3\2\2\2(\u00ad\3\2\2\2*\u00b7\3\2\2\2")
        buf.write(",\u00be\3\2\2\2.\u00c4\3\2\2\2\60\u00cf\3\2\2\2\62\64")
        buf.write("\7\3\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\66\7@\2\2\66\3\3\2\2\2\678\7>\2\28<\6\3\2\29;\5\n\6\2")
        buf.write(":9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2><\3")
        buf.write("\2\2\2?@\7?\2\2@A\b\3\1\2A\5\3\2\2\2BC\t\2\2\2CD\b\4\1")
        buf.write("\2D\7\3\2\2\2EG\5\n\6\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2")
        buf.write("HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\7\2\2\3L\t\3\2\2\2MN")
        buf.write("\5\f\7\2NO\7,\2\2O\13\3\2\2\2PT\5*\26\2QT\5\22\n\2RT\5")
        buf.write(".\30\2SP\3\2\2\2SQ\3\2\2\2SR\3\2\2\2T\r\3\2\2\2UV\7=\2")
        buf.write("\2VW\b\b\1\2W\17\3\2\2\2XY\t\3\2\2YZ\b\t\1\2Z\21\3\2\2")
        buf.write("\2[\\\7=\2\2\\]\7.\2\2]^\5\"\22\2^_\b\n\1\2_\23\3\2\2")
        buf.write("\2`a\t\4\2\2ab\b\13\1\2b\25\3\2\2\2cd\5\24\13\2de\7\63")
        buf.write("\2\2ef\7<\2\2fg\b\f\1\2g\27\3\2\2\2hi\5\26\f\2ij\b\r\1")
        buf.write("\2j\31\3\2\2\2kl\7\64\2\2lm\5\36\20\2mo\5\6\4\2np\5\60")
        buf.write("\31\2on\3\2\2\2op\3\2\2\2pq\3\2\2\2qr\5\36\20\2rs\7\65")
        buf.write("\2\2s\33\3\2\2\2tv\7\66\2\2uw\5\60\31\2vu\3\2\2\2vw\3")
        buf.write("\2\2\2wx\3\2\2\2x\u0080\5\"\22\2y{\7\67\2\2z|\5\60\31")
        buf.write("\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2\2}\177\5\"\22\2~y\3\2\2")
        buf.write("\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084")
        buf.write("\78\2\2\u0084\35\3\2\2\2\u0085\u0086\5\16\b\2\u0086\u0087")
        buf.write("\b\20\1\2\u0087\u008c\3\2\2\2\u0088\u0089\5\20\t\2\u0089")
        buf.write("\u008a\b\20\1\2\u008a\u008c\3\2\2\2\u008b\u0085\3\2\2")
        buf.write("\2\u008b\u0088\3\2\2\2\u008c\37\3\2\2\2\u008d\u008e\7")
        buf.write("A\2\2\u008e!\3\2\2\2\u008f\u0090\5\36\20\2\u0090\u0091")
        buf.write("\b\22\1\2\u0091\u0098\3\2\2\2\u0092\u0098\5\32\16\2\u0093")
        buf.write("\u0098\5\34\17\2\u0094\u0098\5\4\3\2\u0095\u0098\5\2\2")
        buf.write("\2\u0096\u0098\5 \21\2\u0097\u008f\3\2\2\2\u0097\u0092")
        buf.write("\3\2\2\2\u0097\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098#\3\2\2\2\u0099")
        buf.write("\u009b\5\"\22\2\u009a\u009c\5(\25\2\u009b\u009a\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009c\u00a4\3\2\2\2\u009d\u009e")
        buf.write("\7\67\2\2\u009e\u00a0\5\"\22\2\u009f\u00a1\5(\25\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2")
        buf.write("\u00a2\u009d\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a4\u00a5\3\2\2\2\u00a5%\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a7\u00a9\5\6\4\2\u00a8\u00aa\5\60\31\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\5$\23\2\u00ac\'\3\2\2\2\u00ad\u00b1\79\2")
        buf.write("\2\u00ae\u00af\5&\24\2\u00af\u00b0\7,\2\2\u00b0\u00b2")
        buf.write("\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b6\7:\2\2\u00b6)\3\2\2\2\u00b7\u00b8\5\30\r")
        buf.write("\2\u00b8\u00b9\7;\2\2\u00b9\u00ba\5\30\r\2\u00ba\u00bb")
        buf.write("\7;\2\2\u00bb\u00bc\5\30\r\2\u00bc\u00bd\b\26\1\2\u00bd")
        buf.write("+\3\2\2\2\u00be\u00c0\5\6\4\2\u00bf\u00c1\5\60\31\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c3\5$\23\2\u00c3-\3\2\2\2\u00c4\u00c5\5\"\22")
        buf.write("\2\u00c5\u00ca\5,\27\2\u00c6\u00c7\7\67\2\2\u00c7\u00c9")
        buf.write("\5,\27\2\u00c8\u00c6\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb/\3\2\2\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cd\u00ce\7<\2\2\u00ce\u00d0\7B\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\61\3\2\2\2\24\63<HSov{\u0080")
        buf.write("\u008b\u0097\u009b\u00a0\u00a4\u00a9\u00b3\u00c0\u00ca")
        buf.write("\u00d1")
        return buf.getvalue()


class scsParser ( Parser ):

    grammarFileName = "scs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "'<>'", "'>'", "'<'", "'..>'", 
                     "'<..'", "'->'", "'<-'", "'<=>'", "'=>'", "'<='", "'-|>'", 
                     "'<|-'", "'-/>'", "'</-'", "'~>'", "'<~'", "'~|>'", 
                     "'<|~'", "'~/>'", "'</~'", "'_<>'", "'_>'", "'_<'", 
                     "'_..>'", "'_<..'", "'_->'", "'_<-'", "'_<=>'", "'_=>'", 
                     "'_<='", "'_-|>'", "'_<|-'", "'_-/>'", "'_</-'", "'_~>'", 
                     "'_<~'", "'_~|>'", "'_<|~'", "'_~/>'", "'_</~'", "';;'", 
                     "'...'", "'='", "'sc_node'", "'sc_link'", "'sc_edge'", 
                     "'sc_arc'", "'#'", "'('", "')'", "'{'", "';'", "'}'", 
                     "'(*'", "'*)'", "'|'", "<INVALID>", "<INVALID>", "'[*'", 
                     "'*]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID_SYSTEM", "ALIAS_SYMBOLS", 
                      "CONTOUR_BEGIN", "CONTOUR_END", "CONTENT_BODY", "LINK", 
                      "EDGE_ATTR", "LINE_TERMINATOR", "LINE_COMMENT", "MULTINE_COMMENT", 
                      "WS" ]

    RULE_content = 0
    RULE_contour = 1
    RULE_connector = 2
    RULE_syntax = 3
    RULE_sentence_wrap = 4
    RULE_sentence = 5
    RULE_ifdf_alias = 6
    RULE_idtf_system = 7
    RULE_sentence_assign = 8
    RULE_idtf_lvl1_preffix = 9
    RULE_idtf_lvl1_value = 10
    RULE_idtf_lvl1 = 11
    RULE_idtf_edge = 12
    RULE_idtf_set = 13
    RULE_idtf_atomic = 14
    RULE_idtf_url = 15
    RULE_idtf_common = 16
    RULE_idtf_list = 17
    RULE_internal_sentence = 18
    RULE_internal_sentence_list = 19
    RULE_sentence_lvl1 = 20
    RULE_sentence_lvl_4_list_item = 21
    RULE_sentence_lvl_common = 22
    RULE_attr_list = 23

    ruleNames =  [ "content", "contour", "connector", "syntax", "sentence_wrap", 
                   "sentence", "ifdf_alias", "idtf_system", "sentence_assign", 
                   "idtf_lvl1_preffix", "idtf_lvl1_value", "idtf_lvl1", 
                   "idtf_edge", "idtf_set", "idtf_atomic", "idtf_url", "idtf_common", 
                   "idtf_list", "internal_sentence", "internal_sentence_list", 
                   "sentence_lvl1", "sentence_lvl_4_list_item", "sentence_lvl_common", 
                   "attr_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    ID_SYSTEM=58
    ALIAS_SYMBOLS=59
    CONTOUR_BEGIN=60
    CONTOUR_END=61
    CONTENT_BODY=62
    LINK=63
    EDGE_ATTR=64
    LINE_TERMINATOR=65
    LINE_COMMENT=66
    MULTINE_COMMENT=67
    WS=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTENT_BODY(self):
            return self.getToken(scsParser.CONTENT_BODY, 0)

        def getRuleIndex(self):
            return scsParser.RULE_content




    def content(self):

        localctx = scsParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__0:
                self.state = 48
                self.match(scsParser.T__0)


            self.state = 51
            self.match(scsParser.CONTENT_BODY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContourContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTOUR_BEGIN(self):
            return self.getToken(scsParser.CONTOUR_BEGIN, 0)

        def CONTOUR_END(self):
            return self.getToken(scsParser.CONTOUR_END, 0)

        def sentence_wrap(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_wrapContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_wrapContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_contour




    def contour(self):

        localctx = scsParser.ContourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_contour)
        count = 1
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(scsParser.CONTOUR_BEGIN)
            self.state = 54
            if not count > 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "count > 0")

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__42) | (1 << scsParser.T__44) | (1 << scsParser.T__45) | (1 << scsParser.T__46) | (1 << scsParser.T__47) | (1 << scsParser.T__49) | (1 << scsParser.T__51) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 55
                self.sentence_wrap()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(scsParser.CONTOUR_END)

            count -= 1
            if count == 0:
                pass
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symbol = None
            self.c = None # Token


        def getRuleIndex(self):
            return scsParser.RULE_connector




    def connector(self):

        localctx = scsParser.ConnectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_connector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx.c = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__1) | (1 << scsParser.T__2) | (1 << scsParser.T__3) | (1 << scsParser.T__4) | (1 << scsParser.T__5) | (1 << scsParser.T__6) | (1 << scsParser.T__7) | (1 << scsParser.T__8) | (1 << scsParser.T__9) | (1 << scsParser.T__10) | (1 << scsParser.T__11) | (1 << scsParser.T__12) | (1 << scsParser.T__13) | (1 << scsParser.T__14) | (1 << scsParser.T__15) | (1 << scsParser.T__16) | (1 << scsParser.T__17) | (1 << scsParser.T__18) | (1 << scsParser.T__19) | (1 << scsParser.T__20) | (1 << scsParser.T__21) | (1 << scsParser.T__22) | (1 << scsParser.T__23) | (1 << scsParser.T__24) | (1 << scsParser.T__25) | (1 << scsParser.T__26) | (1 << scsParser.T__27) | (1 << scsParser.T__28) | (1 << scsParser.T__29) | (1 << scsParser.T__30) | (1 << scsParser.T__31) | (1 << scsParser.T__32) | (1 << scsParser.T__33) | (1 << scsParser.T__34) | (1 << scsParser.T__35) | (1 << scsParser.T__36) | (1 << scsParser.T__37) | (1 << scsParser.T__38) | (1 << scsParser.T__39) | (1 << scsParser.T__40))) != 0)):
                localctx.c = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.symbol = (None if localctx.c is None else localctx.c.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SyntaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(scsParser.EOF, 0)

        def sentence_wrap(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_wrapContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_wrapContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_syntax




    def syntax(self):

        localctx = scsParser.SyntaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_syntax)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__0) | (1 << scsParser.T__42) | (1 << scsParser.T__44) | (1 << scsParser.T__45) | (1 << scsParser.T__46) | (1 << scsParser.T__47) | (1 << scsParser.T__49) | (1 << scsParser.T__51) | (1 << scsParser.ID_SYSTEM) | (1 << scsParser.ALIAS_SYMBOLS) | (1 << scsParser.CONTOUR_BEGIN) | (1 << scsParser.CONTENT_BODY) | (1 << scsParser.LINK))) != 0):
                self.state = 67
                self.sentence_wrap()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(scsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_wrapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(scsParser.SentenceContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_wrap




    def sentence_wrap(self):

        localctx = scsParser.Sentence_wrapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentence_wrap)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.sentence()
            self.state = 76
            self.match(scsParser.T__41)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence_lvl1(self):
            return self.getTypedRuleContext(scsParser.Sentence_lvl1Context,0)


        def sentence_assign(self):
            return self.getTypedRuleContext(scsParser.Sentence_assignContext,0)


        def sentence_lvl_common(self):
            return self.getTypedRuleContext(scsParser.Sentence_lvl_commonContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence




    def sentence(self):

        localctx = scsParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentence)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.sentence_lvl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.sentence_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.sentence_lvl_common()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifdf_aliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._ALIAS_SYMBOLS = None # Token

        def ALIAS_SYMBOLS(self):
            return self.getToken(scsParser.ALIAS_SYMBOLS, 0)

        def getRuleIndex(self):
            return scsParser.RULE_ifdf_alias




    def ifdf_alias(self):

        localctx = scsParser.Ifdf_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifdf_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            localctx._ALIAS_SYMBOLS = self.match(scsParser.ALIAS_SYMBOLS)

            localctx.el = self._impl.create_alias(create_token_context(localctx._ALIAS_SYMBOLS))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_systemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.value = None # Token

        def ID_SYSTEM(self):
            return self.getToken(scsParser.ID_SYSTEM, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_system




    def idtf_system(self):

        localctx = scsParser.Idtf_systemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idtf_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==scsParser.T__42 or _la==scsParser.ID_SYSTEM):
                localctx.value = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            localctx.el = create_token_context(localctx.value)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ALIAS_SYMBOLS = None # Token
            self._idtf_common = None # Idtf_commonContext

        def ALIAS_SYMBOLS(self):
            return self.getToken(scsParser.ALIAS_SYMBOLS, 0)

        def idtf_common(self):
            return self.getTypedRuleContext(scsParser.Idtf_commonContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_assign




    def sentence_assign(self):

        localctx = scsParser.Sentence_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sentence_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            localctx._ALIAS_SYMBOLS = self.match(scsParser.ALIAS_SYMBOLS)
            self.state = 90
            self.match(scsParser.T__43)
            self.state = 91
            localctx._idtf_common = self.idtf_common()


            context = create_token_context(localctx._ALIAS_SYMBOLS)
            self._impl.define_alias(self._impl.create_alias(context), localctx._idtf_common.el)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_lvl1_preffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.context = None
            self.value = None # Token


        def getRuleIndex(self):
            return scsParser.RULE_idtf_lvl1_preffix




    def idtf_lvl1_preffix(self):

        localctx = scsParser.Idtf_lvl1_preffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idtf_lvl1_preffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__44) | (1 << scsParser.T__45) | (1 << scsParser.T__46) | (1 << scsParser.T__47))) != 0)):
                localctx.value = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            localctx.context = create_token_context(localctx.value)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_lvl1_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self.t = None # Idtf_lvl1_preffixContext
            self.i = None # Token

        def idtf_lvl1_preffix(self):
            return self.getTypedRuleContext(scsParser.Idtf_lvl1_preffixContext,0)


        def ID_SYSTEM(self):
            return self.getToken(scsParser.ID_SYSTEM, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_lvl1_value




    def idtf_lvl1_value(self):

        localctx = scsParser.Idtf_lvl1_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idtf_lvl1_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            localctx.t = self.idtf_lvl1_preffix()
            self.state = 98
            self.match(scsParser.T__48)
            self.state = 99
            localctx.i = self.match(scsParser.ID_SYSTEM)

            context = localctx.t.context
            context._length += 1 + len((None if localctx.i is None else localctx.i.text))
            localctx.el = self._impl._processIdtfLevel1(context, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)), (None if localctx.i is None else localctx.i.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_lvl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._idtf_lvl1_value = None # Idtf_lvl1_valueContext

        def idtf_lvl1_value(self):
            return self.getTypedRuleContext(scsParser.Idtf_lvl1_valueContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_lvl1




    def idtf_lvl1(self):

        localctx = scsParser.Idtf_lvl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idtf_lvl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            localctx._idtf_lvl1_value = self.idtf_lvl1_value()

            localctx.el = localctx._idtf_lvl1_value.el

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_edgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtf_atomic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_atomicContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_atomicContext,i)


        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_edge




    def idtf_edge(self):

        localctx = scsParser.Idtf_edgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_idtf_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(scsParser.T__49)
            self.state = 106
            self.idtf_atomic()
            self.state = 107
            self.connector()
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 108
                self.attr_list()


            self.state = 111
            self.idtf_atomic()
            self.state = 112
            self.match(scsParser.T__50)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtf_common(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_commonContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_commonContext,i)


        def attr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Attr_listContext)
            else:
                return self.getTypedRuleContext(scsParser.Attr_listContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_set




    def idtf_set(self):

        localctx = scsParser.Idtf_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idtf_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(scsParser.T__51)
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 115
                self.attr_list()


            self.state = 118
            self.idtf_common()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__52:
                self.state = 119
                self.match(scsParser.T__52)
                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.attr_list()


                self.state = 123
                self.idtf_common()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(scsParser.T__53)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_atomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._ifdf_alias = None # Ifdf_aliasContext
            self._idtf_system = None # Idtf_systemContext

        def ifdf_alias(self):
            return self.getTypedRuleContext(scsParser.Ifdf_aliasContext,0)


        def idtf_system(self):
            return self.getTypedRuleContext(scsParser.Idtf_systemContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_atomic




    def idtf_atomic(self):

        localctx = scsParser.Idtf_atomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idtf_atomic)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                localctx._ifdf_alias = self.ifdf_alias()
                localctx.el = localctx._ifdf_alias.el
                pass
            elif token in [scsParser.T__42, scsParser.ID_SYSTEM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                localctx._idtf_system = self.idtf_system()
                localctx.el = localctx._idtf_system.el
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


    class Idtf_urlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINK(self):
            return self.getToken(scsParser.LINK, 0)

        def getRuleIndex(self):
            return scsParser.RULE_idtf_url




    def idtf_url(self):

        localctx = scsParser.Idtf_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idtf_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(scsParser.LINK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idtf_commonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.el = None
            self._idtf_atomic = None # Idtf_atomicContext

        def idtf_atomic(self):
            return self.getTypedRuleContext(scsParser.Idtf_atomicContext,0)


        def idtf_edge(self):
            return self.getTypedRuleContext(scsParser.Idtf_edgeContext,0)


        def idtf_set(self):
            return self.getTypedRuleContext(scsParser.Idtf_setContext,0)


        def contour(self):
            return self.getTypedRuleContext(scsParser.ContourContext,0)


        def content(self):
            return self.getTypedRuleContext(scsParser.ContentContext,0)


        def idtf_url(self):
            return self.getTypedRuleContext(scsParser.Idtf_urlContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_common




    def idtf_common(self):

        localctx = scsParser.Idtf_commonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_idtf_common)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scsParser.T__42, scsParser.ID_SYSTEM, scsParser.ALIAS_SYMBOLS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                localctx._idtf_atomic = self.idtf_atomic()
                localctx.el = localctx._idtf_atomic.el
                pass
            elif token in [scsParser.T__49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.idtf_edge()
                pass
            elif token in [scsParser.T__51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.idtf_set()
                pass
            elif token in [scsParser.CONTOUR_BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.contour()
                pass
            elif token in [scsParser.T__0, scsParser.CONTENT_BODY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.content()
                pass
            elif token in [scsParser.LINK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.idtf_url()
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


    class Idtf_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.i2 = None # Idtf_commonContext

        def idtf_common(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_commonContext)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_commonContext,i)


        def internal_sentence_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Internal_sentence_listContext)
            else:
                return self.getTypedRuleContext(scsParser.Internal_sentence_listContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_idtf_list




    def idtf_list(self):

        localctx = scsParser.Idtf_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idtf_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.idtf_common()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scsParser.T__54:
                self.state = 152
                self.internal_sentence_list()


            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.match(scsParser.T__52)
                    self.state = 156
                    localctx.i2 = self.idtf_common()
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==scsParser.T__54:
                        self.state = 157
                        self.internal_sentence_list()

             
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Internal_sentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def idtf_list(self):
            return self.getTypedRuleContext(scsParser.Idtf_listContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_internal_sentence




    def internal_sentence(self):

        localctx = scsParser.Internal_sentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_internal_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.connector()
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 166
                self.attr_list()


            self.state = 169
            self.idtf_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Internal_sentence_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def internal_sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Internal_sentenceContext)
            else:
                return self.getTypedRuleContext(scsParser.Internal_sentenceContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_internal_sentence_list




    def internal_sentence_list(self):

        localctx = scsParser.Internal_sentence_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_internal_sentence_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(scsParser.T__54)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.internal_sentence()
                self.state = 173
                self.match(scsParser.T__41)
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scsParser.T__1) | (1 << scsParser.T__2) | (1 << scsParser.T__3) | (1 << scsParser.T__4) | (1 << scsParser.T__5) | (1 << scsParser.T__6) | (1 << scsParser.T__7) | (1 << scsParser.T__8) | (1 << scsParser.T__9) | (1 << scsParser.T__10) | (1 << scsParser.T__11) | (1 << scsParser.T__12) | (1 << scsParser.T__13) | (1 << scsParser.T__14) | (1 << scsParser.T__15) | (1 << scsParser.T__16) | (1 << scsParser.T__17) | (1 << scsParser.T__18) | (1 << scsParser.T__19) | (1 << scsParser.T__20) | (1 << scsParser.T__21) | (1 << scsParser.T__22) | (1 << scsParser.T__23) | (1 << scsParser.T__24) | (1 << scsParser.T__25) | (1 << scsParser.T__26) | (1 << scsParser.T__27) | (1 << scsParser.T__28) | (1 << scsParser.T__29) | (1 << scsParser.T__30) | (1 << scsParser.T__31) | (1 << scsParser.T__32) | (1 << scsParser.T__33) | (1 << scsParser.T__34) | (1 << scsParser.T__35) | (1 << scsParser.T__36) | (1 << scsParser.T__37) | (1 << scsParser.T__38) | (1 << scsParser.T__39) | (1 << scsParser.T__40))) != 0)):
                    break

            self.state = 179
            self.match(scsParser.T__55)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None # Idtf_lvl1Context
            self.edge = None # Idtf_lvl1Context
            self.trg = None # Idtf_lvl1Context

        def idtf_lvl1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Idtf_lvl1Context)
            else:
                return self.getTypedRuleContext(scsParser.Idtf_lvl1Context,i)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl1




    def sentence_lvl1(self):

        localctx = scsParser.Sentence_lvl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sentence_lvl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            localctx.src = self.idtf_lvl1()
            self.state = 182
            self.match(scsParser.T__56)
            self.state = 183
            localctx.edge = self.idtf_lvl1()
            self.state = 184
            self.match(scsParser.T__56)
            self.state = 185
            localctx.trg = self.idtf_lvl1()

            self._impl.append_triple(localctx.src.el, localctx.edge.el, localctx.trg.el)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl_4_list_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connector(self):
            return self.getTypedRuleContext(scsParser.ConnectorContext,0)


        def idtf_list(self):
            return self.getTypedRuleContext(scsParser.Idtf_listContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(scsParser.Attr_listContext,0)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl_4_list_item




    def sentence_lvl_4_list_item(self):

        localctx = scsParser.Sentence_lvl_4_list_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_sentence_lvl_4_list_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.connector()
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 189
                self.attr_list()


            self.state = 192
            self.idtf_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_lvl_commonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtf_common(self):
            return self.getTypedRuleContext(scsParser.Idtf_commonContext,0)


        def sentence_lvl_4_list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scsParser.Sentence_lvl_4_list_itemContext)
            else:
                return self.getTypedRuleContext(scsParser.Sentence_lvl_4_list_itemContext,i)


        def getRuleIndex(self):
            return scsParser.RULE_sentence_lvl_common




    def sentence_lvl_common(self):

        localctx = scsParser.Sentence_lvl_commonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sentence_lvl_common)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.idtf_common()
            self.state = 195
            self.sentence_lvl_4_list_item()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==scsParser.T__52:
                self.state = 196
                self.match(scsParser.T__52)
                self.state = 197
                self.sentence_lvl_4_list_item()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_SYSTEM(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.ID_SYSTEM)
            else:
                return self.getToken(scsParser.ID_SYSTEM, i)

        def EDGE_ATTR(self, i:int=None):
            if i is None:
                return self.getTokens(scsParser.EDGE_ATTR)
            else:
                return self.getToken(scsParser.EDGE_ATTR, i)

        def getRuleIndex(self):
            return scsParser.RULE_attr_list




    def attr_list(self):

        localctx = scsParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_attr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 203
                    self.match(scsParser.ID_SYSTEM)
                    self.state = 204
                    self.match(scsParser.EDGE_ATTR)

                else:
                    raise NoViableAltException(self)
                self.state = 207 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.contour_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def contour_sempred(self, localctx:ContourContext, predIndex:int):
            if predIndex == 0:
                return count > 0
         




