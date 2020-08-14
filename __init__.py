from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .pml_grammar.pmlLexer import pmlLexer
from .pml_grammar.pmlParser import pmlParser
from .PythonListener import PythonListener
from .PML_Preprocessor import PML_Preprocessor
from .ExceptionManagement import ParserExceptionListener
from .ExceptionManagement import ParserException


class PML:
    
    def __init__(self, pmlFilePath, assetsDir):
        self.pmlFilePath = pmlFilePath
        self.assetsDir = assetsDir
    
    def getPythonCode(self):
        preprocessor = PML_Preprocessor(self.assetsDir)
        preprocessor.process(self.pmlFilePath)
        
        inputStream = InputStream(preprocessor.getStream())
        lexer = pmlLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = pmlParser(stream)
        
        parser.removeErrorListeners()
        exceptionListener = ParserExceptionListener()
        parser.addErrorListener(exceptionListener)
        
        try:
            tree = parser.styles()
        except ParserException as e:
            line, col, msg = e.errParams()
            localFile, localLine = preprocessor.trackDownLineNr(line)
            raise Exception(
                "Error in file {file} on line {line}, col {col}: {msg}".format(
                    file = localFile, line = localLine, col = col, msg = msg
                )
            )
        
        translator = PythonListener()
        walker = ParseTreeWalker()
        walker.walk(translator, tree)
        
        return translator.getCode()