import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from pml_grammar.pmlLexer import pmlLexer
from pml_grammar.pmlParser import pmlParser
from PythonListener import PythonListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = pmlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = pmlParser(stream)
    tree = parser.style()
    translator = PythonListener('output.py')
    walker = ParseTreeWalker()
    walker.walk(translator, tree) 

if __name__ == '__main__':
    main(sys.argv)