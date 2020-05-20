from pml_grammar.pmlListener import pmlListener
from pml_grammar.pmlParser import pmlParser
import inspect

import sys

# This class defines a complete listener for a parse tree produced by pmlParser.
class testListener(pmlListener):

    def getCode(self):
        return "ENDE"

    # Enter a parse tree produced by pmlParser#style.
    def enterStyle(self, ctx:pmlParser.StyleContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#style.
    def exitStyle(self, ctx:pmlParser.StyleContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#elements.
    def enterElements(self, ctx:pmlParser.ElementsContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#elements.
    def exitElements(self, ctx:pmlParser.ElementsContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#element.
    def enterElement(self, ctx:pmlParser.ElementContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#element.
    def exitElement(self, ctx:pmlParser.ElementContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#attributes.
    def enterAttributes(self, ctx:pmlParser.AttributesContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#attributes.
    def exitAttributes(self, ctx:pmlParser.AttributesContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#attribute.
    def enterAttribute(self, ctx:pmlParser.AttributeContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#attribute.
    def exitAttribute(self, ctx:pmlParser.AttributeContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#expression.
    def enterExpression(self, ctx:pmlParser.ExpressionContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#expression.
    def exitExpression(self, ctx:pmlParser.ExpressionContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#alternatives.
    def enterAlternatives(self, ctx:pmlParser.AlternativesContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#alternatives.
    def exitAlternatives(self, ctx:pmlParser.AlternativesContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#ATTR.
    def enterATTR(self, ctx:pmlParser.ATTRContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#ATTR.
    def exitATTR(self, ctx:pmlParser.ATTRContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#RANDN.
    def enterRANDN(self, ctx:pmlParser.RANDNContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#RANDN.
    def exitRANDN(self, ctx:pmlParser.RANDNContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#RANDW.
    def enterRANDW(self, ctx:pmlParser.RANDWContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#RANDW.
    def exitRANDW(self, ctx:pmlParser.RANDWContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#COND.
    def enterCOND(self, ctx:pmlParser.CONDContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#COND.
    def exitCOND(self, ctx:pmlParser.CONDContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#NESTED.
    def enterNESTED(self, ctx:pmlParser.NESTEDContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#NESTED.
    def exitNESTED(self, ctx:pmlParser.NESTEDContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#CONST.
    def enterCONST(self, ctx:pmlParser.CONSTContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#CONST.
    def exitCONST(self, ctx:pmlParser.CONSTContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#ARITH.
    def enterARITH(self, ctx:pmlParser.ARITHContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#ARITH.
    def exitARITH(self, ctx:pmlParser.ARITHContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#nested_list.
    def enterNested_list(self, ctx:pmlParser.Nested_listContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#nested_list.
    def exitNested_list(self, ctx:pmlParser.Nested_listContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#def_name.
    def enterDef_name(self, ctx:pmlParser.Def_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#def_name.
    def exitDef_name(self, ctx:pmlParser.Def_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#conditional.
    def enterConditional(self, ctx:pmlParser.ConditionalContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#conditional.
    def exitConditional(self, ctx:pmlParser.ConditionalContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#condition.
    def enterCondition(self, ctx:pmlParser.ConditionContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#condition.
    def exitCondition(self, ctx:pmlParser.ConditionContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#arith_expr.
    def enterArith_expr(self, ctx:pmlParser.Arith_exprContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#arith_expr.
    def exitArith_expr(self, ctx:pmlParser.Arith_exprContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#ATOM_SINGLE.
    def enterATOM_SINGLE(self, ctx:pmlParser.ATOM_SINGLEContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#ATOM_SINGLE.
    def exitATOM_SINGLE(self, ctx:pmlParser.ATOM_SINGLEContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#ATOM_FROMATTR.
    def enterATOM_FROMATTR(self, ctx:pmlParser.ATOM_FROMATTRContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#ATOM_FROMATTR.
    def exitATOM_FROMATTR(self, ctx:pmlParser.ATOM_FROMATTRContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#ATOM_IDENT.
    def enterATOM_IDENT(self, ctx:pmlParser.ATOM_IDENTContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#ATOM_IDENT.
    def exitATOM_IDENT(self, ctx:pmlParser.ATOM_IDENTContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#const_atom.
    def enterConst_atom(self, ctx:pmlParser.Const_atomContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#const_atom.
    def exitConst_atom(self, ctx:pmlParser.Const_atomContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#constant.
    def enterConstant(self, ctx:pmlParser.ConstantContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#constant.
    def exitConstant(self, ctx:pmlParser.ConstantContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#simple_expr.
    def enterSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#simple_expr.
    def exitSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#element_name.
    def enterElement_name(self, ctx:pmlParser.Element_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#element_name.
    def exitElement_name(self, ctx:pmlParser.Element_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#attr_name.
    def enterAttr_name(self, ctx:pmlParser.Attr_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#attr_name.
    def exitAttr_name(self, ctx:pmlParser.Attr_nameContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#relop.
    def enterRelop(self, ctx:pmlParser.RelopContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#relop.
    def exitRelop(self, ctx:pmlParser.RelopContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#arith_op.
    def enterArith_op(self, ctx:pmlParser.Arith_opContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#arith_op.
    def exitArith_op(self, ctx:pmlParser.Arith_opContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#number.
    def enterNumber(self, ctx:pmlParser.NumberContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#number.
    def exitNumber(self, ctx:pmlParser.NumberContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")


    # Enter a parse tree produced by pmlParser#string_literal.
    def enterString_literal(self, ctx:pmlParser.String_literalContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")

    # Exit a parse tree produced by pmlParser#string_literal.
    def exitString_literal(self, ctx:pmlParser.String_literalContext):
        sys.stdout.write(inspect.stack()[0][3]+": "+ctx.getText()+"\n")



del pmlParser