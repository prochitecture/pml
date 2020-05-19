// This is a grammar fragment for PML style language
// Version 02


grammar pml;

style
    : LBRACK elements RBRACK
    ;

elements
    : element ( COMMA element )*
    ;

element // for instance Footprint
    : element_name LCURLY attributes RCURLY
    ;

attributes
    : attribute*
    ;

attribute // for instance 'roofShape: "gabled";
    : attr_name COLON expression SEMI
    ;

expression
    : simple_expr | function | alternatives
    ;

alternatives
    : function (PIPE function)+
    ;

function
    : 'attr' LPAREN string_literal RPAREN           #ATTR
    | 'random_normal' LPAREN NUMBER RPAREN          #RANDN
    | 'random_weighted' LPAREN nested_list RPAREN   #RANDW
    | constant                                      #CONST
    ;

nested_list
    : LPAREN (STRING_LITERAL | NUMBER | IDENTIFIER) (COMMA (STRING_LITERAL | NUMBER  | IDENTIFIER))+ RPAREN
    | NUMBER
    | LPAREN nested_list (COMMA nested_list)+ RPAREN
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

number
    : NUMBER
    ; 

string_literal
    : STRING_LITERAL
    ;

// Lexer rules
// -------------------------------------

IDENTIFIER
    : [a-zA-Z]([a-zA-Z0-9_]|'-')*  //[a-zA-Z][a-zA-Z0-9_]*
    ;

STRING_LITERAL
    : '"' ('""' | ~ ('"'))* '"'
    ;

NUMBER
    : FLOAT
    | INT
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

GT         : '>' ;
GE         : '>=' ;
LT         : '<' ;
LE         : '<=' ;
EQ         : '=' ;



//Boolean  operators
//NOT:        'not';
//OR:         'or';
//AND:        'and';


COMMENT
   :'//' .*? [\r\n] -> skip 
   ;  

WS : [ \t\r\n]+ -> skip ;
