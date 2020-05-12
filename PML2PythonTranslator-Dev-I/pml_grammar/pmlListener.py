# Generated from pml.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pmlParser import pmlParser
else:
    from pmlParser import pmlParser

# This class defines a complete listener for a parse tree produced by pmlParser.
class pmlListener(ParseTreeListener):

    # Enter a parse tree produced by pmlParser#style.
    def enterStyle(self, ctx:pmlParser.StyleContext):
        pass

    # Exit a parse tree produced by pmlParser#style.
    def exitStyle(self, ctx:pmlParser.StyleContext):
        pass


    # Enter a parse tree produced by pmlParser#elements.
    def enterElements(self, ctx:pmlParser.ElementsContext):
        pass

    # Exit a parse tree produced by pmlParser#elements.
    def exitElements(self, ctx:pmlParser.ElementsContext):
        pass


    # Enter a parse tree produced by pmlParser#element.
    def enterElement(self, ctx:pmlParser.ElementContext):
        pass

    # Exit a parse tree produced by pmlParser#element.
    def exitElement(self, ctx:pmlParser.ElementContext):
        pass


    # Enter a parse tree produced by pmlParser#attributes.
    def enterAttributes(self, ctx:pmlParser.AttributesContext):
        pass

    # Exit a parse tree produced by pmlParser#attributes.
    def exitAttributes(self, ctx:pmlParser.AttributesContext):
        pass


    # Enter a parse tree produced by pmlParser#attribute.
    def enterAttribute(self, ctx:pmlParser.AttributeContext):
        pass

    # Exit a parse tree produced by pmlParser#attribute.
    def exitAttribute(self, ctx:pmlParser.AttributeContext):
        pass


    # Enter a parse tree produced by pmlParser#expression.
    def enterExpression(self, ctx:pmlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pmlParser#expression.
    def exitExpression(self, ctx:pmlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pmlParser#alternatives.
    def enterAlternatives(self, ctx:pmlParser.AlternativesContext):
        pass

    # Exit a parse tree produced by pmlParser#alternatives.
    def exitAlternatives(self, ctx:pmlParser.AlternativesContext):
        pass


    # Enter a parse tree produced by pmlParser#ATTR.
    def enterATTR(self, ctx:pmlParser.ATTRContext):
        pass

    # Exit a parse tree produced by pmlParser#ATTR.
    def exitATTR(self, ctx:pmlParser.ATTRContext):
        pass


    # Enter a parse tree produced by pmlParser#RANDN.
    def enterRANDN(self, ctx:pmlParser.RANDNContext):
        pass

    # Exit a parse tree produced by pmlParser#RANDN.
    def exitRANDN(self, ctx:pmlParser.RANDNContext):
        pass


    # Enter a parse tree produced by pmlParser#RANDW.
    def enterRANDW(self, ctx:pmlParser.RANDWContext):
        pass

    # Exit a parse tree produced by pmlParser#RANDW.
    def exitRANDW(self, ctx:pmlParser.RANDWContext):
        pass


    # Enter a parse tree produced by pmlParser#CONST.
    def enterCONST(self, ctx:pmlParser.CONSTContext):
        pass

    # Exit a parse tree produced by pmlParser#CONST.
    def exitCONST(self, ctx:pmlParser.CONSTContext):
        pass


    # Enter a parse tree produced by pmlParser#nested_list.
    def enterNested_list(self, ctx:pmlParser.Nested_listContext):
        pass

    # Exit a parse tree produced by pmlParser#nested_list.
    def exitNested_list(self, ctx:pmlParser.Nested_listContext):
        pass


    # Enter a parse tree produced by pmlParser#constant.
    def enterConstant(self, ctx:pmlParser.ConstantContext):
        pass

    # Exit a parse tree produced by pmlParser#constant.
    def exitConstant(self, ctx:pmlParser.ConstantContext):
        pass


    # Enter a parse tree produced by pmlParser#simple_expr.
    def enterSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        pass

    # Exit a parse tree produced by pmlParser#simple_expr.
    def exitSimple_expr(self, ctx:pmlParser.Simple_exprContext):
        pass


    # Enter a parse tree produced by pmlParser#element_name.
    def enterElement_name(self, ctx:pmlParser.Element_nameContext):
        pass

    # Exit a parse tree produced by pmlParser#element_name.
    def exitElement_name(self, ctx:pmlParser.Element_nameContext):
        pass


    # Enter a parse tree produced by pmlParser#attr_name.
    def enterAttr_name(self, ctx:pmlParser.Attr_nameContext):
        pass

    # Exit a parse tree produced by pmlParser#attr_name.
    def exitAttr_name(self, ctx:pmlParser.Attr_nameContext):
        pass


    # Enter a parse tree produced by pmlParser#number.
    def enterNumber(self, ctx:pmlParser.NumberContext):
        pass

    # Exit a parse tree produced by pmlParser#number.
    def exitNumber(self, ctx:pmlParser.NumberContext):
        pass


    # Enter a parse tree produced by pmlParser#string_literal.
    def enterString_literal(self, ctx:pmlParser.String_literalContext):
        pass

    # Exit a parse tree produced by pmlParser#string_literal.
    def exitString_literal(self, ctx:pmlParser.String_literalContext):
        pass



del pmlParser