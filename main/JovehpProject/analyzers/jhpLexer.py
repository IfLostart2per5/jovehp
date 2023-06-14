from sys import path
path.append("..")
#tipos
from coreLib.Types import *
#erros
from coreLib.Exceptions import *
#basic lexer
from sly import Lexer



'''
Estrutura:

$STORAGE
└JovehpProject
		├analyzers
				└jhpLexer.py(actual file now)
				└jhpParser.py
		├compiled(is here that the file-test-dev go)
				
		├coreLib
				└compiler.py
				└Exceptions.py
				└teste.jhp
				└Types.py
				└resources.py
				└Ast.py
		└logs
				
'''
#Analisador Lexico
class JHPLex(Lexer):
	tokens = {TYPE, ID, INT, FLOAT, DOUBLE, STRING, ARRAY, CHAR, BOOL, COMPLEX, INTERNALWORD, IF, ELSE, WHILE, FOR, FOREACH, IN, RSHIFT, LSHIFT, EQ, GE, LE, NE, FUNCTION, RETURN, POWER, INCREASE, DECREASE}
	
	literals = {';', '=', '[', ']', '+', '-', '*', '/', '(', ')', '{', '}', '!', '^', '.', '&', '|', '>', '<', '%', ','}
	
	ignore = " \t"
	ignore_comment = r"``\s*.*\s*``|\#\#"
	ignore_newline = r"\n+"
	
	
	TYPE = r"integer|float|double float|string|array\[(\w+?)\]|character|boolean|complex number|void|any"
	ID = r"(?P<constant>\$[a-zA-Z_][a-zA-Z0-9_]*)|(?P<variable>\#[a-zA-Z_][a-zA-Z0-9_]*)"
	COMPLEX = r"(\-?\d+(\.\d+)?)([+-]\d+(\.\d+)?)(i|I)"
	ARRAY = r"\[\s*\w*?\s*(,\s*\w+?\s*)*?\]"
	FLOAT = r"\-?\d+(\.\d{1,6}(f|F))"
	DOUBLE = r"\-?\d+(\.\d{1,15})"
	BOOL = r"true|false"
	CHAR = r"'\s'|'.'"
	INT = r"\-?\d+"
	STRING = r'"\s*.*?"'
	LSHIFT = r"\<\<"
	RSHIFT = r"\>\>"
	EQ = r"\=\="
	GE = r"\>\="
	LE = r"\<\="
	NE = r"\!\="
	POWER = r"\*\*"
	INCREASE = r"\+\+"
	DECREASE = r"\-\-"
	INTERNALWORD = r"[a-zA-Z_][a-zA-Z0-9_]*"
	
	
	INTERNALWORD["if"] = IF
	INTERNALWORD["else"] = ELSE
	INTERNALWORD["for"] = FOR
	INTERNALWORD["every"] = FOREACH
	INTERNALWORD["while"] = WHILE
	INTERNALWORD["in"] = IN
	INTERNALWORD["func"] = FUNCTION
	INTERNALWORD["return"] = RETURN
	def __init__(self):
		#nivel de aninhamento
		self.nesting_level = 0
	@_(r"[a-zA-Z_][a-zA-Z0-9_]*")
	def INTERNALWORD(self, t):
		match t.value:
			case "if":
				return t
			case "else":
				return t
			case "every":
				return t
			case "while":
			 	return t
			case "for":
				return t
			case "in":
				return t
			case "func":
				return t
			case "return":
				return t
			case _:
				raise KeywordNotFoundException(" isn't a keyword", t.value)
	#pre processamento para booleano
	@_(r"true|false")
	def BOOL(self, t):
		if t.value == "true":
			self.index += len(t.value)
			t.value = True
			return t
		elif t.value == "false":
			self.index += len(t.value)
			t.value = False
			return t
		else:
			if t.value[0] == "f":
				mean = "false"
			else:
				mean = "true"
				raise LexException("Errno 5: Lexical error: Error on value {}, did you mean {}?".format(t.value, mean))
			
			
	#pre processamento para inteiros
	@_(r"\-?\d+")
	def INT(self, t):
		t.value = int(t.value)
		return t
	
	#pre processamento para numeros complexos
	@_((r"(\-?\d+(\.\d+)?)([+-]\d+(\.\d+)?)(i|I)"))
	def COMPLEX(self, t):
		t.value = t.value.lower()
		t.value = complex(t.value.replace("i", "j"))
		return t
	#contador de linhas
	@_(r"\n+")
	def ignore_newline(self, t):
		self.lineno += t.value.count("\n")
	
	#çre processamento para float
	@_(r"\-?\d+(\.\d{1,6}(f|F))")
	def FLOAT(self, t):
		t.value = float(t.value[:-1])
		return t
	
	#pre processamento para arrays
	@_(r"\[\s*\w*?\s*(,\s*\w+?\s*)*?\]")
	def ARRAY(self, t):
		t.value = array("any", t.value)
		return t
	
	#pre processamento para caracter
	@_(r"'.'|'\s'")
	def CHAR(self, t):
		t.value = char(t.value, "utf-8")
		return t
	
	#pre processamento para string
	@_(r'"\s*.*?"')
	def STRING(self, t):
		t.value = t.value.strip('"')
		return t
		
		
	#exception para "mau-caracter"
	def error(self, t):
		print("bad character '{char}' at line {lineno} and index {index}".format(char=t.value[0], lineno=self.lineno, index=self.index))
		self.index += 1
	
	
	
	
if __name__ == "__main__":
	jhp = JHPLex()
	while True:
		
		expr = input("code > ")
		if expr == "exit":
			break
		for tok in jhp.tokenize(expr):
		
			print("type='{}' value='{}' indexS={} indexE={} line={}".format(tok.type, tok.value, tok.index, tok.index + len(str(tok.value)) - 1, tok.lineno))
		
		
	
		
	
		