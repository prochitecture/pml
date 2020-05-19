import re
from Dictionaries import Dictionaries

class PythonCoder():
    def __init__(self):
        self.dictionary = Dictionaries()
        self.code = ""
        self.elementCommaStack = []
        self.exprCommaStack = []
        self.alterCommaStack = []
        self.indents = 0
        self.context = ""

    def getCode(self):
        return self.code

    def indent(self):
        return (" "*4*self.indents)

    def write(self,text):
        self.code += text

    def literalize(self,text):
        literalized = re.sub('(" +")', ' ', re.sub('("")', '"', re.sub('([a-z\\-]+)', '"\\1"', text) ) )
        return literalized

    def enterStyle(self):
        self.write('[\n')
        self.indents += 1

    def exitStyle(self):
        self.indents -= 1
        self.write(']\n')

    def enterElements(self):
        self.elementCommaStack.append("")

    def exitElements(self):
        self.write("\n")
        self.indents -= 1
        self.elementCommaStack.pop()

    def enterElement_name(self,name):
        txt = name.capitalize()
        self.write(self.indent()+txt+'(\n')
        self.indents += 1

    def enterElement(self):
        self.write(self.elementCommaStack[-1])

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

    def enterAttributes(self):
        self.exprCommaStack.append("")

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
                self.write( "Value(FromAttr(" + attribute + ", " + types[0] + ')' )
            else:
                self.write('Value(Alternatives(\n')
                self.indents += 1
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[0] + '),\n' )
                self.write( self.indent()+"FromAttr(" + attribute + ", " + types[1] + ')\n' )
                self.indents -= 1
                self.write(self.indent()+'))')

    def enterCONST(self,text):
        expr = self.literalize(text)
        if self.context == "alternatives":
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Constant(" + expr + ')' )
        else:
            self.write('Value(Constant(' + expr + ')' )

    def enterRANDN(self,value):
        if self.context == "alternatives":
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomNormal( ' + value + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomNormal( ' + value + ' )')

    def enterRANDW(self,li):
        list = self.literalize(li)
        if self.context == "alternatives":
            self.write(self.alterCommaStack[-1])
            self.write(self.indent()+'RandomWeighted( ' + list + ' )')
            self.alterCommaStack[-1] = ",\n"
        else:
            self.write('Value(RandomWeighted( ' + list + ' )')

    def enterSimple_expr(self,text):
        expr = self.literalize(text)
        if self.context == "alternatives":
            self.write(self.alterCommaStack[-1])
            self.write( self.indent()+"Constant(" + expr + ')' )
        else:
            self.write(expr)
