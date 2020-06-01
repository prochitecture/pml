import re
from Dictionaries import Dictionaries

class PythonCoder():
    def __init__(self):
        self.dictionary = Dictionaries()
        self.code = ""
        self.blockCommaStack = []
        self.elementCommaStack = []
        self.attribCommaStack = []
        self.alterCommaStack = []
        self.condCommaStack = []
        self.indents = 0
        self.smoothContext = False
        self.alternativesContext = False
        self.conditionContext = False
        self.conditionalContext = False

    def getCode(self):
        return self.code

    def indent(self):
        return (" "*4*self.indents)

    def write(self,text):
        self.code += text

    def literalize(self,text):
        literalized = re.sub('("[ _]+")', ' ', re.sub('("")', '"', re.sub('([a-zA-Z]+)', '"\\1"', text) ) )
        return literalized

    def toCamelCase(self,text):
        return ''.join([ x.capitalize() for x in text.split('_') ])

    # ------------------------------------------------------------
    # styles
    # : named_block+  EOF            #NAMED
    # | elements EOF                 #UNNAMED
    # ;
    # ------------------------------------------------------------

    def enterNAMED(self):
        self.indents = 1
        self.blockCommaStack.append('')
        self.write('styles = {\n' )

    def exitNAMED(self):
        self.blockCommaStack.pop()
        self.write('\n}')

    def enterUNNAMED(self):
        self.indents = 1
        self.write('styles = [' )

    def exitUNNAMED(self):
        self.write(']')

    # ------------------------------------------------------------
    # named_block
    #     : ('@name' STRING_LITERAL SEMI elements)
    #     ;
    # ------------------------------------------------------------

    def enterNamed_block(self,name):
        self.write(self.blockCommaStack[-1])
        self.write(self.indent()+name + ' : [')
        self.blockCommaStack[-1] = ',\n'
        self.indents += 1
    
    def exitNamed_block(self):
        self.write(self.indent()+']') 

    # ------------------------------------------------------------
    # elements
    #     : element ( element )* 
    #     ;
    # ------------------------------------------------------------

    def enterElements(self):
        self.elementCommaStack.append('\n')
        self.attribCommaStack.append("\n")

    def exitElements(self):
        self.write("\n")
        self.indents -= 1
        self.elementCommaStack.pop()

    # ------------------------------------------------------------
    # element 
    #     : '@'? element_name (STRUDEL def_name)? (LBRACK condition RBRACK)? LCURLY attributes RCURLY
    #     ;
    # ------------------------------------------------------------

    def enterElement_name(self,name):
        txt = self.toCamelCase(name)
        self.write(self.indent()+txt+'(')
        self.indents += 1

    def enterElement(self):
        self.write(self.elementCommaStack[-1])
        self.attribCommaStack.append("\n")  # maybe we have a condition first
 
    def exitElement(self):
        self.indents -=1
        self.write(self.indent()+')')
        self.elementCommaStack[-1] = ",\n"

    def enterCondition(self):
        self.conditionContext = True
        self.write(self.attribCommaStack[-1])
        self.write(self.indent()+'condition = lambda item : ' )
        self.attribCommaStack[-1] = ',\n'

    def exitCondition(self):
        self.conditionContext = False
        self.attribCommaStack[-1] = ',\n'


 
    # ------------------------------------------------------------
    # attributes
    #     : attribute*
    #     ;
    # ------------------------------------------------------------

    def enterAttributes(self):
        pass
 #      self.attribCommaStack.append("\n")

    def exitAttributes(self):
        self.write("\n")
        self.attribCommaStack.pop()

    # ------------------------------------------------------------
    # attribute 
    #     : 'symmetry' COLON sym_expression SEMI
    #     | 'use' COLON use_expression SEMI
    #     | ('faces' | 'sharpEdges') COLON smooth_expression SEMI
    #     | attr_name COLON expression SEMI
    #     | attr_name COLON markup_block  // markup
    #     ;
    # sym_expression
    #     : IDENTIFIER
    #     ;
    # use_expression
    #     : IDENTIFIER (COMMA IDENTIFIER)*
    #     ;
    # smooth_expression
    #     : expression
    #     ;
    # markup_block
    #     : LBRACK elements RBRACK
    #     ;
    # ------------------------------------------------------------

    def enterSym_expression(self,sym):
        self.write(self.attribCommaStack[-1])
        symmetry = self.toCamelCase(sym)
        self.write(self.indent()+'symmetry = symmetry.'+symmetry )
        self.attribCommaStack[-1] = ",\n"

    def enterUse_expression(self,expr):
        self.write(self.attribCommaStack[-1])
        expression = self.literalize(expr)
        self.write(self.indent()+'use = (' + expression + ',)' )
        self.attribCommaStack[-1] = ",\n"

    def enterSmooth_expression(self, name):
        self.smoothContext = True
        self.write(self.attribCommaStack[-1])
        self.write(self.indent() + name + ' = ' )
        self.attribCommaStack[-1] = ",\n"

    def exitSmooth_expression(self):
        self.smoothContext = False

    def enterMarkup_block(self):
        self.write(' [')
        self.indents += 1

    def exitMarkup_block(self):
        self.write(self.indent()+']')

    def enterAttr_name(self,name):
        self.write(self.attribCommaStack[-1])
        self.write(self.indent()+name+' = ')
        self.attribCommaStack[-1] = ",\n"

    # ------------------------------------------------------------
    # expression
    #     :  simple_expr | function | alternatives
    #     ;
    # alternatives
    #     : function (PIPE function)+
    #     ;
    # ------------------------------------------------------------

    def enterAlternatives(self):
        self.alternativesContext = True
        # self.inFunctionStack.append('inFunction')
        self.functionContext = True
        self.write("Value(Alternatives(\n")
        self.alterCommaStack.append("")
        self.indents +=1

    def exitAlternatives(self):
        self.alternativesContext = False
        self.alterCommaStack.pop()
        self.indents -=1
        self.write('\n'+self.indent()+'))')

    # ------------------------------------------------------------
    # function
    #     : 'attr' LPAREN string_literal RPAREN           #ATTR
    #     | 'random_normal' LPAREN NUMBER RPAREN          #RANDN
    #     | 'random_weighted' nested_list                 #RANDW
    #     | 'if' LPAREN conditional RPAREN function       #COND
    #     | 'use_from' LPAREN IDENTIFIER RPAREN           #USEFROM
    #     | 'per_building' LPAREN function RPAREN         #PERBUILD
    #     | constant                                      #CONST
    #     | nested_list                                   #NESTED
    #     | arith_atom                                    #ARITH
    #     ;
    # ------------------------------------------------------------

    def enterATTR(self,attribute):
        types = self.dictionary.getAttributeTypes(attribute)
        if self.alternativesContext:
            self.write(self.alterCommaStack[-1])
            if len(types) == 1:
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[0] + ')' )
            else:
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[0] + '),\n' )
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[1] + ')' )
            self.alterCommaStack[-1] = ",\n"
        else:
            if len(types) == 1:
                self.write( "Value(FromAttr(" + attribute + ", " + types[0] + '))' )
            else:
                self.write('Value(Alternatives(\n')
                self.indents += 1
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[0] + '),\n' )
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[1] + ')\n' )
                self.indents -= 1
                self.write(self.indent()+'))')

    # ------------------------------------------------------------
    # function
    #     : ...
    #     | 'random_normal' LPAREN NUMBER RPAREN          #RANDN
    #     | 'random_weighted' nested_list                 #RANDW
    #     | ...
    # ------------------------------------------------------------

    def enterRANDN(self,value):
        if self.alternativesContext or self.conditionContext:
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomNormal( ' + value + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomNormal( ' + value + ' ))')

    def enterRANDW(self,li):
        list = self.literalize(li)
        if self.alternativesContext or self.conditionContext:
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomWeighted( ' + list + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomWeighted( ' + list + ' ))')

    # ------------------------------------------------------------
    # function
    #     : ...
    #     | 'if' LPAREN conditional RPAREN function       #COND
    #     | ...
    # ------------------------------------------------------------

    def enterCOND(self, condition, result):
        self.conditionContext = True
        self.conditionalContext = True
        if self.alternativesContext:
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Conditional(\n" )
            self.indents += 1
            self.write(self.indent()+'lambda item: ' ) 
            self.alterCommaStack.append(',\n')
        else:
            self.write( "Value(Conditional(\n" )
            self.indents += 1
            self.write(self.indent()+'lambda item: ' ) 

    def exitCOND(self):
        self.indents -= 1
        self.write("\n")
        if self.conditionContext:
            if self.alternativesContext:
                self.write(self.indent()+")" )
            else:
                self.write(self.indent()+"))" )
        else:
            self.write(self.indent()+")" )
        self.conditionContext = False
        self.conditionalContext = False

    # ------------------------------------------------------------
    # function
    #     : ...
    #     | 'use_from' LPAREN IDENTIFIER RPAREN           #USEFROM
    #     | 'per_building' LPAREN function RPAREN         #PERBUILD
    #     | ...
    # ------------------------------------------------------------

    def enterUSEFROM(self,ident):
        self.write('useFrom("' + ident + '")')

    def enterPERBUILD(self):
        self.write('PerBuilding(')

    def exitPERBUILD(self):
        self.write(')')

    # ------------------------------------------------------------
    # function
    #     : ...
    #     | constant                                      #CONST
    #     | nested_list                                   #NESTED
    #     | ...
    # ------------------------------------------------------------

    def enterCONST(self,text):
        if self.conditionalContext:
            self.write(',\n')
            if self.smoothContext and text in ('smooth','flat','horizontal','side','all'):
                expr = self.toCamelCase(text)
                self.write( self.indent()+"Constant(smoothness." + expr + ')' )
            else:
                expr = self.literalize(text)
                self.write( self.indent()+"Constant(" + expr + ')' )
        elif self.alternativesContext: 
            self.write(self.alterCommaStack[-1])
            expr = self.literalize(text)
            self.write( self.indent()+"Constant(" + expr + ')' )
            self.alterCommaStack[-1] = ',\n'
        else:
            expr = self.literalize(text)
            self.write('Value(Constant(' + expr + ')' )

    def enterNESTED(self, li):
        list = self.literalize(li)
        self.write( list )

    def exitINNESTED(self,li):
        list = self.literalize(li)
        self.write( list )
    # ------------------------------------------------------------
    # arith_atom
    #     : 'item' '.' IDENTIFIER                                 # ATOM_SINGLE
    #     | 'item' '.' IDENTIFIER '.' IDENTIFIER                  # ATOM_SINGLE
    #     | 'item' '.' IDENTIFIER LBRACK STRING_LITERAL RBRACK    # ATOM_FROMATTR
    #     | 'item' LBRACK STRING_LITERAL RBRACK                   # ATOM_FROMATTR_SHORT
    #     | identifier                                            # ATOM_IDENT
    #     | NUMBER                                                # ATOM_IDENT
    #     | STRING_LITERAL                                        # ATOM_IDENT
    # ------------------------------------------------------------

    def enterATOM_SINGLE(self,atom):
        self.write(atom)

    def enterATOM_FROMATTR(self,ident,literal):
        if self.conditionContext or self.conditionalContext:
            self.write( 'item.' + ident +'.getStyleBlockAttr(' + literal + ')' )
        else:
#            self.write(self.alterCommaStack[-1])
            identifier = ident.capitalize()
            self.write(self.indent()+"FromStyleBlockAttr("+literal+",FromStyleBlockAttr."+identifier+")")
 #           self.alterCommaStack[-1] = ",\n"

    def enterATOM_FROMATTR_SHORT(self,literal):
        if self.conditionContext:
            self.write( 'item.getStyleBlockAttr(' + literal + ')' )
        else:
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+"FromStyleBlockAttr("+literal+")")
            self.alterCommaStack[-1] = ",\n"

    def enterATOM_IDENT(self,ident):
        self.write(ident)

    def enterConst_atom(self,atom):
        const = self.literalize(atom)
        self.write( ',\n'+self.indent()+"Constant(" + const + ')' )

    # ------------------------------------------------------------
    #   ... and all the remaining details
    # ------------------------------------------------------------
    def enterDef_name(self,definition):
        self.write(self.attribCommaStack[-1])
        self.write(self.indent()+'defName = "' + definition + '"' )
        self.attribCommaStack[-1] = ",\n"

    def enterSimple_expr(self,text):
        if self.smoothContext:
            return
        if text in ('true','false'):
            expr = text.capitalize()
        else:
            expr = self.literalize(text)
        if self.alternativesContext or self.conditionalContext: # ???or self.context  in ( "conditional" ):
            # self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Constant(" + expr + ')' )
        else:
            self.write(expr)

    def enterAri_lparen(self):
        self.write( ' (' ) 

    def enterAri_rparen(self):
        self.write( ') ' ) 

    def enterIdentifier(self, ident):
        if self.smoothContext and ident in ('smooth','flat','horizontal','side','all') :
            self.write('smoothness.' + ident )

    def enterInop(self,op):
        self.write( ' '+op+' ' )

    def enterRelop(self,op):
        self.write( ' '+op+' ' )

    def enterLogicop(self,op):
        self.write( ' '+op+' ' )

    def enterNotop(self,op):
        self.write( ' '+op+' ' )

    def enterArith_op(self,op):
        self.write( ' '+op+' ' )
