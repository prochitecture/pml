from pml_grammar.pmlListener import pmlListener
from pml_grammar.pmlParser import pmlParser
from PythonCoder import PythonCoder

class PythonListener(pmlListener):
    def __init__(self):
        self.coder = PythonCoder()

    def getCode(self):
        return self.coder.getCode()

    # Enter a parse tree produced by pmlParser#style_list.
    def enterStyle(self, ctx:pmlParser.StyleContext):
        self.coder.enterStyle()

    # Exit a parse tree produced by pmlParser#style_list.
    def exitStyle(self, ctx:pmlParser.StyleContext):
        self.coder.exitStyle()

     # Enter a parse tree produced by pmlParser#elements.
    def enterElements(self, ctx:pmlParser.ElementsContext):
        self.coder.enterElements()

    # Exit a parse tree produced by pmlParser#elements.
    def exitElements(self, ctx:pmlParser.ElementsContext):
        self.coder.exitElements()

   # Enter a parse tree produced by pmlParser#element_name.
    def enterElement_name(self, ctx:pmlParser.Element_nameContext):
        self.coder.enterElement_name(ctx.getText())

    # Enter a parse tree produced by pmlParser#style_block.
    def enterElement(self, ctx:pmlParser.ElementContext):
        self.coder.enterElement()

    # Exit a parse tree produced by pmlParser#style_block.
    def exitElement(self, ctx:pmlParser.ElementContext):
        self.coder.exitElement()

    # Enter a parse tree produced by pmlParser#alternatives.
    def enterAlternatives(self, ctx:pmlParser.AlternativesContext):
        self.coder.enterAlternatives()

    # Exit a parse tree produced by pmlParser#alternatives.
    def exitAlternatives(self, ctx:pmlParser.AlternativesContext):
        self.coder.exitAlternatives()

    # Enter a parse tree produced by pmlParser#attributes.
    def enterAttributes(self, ctx:pmlParser.AttributesContext):
       self.coder.enterAttributes()

    # Enter a parse tree produced by pmlParser#ATTR.
    def enterATTR(self, ctx:pmlParser.ATTRContext):
        self.coder.enterATTR(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#attributes.
    def exitAttributes(self, ctx:pmlParser.AttributesContext):
        self.coder.exitAttributes()
        
    # Enter a parse tree produced by pmlParser#RANDN.
    def enterRANDN(self, ctx:pmlParser.RANDNContext):
        self.coder.enterRANDN(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#RANDW.
    def enterRANDW(self, ctx:pmlParser.RANDWContext):
        self.coder.enterRANDW(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#attr_name.
    def enterAttr_name(self, ctx:pmlParser.Attr_nameContext):
        self.coder.enterAttr_name(ctx.getText())

    # Enter a parse tree produced by pmlParser#CONST.
    def enterCONST(self, ctx:pmlParser.CONSTContext):
        self.coder.enterCONST(ctx.getChild(0).getText())

    # Enter a parse tree produced by pmlParser#simple_expr.
    def enterSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        self.coder.enterSimple_expr(ctx.getText())

