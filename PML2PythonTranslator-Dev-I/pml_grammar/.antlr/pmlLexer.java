// Generated from d:\PML\pml\PML2PythonTranslator-Dev-I\pml_grammar\pml.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pmlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, IDENTIFIER=7, STRING_LITERAL=8, 
		NUMBER=9, FLOAT=10, INT=11, STRUDEL=12, LCURLY=13, RCURLY=14, LPAREN=15, 
		RPAREN=16, LBRACK=17, RBRACK=18, PIPE=19, COMMA=20, COLON=21, SEMI=22, 
		PLUS=23, MINUS=24, TIMES=25, DIV=26, GT=27, GE=28, LT=29, LE=30, EQ=31, 
		COMMENT=32, WS=33;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "IDENTIFIER", "STRING_LITERAL", 
		"NUMBER", "FLOAT", "INT", "STRUDEL", "LCURLY", "RCURLY", "LPAREN", "RPAREN", 
		"LBRACK", "RBRACK", "PIPE", "COMMA", "COLON", "SEMI", "PLUS", "MINUS", 
		"TIMES", "DIV", "GT", "GE", "LT", "LE", "EQ", "COMMENT", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'attr'", "'random_normal'", "'random_weighted'", "'if'", "'item'", 
		"'.'", null, null, null, null, null, "'@'", "'{'", "'}'", "'('", "')'", 
		"'['", "']'", "'|'", "','", "':'", "';'", "'+'", "'-'", "'*'", "'/'", 
		"'>'", "'>='", "'<'", "'<='", "'=='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, "IDENTIFIER", "STRING_LITERAL", 
		"NUMBER", "FLOAT", "INT", "STRUDEL", "LCURLY", "RCURLY", "LPAREN", "RPAREN", 
		"LBRACK", "RBRACK", "PIPE", "COMMA", "COLON", "SEMI", "PLUS", "MINUS", 
		"TIMES", "DIV", "GT", "GE", "LT", "LE", "EQ", "COMMENT", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public pmlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "pml.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2#\u00d4\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\7\bu\n\b"+
		"\f\b\16\bx\13\b\3\t\3\t\3\t\3\t\7\t~\n\t\f\t\16\t\u0081\13\t\3\t\3\t\3"+
		"\n\3\n\5\n\u0087\n\n\3\13\3\13\3\13\7\13\u008c\n\13\f\13\16\13\u008f\13"+
		"\13\3\f\6\f\u0092\n\f\r\f\16\f\u0093\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27"+
		"\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35"+
		"\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\7!\u00c5\n!\f!\16!\u00c8"+
		"\13!\3!\3!\3!\3!\3\"\6\"\u00cf\n\"\r\"\16\"\u00d0\3\"\3\"\3\u00c6\2#\3"+
		"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37"+
		"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37="+
		" ?!A\"C#\3\2\7\4\2C\\c|\7\2//\62;C\\aac|\3\2$$\4\2\f\f\17\17\5\2\13\f"+
		"\17\17\"\"\2\u00db\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\3E"+
		"\3\2\2\2\5J\3\2\2\2\7X\3\2\2\2\th\3\2\2\2\13k\3\2\2\2\rp\3\2\2\2\17r\3"+
		"\2\2\2\21y\3\2\2\2\23\u0086\3\2\2\2\25\u0088\3\2\2\2\27\u0091\3\2\2\2"+
		"\31\u0095\3\2\2\2\33\u0097\3\2\2\2\35\u0099\3\2\2\2\37\u009b\3\2\2\2!"+
		"\u009d\3\2\2\2#\u009f\3\2\2\2%\u00a1\3\2\2\2\'\u00a3\3\2\2\2)\u00a5\3"+
		"\2\2\2+\u00a7\3\2\2\2-\u00a9\3\2\2\2/\u00ab\3\2\2\2\61\u00ad\3\2\2\2\63"+
		"\u00af\3\2\2\2\65\u00b1\3\2\2\2\67\u00b3\3\2\2\29\u00b5\3\2\2\2;\u00b8"+
		"\3\2\2\2=\u00ba\3\2\2\2?\u00bd\3\2\2\2A\u00c0\3\2\2\2C\u00ce\3\2\2\2E"+
		"F\7c\2\2FG\7v\2\2GH\7v\2\2HI\7t\2\2I\4\3\2\2\2JK\7t\2\2KL\7c\2\2LM\7p"+
		"\2\2MN\7f\2\2NO\7q\2\2OP\7o\2\2PQ\7a\2\2QR\7p\2\2RS\7q\2\2ST\7t\2\2TU"+
		"\7o\2\2UV\7c\2\2VW\7n\2\2W\6\3\2\2\2XY\7t\2\2YZ\7c\2\2Z[\7p\2\2[\\\7f"+
		"\2\2\\]\7q\2\2]^\7o\2\2^_\7a\2\2_`\7y\2\2`a\7g\2\2ab\7k\2\2bc\7i\2\2c"+
		"d\7j\2\2de\7v\2\2ef\7g\2\2fg\7f\2\2g\b\3\2\2\2hi\7k\2\2ij\7h\2\2j\n\3"+
		"\2\2\2kl\7k\2\2lm\7v\2\2mn\7g\2\2no\7o\2\2o\f\3\2\2\2pq\7\60\2\2q\16\3"+
		"\2\2\2rv\t\2\2\2su\t\3\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\20"+
		"\3\2\2\2xv\3\2\2\2y\177\7$\2\2z{\7$\2\2{~\7$\2\2|~\n\4\2\2}z\3\2\2\2}"+
		"|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3"+
		"\2\2\2\u0081\177\3\2\2\2\u0082\u0083\7$\2\2\u0083\22\3\2\2\2\u0084\u0087"+
		"\5\25\13\2\u0085\u0087\5\27\f\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2"+
		"\2\u0087\24\3\2\2\2\u0088\u0089\5\27\f\2\u0089\u008d\7\60\2\2\u008a\u008c"+
		"\5\27\f\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2"+
		"\u008d\u008e\3\2\2\2\u008e\26\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0092"+
		"\4\62;\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\30\3\2\2\2\u0095\u0096\7B\2\2\u0096\32\3\2\2\2\u0097"+
		"\u0098\7}\2\2\u0098\34\3\2\2\2\u0099\u009a\7\177\2\2\u009a\36\3\2\2\2"+
		"\u009b\u009c\7*\2\2\u009c \3\2\2\2\u009d\u009e\7+\2\2\u009e\"\3\2\2\2"+
		"\u009f\u00a0\7]\2\2\u00a0$\3\2\2\2\u00a1\u00a2\7_\2\2\u00a2&\3\2\2\2\u00a3"+
		"\u00a4\7~\2\2\u00a4(\3\2\2\2\u00a5\u00a6\7.\2\2\u00a6*\3\2\2\2\u00a7\u00a8"+
		"\7<\2\2\u00a8,\3\2\2\2\u00a9\u00aa\7=\2\2\u00aa.\3\2\2\2\u00ab\u00ac\7"+
		"-\2\2\u00ac\60\3\2\2\2\u00ad\u00ae\7/\2\2\u00ae\62\3\2\2\2\u00af\u00b0"+
		"\7,\2\2\u00b0\64\3\2\2\2\u00b1\u00b2\7\61\2\2\u00b2\66\3\2\2\2\u00b3\u00b4"+
		"\7@\2\2\u00b48\3\2\2\2\u00b5\u00b6\7@\2\2\u00b6\u00b7\7?\2\2\u00b7:\3"+
		"\2\2\2\u00b8\u00b9\7>\2\2\u00b9<\3\2\2\2\u00ba\u00bb\7>\2\2\u00bb\u00bc"+
		"\7?\2\2\u00bc>\3\2\2\2\u00bd\u00be\7?\2\2\u00be\u00bf\7?\2\2\u00bf@\3"+
		"\2\2\2\u00c0\u00c1\7\61\2\2\u00c1\u00c2\7\61\2\2\u00c2\u00c6\3\2\2\2\u00c3"+
		"\u00c5\13\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c7\3"+
		"\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9"+
		"\u00ca\t\5\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\b!\2\2\u00ccB\3\2\2\2\u00cd"+
		"\u00cf\t\6\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00ce\3\2"+
		"\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b\"\2\2\u00d3"+
		"D\3\2\2\2\f\2tv}\177\u0086\u008d\u0093\u00c6\u00d0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}