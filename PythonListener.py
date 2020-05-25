from pml_grammar.pmlListener import pmlListener
from pml_grammar.pmlParser import pmlParser
from PythonCoder import PythonCoder

class PythonListener(pmlListener):
    def __init__(self):
        self.coder = PythonCoder()

    def getCode(self):
        return self.coder.getCode()

    # Enter a parse tree produced by pmlParser#NAMED.
    def enterNAMED(self, ctx:pmlParser.NAMEDContext):
        self.coder.enterNAMED()

    # Exit a parse tree produced by pmlParser#NAMED.
    def exitNAMED(self, ctx:pmlParser.NAMEDContext):
        self.coder.exitNAMED()

    # Enter a parse tree produced by pmlParser#UNNAMED.
    def enterUNNAMED(self, ctx:pmlParser.UNNAMEDContext):
        self.coder.enterUNNAMED()

    # Exit a parse tree produced by pmlParser#UNNAMED.
    def exitUNNAMED(self, ctx:pmlParser.UNNAMEDContext):
        self.coder.exitUNNAMED()

    # Enter a parse tree produced by pmlParser#named_block.
    def enterNamed_block(self, ctx:pmlParser.Named_blockContext):
        self.coder.enterNamed_block(ctx.getChild(1).getText())

    # Exit a parse tree produced by pmlParser#named_block.
    def exitNamed_block(self, ctx:pmlParser.Named_blockContext):
        self.coder.exitNamed_block()

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

    # Enter a parse tree produced by pmlParser#ATTR.
    def enterATTR(self, ctx:pmlParser.ATTRContext):
        self.coder.enterATTR(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#sym_expression.
    def enterSym_expression(self, ctx:pmlParser.Sym_expressionContext):
        self.coder.enterSym_expression(ctx.getText())

    # Enter a parse tree produced by pmlParser#use_expression.
    def enterUse_expression(self, ctx:pmlParser.Use_expressionContext):
        self.coder.enterUse_expression(ctx.getText())

    # Enter a parse tree produced by pmlParser#smooth_expression.
    def enterSmooth_expression(self, ctx:pmlParser.Smooth_expressionContext):
        self.coder.enterSmooth_expression(ctx.parentCtx.getChild(0).getText(), ctx.getText())

    # Enter a parse tree produced by pmlParser#markup_block.
    def enterMarkup_block(self, ctx:pmlParser.Markup_blockContext):
        self.coder.enterMarkup_block()

    # Exit a parse tree produced by pmlParser#markup_block.
    def exitMarkup_block(self, ctx:pmlParser.Markup_blockContext):
        self.coder.exitMarkup_block()

    # Enter a parse tree produced by pmlParser#attributes.
    def exitAttributes(self, ctx:pmlParser.AttributesContext):
        self.coder.exitAttributes()
        
    # Enter a parse tree produced by pmlParser#RANDN.
    def enterRANDN(self, ctx:pmlParser.RANDNContext):
        self.coder.enterRANDN(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#RANDW.
    def enterRANDW(self, ctx:pmlParser.RANDWContext):
        self.coder.enterRANDW(ctx.getChild(1).getText())

    # Enter a parse tree produced by pmlParser#attr_name.
    def enterAttr_name(self, ctx:pmlParser.Attr_nameContext):
        self.coder.enterAttr_name(ctx.getText())

    # Enter a parse tree produced by pmlParser#COND.
    def enterCOND(self, ctx:pmlParser.CONDContext):
        self.coder.enterCOND(ctx.getChild(2).getText(),ctx.getChild(4).getText())

    # # Exit a parse tree produced by pmlParser#COND.
    def exitCOND(self, ctx:pmlParser.CONDContext):
        self.coder.exitCOND()

    # Enter a parse tree produced by pmlParser#USEFROM.
    def enterUSEFROM(self, ctx:pmlParser.USEFROMContext):
        self.coder.enterUSEFROM(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#PERBUILD.
    def enterPERBUILD(self, ctx:pmlParser.PERBUILDContext):
        self.coder.enterPERBUILD()

    # Exit a parse tree produced by pmlParser#PERBUILD.
    def exitPERBUILD(self, ctx:pmlParser.PERBUILDContext):
        self.coder.exitPERBUILD()

    # Enter a parse tree produced by pmlParser#NESTED.
    def enterNESTED(self, ctx:pmlParser.NESTEDContext):
        self.coder.enterNESTED(ctx.getText())

    # Enter a parse tree produced by pmlParser#CONST.
    def enterCONST(self, ctx:pmlParser.CONSTContext):
        self.coder.enterCONST(ctx.getChild(0).getText())

    # Enter a parse tree produced by pmlParser#condition.
    def enterCondition(self, ctx:pmlParser.ConditionContext):
        self.coder.enterCondition(ctx.getText())

    # Enter a parse tree produced by pmlParser#ATOM_SINGLE.
    def enterATOM_SINGLE(self, ctx:pmlParser.ATOM_SINGLEContext):
        self.coder.enterATOM_SINGLE(ctx.getText())

    # Enter a parse tree produced by pmlParser#ATOM_FROMATTR.
    def enterATOM_FROMATTR(self, ctx:pmlParser.ATOM_FROMATTRContext):
        self.coder.enterATOM_FROMATTR(ctx.getChild(2).getText(),ctx.getChild(4).getText())

    # Enter a parse tree produced by pmlParser#ATOM_FROMATTR_SHORT.
    def enterATOM_FROMATTR_SHORT(self, ctx:pmlParser.ATOM_FROMATTR_SHORTContext):
        self.coder.enterATOM_FROMATTR_SHORT(ctx.getChild(2).getText())

    # Enter a parse tree produced by pmlParser#ATOM_IDENT.
    def enterATOM_IDENT(self, ctx:pmlParser.ATOM_IDENTContext):
        self.coder.enterATOM_IDENT(ctx.getText())

    # Enter a parse tree produced by pmlParser#const_atom.
    def enterConst_atom(self, ctx:pmlParser.Const_atomContext):
        self.coder.enterConst_atom(ctx.getText())

    # Enter a parse tree produced by pmlParser#def_name.
    def enterDef_name(self, ctx:pmlParser.Def_nameContext):
        self.coder.enterDef_name(ctx.getText())

    # Enter a parse tree produced by pmlParser#simple_expr.
    def enterSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        self.coder.enterSimple_expr(ctx.getText())

    # Enter a parse tree produced by pmlParser#relop.
    def enterRelop(self, ctx:pmlParser.RelopContext):
        self.coder.enterRelop(ctx.getText())

    # Enter a parse tree produced by pmlParser#arith_op.
    def enterArith_op(self, ctx:pmlParser.Arith_opContext):
        self.coder.enterArith_op(ctx.getText())
