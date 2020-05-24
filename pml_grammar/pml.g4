// This is a grammar fragment for PML style language
// Version 03

grammar pml;

styles
    : named_block+              #NAMED
    | elements                  #UNNAMED
    ;

named_block
    : ('@name' STRING_LITERAL SEMI elements)
    ;

elements
    : element ( element )* 
    ;

element 
    : element_name (STRUDEL def_name)? (LBRACK condition RBRACK)? LCURLY attributes RCURLY
    ;

attributes
    : attribute*
    ;

attribute 
    : 'symmetry' COLON sym_expression SEMI
    | 'use' COLON use_expression SEMI
    | ('faces' | 'sharpEdges') COLON smooth_expression SEMI
    | attr_name COLON expression SEMI
    | attr_name COLON markup_block  // markup
    ;

sym_expression
    : IDENTIFIER
    ;

use_expression
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

smooth_expression
    : IDENTIFIER
    ;

markup_block
    : LBRACK elements RBRACK
    ;

expression
    :  simple_expr | function | alternatives
    ;

alternatives
    : function (PIPE function)+
    ;

function
    : 'attr' LPAREN string_literal RPAREN           #ATTR
    | 'random_normal' LPAREN NUMBER RPAREN          #RANDN
    | 'random_weighted' LPAREN nested_list RPAREN   #RANDW
    | 'if' LPAREN conditional RPAREN const_atom     #COND
    | 'use_from' LPAREN IDENTIFIER RPAREN           #USEFROM
    | 'per_building' LPAREN function RPAREN         #PERBUILD
    | constant                                      #CONST
    | nested_list                                   #NESTED
    | arith_atom                                    #ARITH
    ;

nested_list
    : LPAREN (STRING_LITERAL | NUMBER | IDENTIFIER) (COMMA (STRING_LITERAL | NUMBER  | IDENTIFIER))+ RPAREN
    | NUMBER
    | LPAREN nested_list (COMMA nested_list)+ RPAREN
   ;

def_name
    : IDENTIFIER
    ;

conditional
    : arith_expr 
    | arith_expr relop arith_expr
    ;

condition
    : arith_expr 
    | arith_expr relop arith_expr
    ;

arith_expr
    : arith_atom
    | arith_expr arith_op arith_expr
    ;

arith_atom
    : 'item' '.' IDENTIFIER                                 # ATOM_SINGLE
    | 'item' '.' IDENTIFIER '.' IDENTIFIER                  # ATOM_SINGLE
    | 'item' '.' IDENTIFIER LBRACK STRING_LITERAL RBRACK    # ATOM_FROMATTR
    | IDENTIFIER                                            # ATOM_IDENT
    | NUMBER                                                # ATOM_IDENT
    | STRING_LITERAL                                        # ATOM_IDENT
    ;

const_atom
    : STRING_LITERAL | NUMBER | IDENTIFIER
    ;

constant
    : STRING_LITERAL | NUMBER | IDENTIFIER
    ;

simple_expr
    : IDENTIFIER
    | NUMBER
    | STRING_LITERAL
    ; 
 
element_name
    : IDENTIFIER
    ;      

attr_name
    : IDENTIFIER
    ;      

relop
    : GT | GE | LT | LE | EQ
    ;

arith_op
    : PLUS | MINUS | TIMES | DIV
    ;

number
    : NUMBER
    ; 

string_literal
    : STRING_LITERAL
    ;

// Lexer rules
// -------------------------------------

IDENTIFIER
    : [a-zA-Z]([a-zA-Z0-9_]|'-')*
    ;

STRING_LITERAL
    : '"' ('""' | ~ ('"'))* '"'
    ;

NUMBER
    : '-'? FLOAT
    | '-'? INT
    ; 

FLOAT
    : INT '.' INT*
    ;

INT
    : ('0' .. '9')+
    ;

STRUDEL:    '@';
LCURLY:     '{';
RCURLY:     '}';
LPAREN:     '(' ;
RPAREN:     ')' ;
LBRACK:     '[';
RBRACK:     ']';
PIPE:       '|';
COMMA:      ',' ;
COLON:      ':'; 
SEMI:       ';'; 

PLUS        : '+';
MINUS       : '-';
TIMES       : '*';
DIV         : '/';

GT         : '>' ;
GE         : '>=' ;
LT         : '<' ;
LE         : '<=' ;
EQ         : '==' ;

COMMENT
   :'//' .*? [\r\n] -> skip 
   ;  

WS : [ \t\r\n]+ -> skip ;
