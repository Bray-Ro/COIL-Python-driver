from ctypes import *



   
KEYWORD = 1
OPERATOR = 2
SEPARATOR = 3
LITERAL = 4
IDENTIFIER = 5
COMMENT = 6
PUNTUATOR = 7
SCOPE = 8




class _TOKEN(Structure):
        _fields_ = [("TYPE", c_int), ("LEXEME", ARRAY(255, c_char)), ("ID", c_int)]




def commander_lexer(program, syntax):        
        fun = CDLL('lexer.so')

        fun.commander_lexer.argtypes = [POINTER(c_char), ARRAY(len(syntax), _TOKEN), c_int]
  
        fun.commander_lexer(program, (_TOKEN * len(syntax))(*syntax), len(syntax))
