// Generated from d:\PML\pml\PML2PythonTranslator-Dev-I\pml_grammar\pml.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pmlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, IDENTIFIER=4, STRING_LITERAL=5, NUMBER=6, FLOAT=7, 
		INT=8, STRUDEL=9, LCURLY=10, RCURLY=11, LPAREN=12, RPAREN=13, LBRACK=14, 
		RBRACK=15, PIPE=16, COMMA=17, COLON=18, SEMI=19, GT=20, GE=21, LT=22, 
		LE=23, EQ=24, COMMENT=25, WS=26;
	public static final int
		RULE_style = 0, RULE_elements = 1, RULE_element = 2, RULE_attributes = 3, 
		RULE_attribute = 4, RULE_expression = 5, RULE_alternatives = 6, RULE_function = 7, 
		RULE_nested_list = 8, RULE_constant = 9, RULE_simple_expr = 10, RULE_element_name = 11, 
		RULE_attr_name = 12, RULE_number = 13, RULE_string_literal = 14;
	public static final String[] ruleNames = {
		"style", "elements", "element", "attributes", "attribute", "expression", 
		"alternatives", "function", "nested_list", "constant", "simple_expr", 
		"element_name", "attr_name", "number", "string_literal"
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

	@Override
	public String getGrammarFileName() { return "pml.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pmlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StyleContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(pmlParser.LBRACK, 0); }
		public ElementsContext elements() {
			return getRuleContext(ElementsContext.class,0);
		}
		public TerminalNode RBRACK() { return getToken(pmlParser.RBRACK, 0); }
		public StyleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_style; }
	}

	public final StyleContext style() throws RecognitionException {
		StyleContext _localctx = new StyleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_style);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(LBRACK);
			setState(31);
			elements();
			setState(32);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementsContext extends ParserRuleContext {
		public List<ElementContext> element() {
			return getRuleContexts(ElementContext.class);
		}
		public ElementContext element(int i) {
			return getRuleContext(ElementContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(pmlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(pmlParser.COMMA, i);
		}
		public ElementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elements; }
	}

	public final ElementsContext elements() throws RecognitionException {
		ElementsContext _localctx = new ElementsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_elements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			element();
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(35);
				match(COMMA);
				setState(36);
				element();
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementContext extends ParserRuleContext {
		public Element_nameContext element_name() {
			return getRuleContext(Element_nameContext.class,0);
		}
		public TerminalNode LCURLY() { return getToken(pmlParser.LCURLY, 0); }
		public AttributesContext attributes() {
			return getRuleContext(AttributesContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(pmlParser.RCURLY, 0); }
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_element);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			element_name();
			setState(43);
			match(LCURLY);
			setState(44);
			attributes();
			setState(45);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttributesContext extends ParserRuleContext {
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public AttributesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributes; }
	}

	public final AttributesContext attributes() throws RecognitionException {
		AttributesContext _localctx = new AttributesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_attributes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(47);
				attribute();
				}
				}
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttributeContext extends ParserRuleContext {
		public Attr_nameContext attr_name() {
			return getRuleContext(Attr_nameContext.class,0);
		}
		public TerminalNode COLON() { return getToken(pmlParser.COLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(pmlParser.SEMI, 0); }
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_attribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			attr_name();
			setState(54);
			match(COLON);
			setState(55);
			expression();
			setState(56);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Simple_exprContext simple_expr() {
			return getRuleContext(Simple_exprContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public AlternativesContext alternatives() {
			return getRuleContext(AlternativesContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expression);
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(58);
				simple_expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				function();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				alternatives();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AlternativesContext extends ParserRuleContext {
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<TerminalNode> PIPE() { return getTokens(pmlParser.PIPE); }
		public TerminalNode PIPE(int i) {
			return getToken(pmlParser.PIPE, i);
		}
		public AlternativesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alternatives; }
	}

	public final AlternativesContext alternatives() throws RecognitionException {
		AlternativesContext _localctx = new AlternativesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_alternatives);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			function();
			setState(66); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(64);
				match(PIPE);
				setState(65);
				function();
				}
				}
				setState(68); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PIPE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	 
		public FunctionContext() { }
		public void copyFrom(FunctionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RANDWContext extends FunctionContext {
		public TerminalNode LPAREN() { return getToken(pmlParser.LPAREN, 0); }
		public Nested_listContext nested_list() {
			return getRuleContext(Nested_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(pmlParser.RPAREN, 0); }
		public RANDWContext(FunctionContext ctx) { copyFrom(ctx); }
	}
	public static class CONSTContext extends FunctionContext {
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public CONSTContext(FunctionContext ctx) { copyFrom(ctx); }
	}
	public static class RANDNContext extends FunctionContext {
		public TerminalNode LPAREN() { return getToken(pmlParser.LPAREN, 0); }
		public TerminalNode NUMBER() { return getToken(pmlParser.NUMBER, 0); }
		public TerminalNode RPAREN() { return getToken(pmlParser.RPAREN, 0); }
		public RANDNContext(FunctionContext ctx) { copyFrom(ctx); }
	}
	public static class ATTRContext extends FunctionContext {
		public TerminalNode LPAREN() { return getToken(pmlParser.LPAREN, 0); }
		public String_literalContext string_literal() {
			return getRuleContext(String_literalContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(pmlParser.RPAREN, 0); }
		public ATTRContext(FunctionContext ctx) { copyFrom(ctx); }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new ATTRContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				match(T__0);
				setState(71);
				match(LPAREN);
				setState(72);
				string_literal();
				setState(73);
				match(RPAREN);
				}
				break;
			case T__1:
				_localctx = new RANDNContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				match(T__1);
				setState(76);
				match(LPAREN);
				setState(77);
				match(NUMBER);
				setState(78);
				match(RPAREN);
				}
				break;
			case T__2:
				_localctx = new RANDWContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				match(T__2);
				setState(80);
				match(LPAREN);
				setState(81);
				nested_list();
				setState(82);
				match(RPAREN);
				}
				break;
			case IDENTIFIER:
			case STRING_LITERAL:
			case NUMBER:
				_localctx = new CONSTContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(84);
				constant();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Nested_listContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(pmlParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(pmlParser.RPAREN, 0); }
		public List<TerminalNode> STRING_LITERAL() { return getTokens(pmlParser.STRING_LITERAL); }
		public TerminalNode STRING_LITERAL(int i) {
			return getToken(pmlParser.STRING_LITERAL, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(pmlParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(pmlParser.NUMBER, i);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(pmlParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(pmlParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(pmlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(pmlParser.COMMA, i);
		}
		public List<Nested_listContext> nested_list() {
			return getRuleContexts(Nested_listContext.class);
		}
		public Nested_listContext nested_list(int i) {
			return getRuleContext(Nested_listContext.class,i);
		}
		public Nested_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nested_list; }
	}

	public final Nested_listContext nested_list() throws RecognitionException {
		Nested_listContext _localctx = new Nested_listContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_nested_list);
		int _la;
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				match(LPAREN);
				setState(88);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << STRING_LITERAL) | (1L << NUMBER))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(91); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(89);
					match(COMMA);
					setState(90);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << STRING_LITERAL) | (1L << NUMBER))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					setState(93); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==COMMA );
				setState(95);
				match(RPAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(96);
				match(NUMBER);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				match(LPAREN);
				setState(98);
				nested_list();
				setState(101); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(99);
					match(COMMA);
					setState(100);
					nested_list();
					}
					}
					setState(103); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==COMMA );
				setState(105);
				match(RPAREN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(pmlParser.STRING_LITERAL, 0); }
		public TerminalNode NUMBER() { return getToken(pmlParser.NUMBER, 0); }
		public TerminalNode IDENTIFIER() { return getToken(pmlParser.IDENTIFIER, 0); }
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << STRING_LITERAL) | (1L << NUMBER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_exprContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(pmlParser.IDENTIFIER, 0); }
		public TerminalNode NUMBER() { return getToken(pmlParser.NUMBER, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(pmlParser.STRING_LITERAL, 0); }
		public Simple_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_expr; }
	}

	public final Simple_exprContext simple_expr() throws RecognitionException {
		Simple_exprContext _localctx = new Simple_exprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_simple_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << STRING_LITERAL) | (1L << NUMBER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(pmlParser.IDENTIFIER, 0); }
		public Element_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_name; }
	}

	public final Element_nameContext element_name() throws RecognitionException {
		Element_nameContext _localctx = new Element_nameContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_element_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attr_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(pmlParser.IDENTIFIER, 0); }
		public Attr_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_name; }
	}

	public final Attr_nameContext attr_name() throws RecognitionException {
		Attr_nameContext _localctx = new Attr_nameContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_attr_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(pmlParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class String_literalContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(pmlParser.STRING_LITERAL, 0); }
		public String_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_literal; }
	}

	public final String_literalContext string_literal() throws RecognitionException {
		String_literalContext _localctx = new String_literalContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_string_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(STRING_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34|\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\7\3(\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\5\7\5\63\n\5\f\5\16\5"+
		"\66\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7@\n\7\3\b\3\b\3\b\6\bE\n\b"+
		"\r\b\16\bF\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\5\tX\n\t\3\n\3\n\3\n\3\n\6\n^\n\n\r\n\16\n_\3\n\3\n\3\n\3\n\3\n\3\n\6"+
		"\nh\n\n\r\n\16\ni\3\n\3\n\5\nn\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16"+
		"\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		"\2\3\3\2\6\b\2x\2 \3\2\2\2\4$\3\2\2\2\6,\3\2\2\2\b\64\3\2\2\2\n\67\3\2"+
		"\2\2\f?\3\2\2\2\16A\3\2\2\2\20W\3\2\2\2\22m\3\2\2\2\24o\3\2\2\2\26q\3"+
		"\2\2\2\30s\3\2\2\2\32u\3\2\2\2\34w\3\2\2\2\36y\3\2\2\2 !\7\20\2\2!\"\5"+
		"\4\3\2\"#\7\21\2\2#\3\3\2\2\2$)\5\6\4\2%&\7\23\2\2&(\5\6\4\2\'%\3\2\2"+
		"\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5\3\2\2\2+)\3\2\2\2,-\5\30\r\2-.\7"+
		"\f\2\2./\5\b\5\2/\60\7\r\2\2\60\7\3\2\2\2\61\63\5\n\6\2\62\61\3\2\2\2"+
		"\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\64\3\2\2\2"+
		"\678\5\32\16\289\7\24\2\29:\5\f\7\2:;\7\25\2\2;\13\3\2\2\2<@\5\26\f\2"+
		"=@\5\20\t\2>@\5\16\b\2?<\3\2\2\2?=\3\2\2\2?>\3\2\2\2@\r\3\2\2\2AD\5\20"+
		"\t\2BC\7\22\2\2CE\5\20\t\2DB\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\17"+
		"\3\2\2\2HI\7\3\2\2IJ\7\16\2\2JK\5\36\20\2KL\7\17\2\2LX\3\2\2\2MN\7\4\2"+
		"\2NO\7\16\2\2OP\7\b\2\2PX\7\17\2\2QR\7\5\2\2RS\7\16\2\2ST\5\22\n\2TU\7"+
		"\17\2\2UX\3\2\2\2VX\5\24\13\2WH\3\2\2\2WM\3\2\2\2WQ\3\2\2\2WV\3\2\2\2"+
		"X\21\3\2\2\2YZ\7\16\2\2Z]\t\2\2\2[\\\7\23\2\2\\^\t\2\2\2][\3\2\2\2^_\3"+
		"\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2an\7\17\2\2bn\7\b\2\2cd\7\16\2\2d"+
		"g\5\22\n\2ef\7\23\2\2fh\5\22\n\2ge\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2"+
		"\2jk\3\2\2\2kl\7\17\2\2ln\3\2\2\2mY\3\2\2\2mb\3\2\2\2mc\3\2\2\2n\23\3"+
		"\2\2\2op\t\2\2\2p\25\3\2\2\2qr\t\2\2\2r\27\3\2\2\2st\7\6\2\2t\31\3\2\2"+
		"\2uv\7\6\2\2v\33\3\2\2\2wx\7\b\2\2x\35\3\2\2\2yz\7\7\2\2z\37\3\2\2\2\n"+
		")\64?FW_im";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}