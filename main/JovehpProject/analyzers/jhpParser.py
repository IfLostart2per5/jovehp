from sys import path
path.append("..")
from analyzers.jhpLexer import *
from coreLib.Exceptions import *
from coreLib.resources import *
from coreLib.Ast import *
from coreLib.Types import double, array, boolean
import re
from datetime import datetime as dt
from sly import Parser
#Obs: recém-completo; falta testes


'''
Estrutura:

$STORAGE
└JovehpProject
		├analyzers
				└jhpLexer.py
				└jhpParser.py(actual file now)
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
class JHParse(Parser):
	debug_file = f"../logs/jovehp-at_{dt.now().strftime('%Y%d%m')}_{dt.now().strftime('%M-%S')}.log"
	tokens = JHPLex.tokens
	literals = JHPLex.literals
	precedence = (
		("nonassoc", '<', '>', LE, GE, EQ, NE),
		("left", '+', '-', '.', INCREASE, DECREASE),
		("left", '*', '/', '%'),
		('left', POWER),
		("left", '&', '|', '^', '!', LSHIFT, RSHIFT),
		('right', NEG, NOT)
		)
	
	def __init__(self):
		self.names = { }
		self.blockNames = { }
		self.funcNames = { }
	
	@_('TYPE ID "=" expr ";"')
	def statem(self, p):
		self.names[p.ID] = p.expr
		return ValueAssign(p.TYPE, p.ID, p.expr)
		
	@_('TYPE FUNCTION ID "(" args ")" "{" code "}"')
	def statem(self, p):
		self.funcNames[p.ID] = (p.TYPE, p.args, p.code)
		return FuncDefine(p.TYPE, p.ID, p.args, p.code)
		
	@_('instruct')
	def statem(self, p):
		return p.instruct
	@_('expr')
	def statem(self, p):
		return Value(p.expr)
		
		
	@_('IF "(" expr ")" "{" code "}" ')
	def instruct(self, p):
	
		return IfStatement(p.expr, Block().addLine(p.code))
	
	@_('IF "(" expr ")" "{" code "}" ELSE "{" code "}"')
	def instruct(self, p):
		
		return IfStatement(p.expr, p.code0, p.ELSE, p.code1)
		
	@_('FOR "(" TYPE ID "=" expr ";" expr ";" expr ")" "{" code "}"')
	def instruct(self, p):
		self.names[p.ID] = p.expr0
		return ForStatement((p.TYPE, p.ID, p.expr0), p.expr1, p.expr2, p.code)
		
	
	@_('FOR "(" FOREACH TYPE ID IN expr ")" "{" code "}"')
	def instruct(self, p):
		self.blockNames[p.ID] = "element"
		return ForEveryStatement((p.TYPE, p.ID), p.expr, p.code)
		
	@_('WHILE "(" expr ")" "{" code "}"')
	def instruct(self, p):
		
		return WhileStatement(p.expr, p.code)
		
	
	@_('expr "+" expr')
	def expr(self, p):
		return binOperation("+", p.expr0, p.expr1)
		
	@_('expr "-" expr')
	def expr(self, p):
		return binOperation("-", p.expr0, p.expr1)
		
	@_('expr "." expr')
	def expr(self, p):
		return binOperation(".", p.expr0, p.expr1)
	
	@_('expr "*" expr')
	def expr(self, p):
		return binOperation("*", p.expr0, p.expr1)
	
	@_('expr "/" expr')
	def expr(self, p):
		return binOperation("/", p.expr0, p.expr1)
	
	@_('expr "%" expr')
	def expr(self, p):
		return binOperation("%", p.expr0, p.expr1)
	
	@_('"-" expr %prec NEG')
	def expr(self, p):
		return unaryOperation("-", p.expr)
		
	
	@_('expr POWER expr')
	def expr(self, p):
		return binOperation("**", p.expr0, p.expr1)
	
	@_('"(" expr ")"')
	def expr(self, p):
		return Value(p.expr)
		
	@_('expr INCREASE')
	def expr(self, p):
		
		return binOperation('+', p.expr, 1)
		
	@_('expr DECREASE')
	def expr(self, p):
		
		return binOperation('-', p.expr, 1)
		
	@_('expr "&" expr')
	def expr(self, p):
		return bitwiseOperation("&", p.expr0, expr1)
	
	
	@_('expr "|" expr')
	def expr(self, p):
		return bitwiseOperation("|", p.expr0, expr1)
	
	@_('expr "^" expr')
	def expr(self, p):
		return bitwiseOperation("^", p.expr0, expr1)
	
	@_('"!" expr %prec NOT')
	def expr(self, p):
		return unaryOperation("!", p.expr)
		
	@_('expr RSHIFT expr')
	def expr(self, p):
		return bitwiseOperation('>>', p.expr0, p.expr1)
	
	@_('expr LSHIFT expr')
	def expr(self, p):
		return bitwiseOperation('<<', p.expr0, p.expr1)
	
	
	@_('expr ">" expr')
	def expr(self, p):
		return conditionalOperation(">", p.expr0, p.expr1)
		
	@_('expr "<" expr')
	def expr(self, p):
		return conditionalOperation("<", p.expr0, p.expr1)
		
	@_('expr LE expr')
	def expr(self, p):
		return conditionalOperation("<=", p.expr0, p.expr1)
		
	@_('expr GE expr')
	def expr(self, p):
		return conditionalOperation(">=", p.expr0, p.expr1)
	
	@_('expr EQ expr')
	def expr(self, p):
		return conditionalOperation("==", p.expr0, p.expr1)
		
	@_('expr NE expr')
	def expr(self, p):
		return conditionalOperator("!=", p.expr0, p.expr1)
	
	@_('text')
	def expr(self, p):
		return Value(p.text)
		
	@_('number')
	def expr(self, p):
		return Value(p.number)
		
	@_('sboolean')
	def expr(self, p):
		return Value(p.sboolean)
		
	@_('sarray')
	def expr(self, p):
		return Value(p.sarray)
		
	@_('ID')
	def expr(self, p):
		try:
			
			return self.names[p.ID]
		except LookupError:
			try:
				return self.funcNames[p.ID]
			except LookupError:
				try:
					return self.blockNames[p.ID]
				except LookupError:
					raise UndefinedValueException(" isn't defined.", p.ID)
			
	@_('ID "(" params ")" ";"')
	def expr(self, p):
		return FuncCall(name=p.ID, params=p.params)
		
	
	@_('args "," TYPE ID')
	def args(self, p):
		return Argument(p.TYPE, p.ID)
		
	@_('TYPE ID')
	def args(self, p):
		return Argument(p.TYPE, p.ID)
		
	@_('empty')
	def args(self, p):
		return 0
		
	@_('expr ";" code')
	def code(self, p):
		Code = Block()
		Code.addLine(p.expr)
		return Code
	

	
	@_('expr')
	def code(self, p):
		return Value(p.expr)
		
	@_('RETURN expr ";"')
	def code(self, p):
		return ReturnValue(p.RETURN, p.expr)
		
	@_('empty')
	def code(self, p):
		return 
		
	@_('STRING')
	def text(self, p):
		return Value(str(p.STRING))
		
	@_('CHAR')
	def text(self, p):
		return Value(p.CHAR)
		
	@_('INT')
	def number(self, p):
		return Value(p.INT)
	
	@_('FLOAT')
	def number(self, p):
		return Value(p.FLOAT)
		
	@_('DOUBLE')
	def number(self, p):
		return Value(p.DOUBLE)
		
	@_('COMPLEX')
	def number(self, p):
		return Value(p.COMPLEX)
		
	@_('BOOL')
	def sboolean(self, p):
		return Value(p.BOOL)
		
	@_('ARRAY')
	def sarray(self, p):
		return Value(p.ARRAY)
	
	
	@_('params "," expr')
	def params(self, p):
		return Parameter(p.expr)
	
	@_('expr')
	def params(self, p):
		return Parameter(p.expr)
		
	@_('empty')
	def params(self, p):
		return 0
		
	@_('')
	def empty(self, p):
		return 0
def analyze(data):
	jhpp, jhpl = JHParse(), JHPLex()
	return jhpp.parse(jhpl.tokenize(data))
	
if __name__ == "__main__":
	parser = JHParse()
	lexer = JHPLex()
	
	while (code := input("code > ")) != "exit":
		r = parser.parse(lexer.tokenize(code))
		
		print(r)