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
		T__0=1, T__1=2, T__2=3, IDENTIFIER=4, STRING_LITERAL=5, NUMBER=6, FLOAT=7, 
		INT=8, STRUDEL=9, LCURLY=10, RCURLY=11, LPAREN=12, RPAREN=13, LBRACK=14, 
		RBRACK=15, PIPE=16, COMMA=17, COLON=18, SEMI=19, GT=20, GE=21, LT=22, 
		LE=23, EQ=24, COMMENT=25, WS=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "IDENTIFIER", "STRING_LITERAL", "NUMBER", "FLOAT", 
		"INT", "STRUDEL", "LCURLY", "RCURLY", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
		"PIPE", "COMMA", "COLON", "SEMI", "GT", "GE", "LT", "LE", "EQ", "COMMENT", 
		"WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'attr'", "'random_normal'", "'random_weighted'", null, null, null, 
		null, null, "'@'", "'{'", "'}'", "'('", "')'", "'['", "']'", "'|'", "','", 
		"':'", "';'", "'>'", "'>='", "'<'", "'<='", "'='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, "IDENTIFIER", "STRING_LITERAL", "NUMBER", "FLOAT", 
		"INT", "STRUDEL", "LCURLY", "RCURLY", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
		"PIPE", "COMMA", "COLON", "SEMI", "GT", "GE", "LT", "LE", "EQ", "COMMENT", 
		"WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34\u00b3\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5]\n\5\f\5\16\5`\13\5\3\6\3\6\3\6"+
		"\3\6\7\6f\n\6\f\6\16\6i\13\6\3\6\3\6\3\7\3\7\5\7o\n\7\3\b\3\b\3\b\7\b"+
		"t\n\b\f\b\16\bw\13\b\3\t\6\tz\n\t\r\t\16\t{\3\n\3\n\3\13\3\13\3\f\3\f"+
		"\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3"+
		"\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\32\3\32\7\32\u00a4\n\32\f\32\16\32\u00a7\13\32\3\32\3\32\3"+
		"\32\3\32\3\33\6\33\u00ae\n\33\r\33\16\33\u00af\3\33\3\33\3\u00a5\2\34"+
		"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20"+
		"\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\3\2\7\4\2C\\"+
		"c|\7\2//\62;C\\aac|\3\2$$\4\2\f\f\17\17\5\2\13\f\17\17\"\"\2\u00ba\2\3"+
		"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2"+
		"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31"+
		"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2"+
		"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2"+
		"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\3\67\3\2\2\2\5<\3\2\2\2\7J\3\2\2"+
		"\2\tZ\3\2\2\2\13a\3\2\2\2\rn\3\2\2\2\17p\3\2\2\2\21y\3\2\2\2\23}\3\2\2"+
		"\2\25\177\3\2\2\2\27\u0081\3\2\2\2\31\u0083\3\2\2\2\33\u0085\3\2\2\2\35"+
		"\u0087\3\2\2\2\37\u0089\3\2\2\2!\u008b\3\2\2\2#\u008d\3\2\2\2%\u008f\3"+
		"\2\2\2\'\u0091\3\2\2\2)\u0093\3\2\2\2+\u0095\3\2\2\2-\u0098\3\2\2\2/\u009a"+
		"\3\2\2\2\61\u009d\3\2\2\2\63\u009f\3\2\2\2\65\u00ad\3\2\2\2\678\7c\2\2"+
		"89\7v\2\29:\7v\2\2:;\7t\2\2;\4\3\2\2\2<=\7t\2\2=>\7c\2\2>?\7p\2\2?@\7"+
		"f\2\2@A\7q\2\2AB\7o\2\2BC\7a\2\2CD\7p\2\2DE\7q\2\2EF\7t\2\2FG\7o\2\2G"+
		"H\7c\2\2HI\7n\2\2I\6\3\2\2\2JK\7t\2\2KL\7c\2\2LM\7p\2\2MN\7f\2\2NO\7q"+
		"\2\2OP\7o\2\2PQ\7a\2\2QR\7y\2\2RS\7g\2\2ST\7k\2\2TU\7i\2\2UV\7j\2\2VW"+
		"\7v\2\2WX\7g\2\2XY\7f\2\2Y\b\3\2\2\2Z^\t\2\2\2[]\t\3\2\2\\[\3\2\2\2]`"+
		"\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\n\3\2\2\2`^\3\2\2\2ag\7$\2\2bc\7$\2\2c"+
		"f\7$\2\2df\n\4\2\2eb\3\2\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h"+
		"j\3\2\2\2ig\3\2\2\2jk\7$\2\2k\f\3\2\2\2lo\5\17\b\2mo\5\21\t\2nl\3\2\2"+
		"\2nm\3\2\2\2o\16\3\2\2\2pq\5\21\t\2qu\7\60\2\2rt\5\21\t\2sr\3\2\2\2tw"+
		"\3\2\2\2us\3\2\2\2uv\3\2\2\2v\20\3\2\2\2wu\3\2\2\2xz\4\62;\2yx\3\2\2\2"+
		"z{\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\22\3\2\2\2}~\7B\2\2~\24\3\2\2\2\177\u0080"+
		"\7}\2\2\u0080\26\3\2\2\2\u0081\u0082\7\177\2\2\u0082\30\3\2\2\2\u0083"+
		"\u0084\7*\2\2\u0084\32\3\2\2\2\u0085\u0086\7+\2\2\u0086\34\3\2\2\2\u0087"+
		"\u0088\7]\2\2\u0088\36\3\2\2\2\u0089\u008a\7_\2\2\u008a \3\2\2\2\u008b"+
		"\u008c\7~\2\2\u008c\"\3\2\2\2\u008d\u008e\7.\2\2\u008e$\3\2\2\2\u008f"+
		"\u0090\7<\2\2\u0090&\3\2\2\2\u0091\u0092\7=\2\2\u0092(\3\2\2\2\u0093\u0094"+
		"\7@\2\2\u0094*\3\2\2\2\u0095\u0096\7@\2\2\u0096\u0097\7?\2\2\u0097,\3"+
		"\2\2\2\u0098\u0099\7>\2\2\u0099.\3\2\2\2\u009a\u009b\7>\2\2\u009b\u009c"+
		"\7?\2\2\u009c\60\3\2\2\2\u009d\u009e\7?\2\2\u009e\62\3\2\2\2\u009f\u00a0"+
		"\7\61\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4\13\2\2"+
		"\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a5\u00a3"+
		"\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\t\5\2\2\u00a9"+
		"\u00aa\3\2\2\2\u00aa\u00ab\b\32\2\2\u00ab\64\3\2\2\2\u00ac\u00ae\t\6\2"+
		"\2\u00ad\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0"+
		"\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\b\33\2\2\u00b2\66\3\2\2\2\f\2"+
		"\\^egnu{\u00a5\u00af\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}