import re
from Dictionaries import Dictionaries

class PythonCoder():
    def __init__(self):
        self.dictionary = Dictionaries()
        self.code = ""
        self.elementCommaStack = []
        self.exprCommaStack = []
        self.alterCommaStack = []
        self.condCommaStack = []
        self.indents = 0
        self.context = ""

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
        return ''.join([ x.capitalize() for x in text.split('-') ])

    def enterNAMED(self):
        self.indents = 1
        self.write('styles = {\n' )

    def exitNAMED(self):
        self.write('\n}')

    def enterUNNAMED(self):
        self.indents = 1
        self.write('styles = [\n' )

    def exitUNNAMED(self):
        self.write(']')

    def enterNamed_block(self,name):
        self.write(self.indent()+name + ' : [\n')
        self.indents += 1

    def exitNamed_block(self):
        self.indents -= 1
        self.write('\n'+self.indent()+']')


    def enterStyles(self):
        self.write('styles = {\n' )
        self.indents += 1

    def exitStyles(self):
        self.write('\n]')

    def enterStyle_block(self, style):
        self.write(self.indent()+style + ' : [\n')
        self.indents += 1

    def enterSym_expression(self,sym):
        self.write(self.exprCommaStack[-1])
        symmetry = self.toCamelCase(sym)
        self.write(self.indent()+'symmetry = symmetry.'+symmetry )
        self.exprCommaStack[-1] = ",\n"

    def enterUse_expression(self,expr):
        self.write(self.exprCommaStack[-1])
        expression = self.literalize(expr)
        self.write(self.indent()+'use = (' + expression + ',)' )
        self.exprCommaStack[-1] = ",\n"

    def enterSmooth_expression(self, name, expr):
        self.write(self.exprCommaStack[-1])
        expression = expr.capitalize()
        self.write(self.indent()+name+' = smoothness.' + expression )
        self.exprCommaStack[-1] = ",\n"

    def enterMarkup_block(self):
        self.write(' [\n')
        self.indents += 1

    def exitMarkup_block(self):
        self.write(self.indent()+']')

    def exitStyle_block(self):
        self.write(self.indent()+']')

    def enterElements(self):
        self.elementCommaStack.append("")

    def exitElements(self):
        self.write("\n")
        self.indents -= 1
        self.elementCommaStack.pop()

    def enterElement_name(self,name):
        txt = self.toCamelCase(name)
        self.write(self.indent()+txt+'(\n')
        self.indents += 1

    def enterElement(self):
        self.write(self.elementCommaStack[-1])
        self.exprCommaStack.append("")

    def exitElement(self):
        self.indents -=1
        self.write(self.indent()+')')
        self.elementCommaStack[-1] = ",\n"

    def enterAlternatives(self):
        self.context = "alternatives"
        self.write("Value(Alternatives(\n")
        self.alterCommaStack.append("")
        self.indents +=1

    def exitAlternatives(self):
        self.alterCommaStack.pop()
        self.context = ""
        self.indents -=1
        self.write('\n'+self.indent()+'))')

    def exitAttributes(self):
        self.write("\n")
        self.exprCommaStack.pop()

    def enterAttr_name(self,name):
        self.write(self.exprCommaStack[-1])
        self.write(self.indent()+name+' = ')
        self.exprCommaStack[-1] = ",\n"

    def enterATTR(self,attribute):
        types = self.dictionary.getAttributeTypes(attribute)
        if self.context == "alternatives":
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

    def enterCOND(self, condition, result):
        if self.context == "alternatives":
            self.context = "conditional"
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Conditional(\n" )
            self.indents += 1
            self.write(self.indent()+'lambda item: ' ) 

    def exitCOND(self):
        self.context = "alternatives"
        self.indents -= 1
        self.write("\n")
        self.write(self.indent()+")" )

    def enterUSEFROM(self,ident):
        self.write('useFrom("' + ident + '")')

    def enterPERBUILD(self):
        self.write('PerBuilding(')

    def exitPERBUILD(self):
        self.write(')')

    def enterNESTED(self, li):
        list = self.literalize(li)
        self.write( list )

    def enterCONST(self,text):
        expr = self.literalize(text)
        if self.context  in ( "alternatives", "conditional" ):
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Constant(" + expr + ')' )
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(Constant(' + expr + ')' )

    def enterRANDN(self,value):
        if self.context  in ( "alternatives", "conditional" ):
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomNormal( ' + value + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomNormal( ' + value + ' ))')

    def enterRANDW(self,li):
        list = self.literalize(li)
        if self.context in ( "alternatives", "conditional" ):
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomWeighted( ' + list + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomWeighted( ' + list + ' ))')

    def enterCondition(self, condition):
        self.write(self.exprCommaStack[-1])
        self.write(self.indent()+'condition = lambda item: ' )
        self.exprCommaStack[-1] = ",\n"

    def enterATOM_SINGLE(self,atom):
        self.write(atom)

    def enterATOM_FROMATTR(self,ident,literal):
        if self.context == "conditional":
            self.write( 'item.' + ident +'.getStyleBlockAttr(' + literal + ')' )
        else:
            self.write(self.alterCommaStack[-1])
            identifier = ident.capitalize()
            self.write(self.indent()+"FromStyleBlockAttr("+literal+",FromStyleBlockAttr."+identifier+")")
            self.alterCommaStack[-1] = ",\n"

    def enterATOM_FROMATTR_SHORT(self,literal):
        if self.context == "conditional":
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

    def enterDef_name(self,definition):
        self.write(self.exprCommaStack[-1])
        self.write(self.indent()+'defName = "' + definition + '"' )
        self.exprCommaStack[-1] = ",\n"

    def enterSimple_expr(self,text):
        if text in ('true','false'):
            expr = text.capitalize()
        else:
            expr = self.literalize(text)
        if self.context in ( "alternatives", "conditional" ):
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Constant(" + expr + ')' )
        else:
            self.write(expr)

    def enterAri_lparen(self):
        self.write( ' (' ) 

    def enterAri_rparen(self):
        self.write( ') ' ) 

    def enterRelop(self,op):
        self.write( ' '+op+' ' )

    def enterLogicop(self,op):
        self.write( ' '+op+' ' )

    def enterNotop(self,op):
        self.write( ' '+op+' ' )

    def enterArith_op(self,op):
        self.write( ' '+op+' ' )
