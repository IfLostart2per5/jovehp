from coreLib.Exceptions import *
from coreLib.resources import const
'''
Estrutura:

$STORAGE
└JovehpProject
		├analyzers
				└jhpLexer.py
				└jhpParser.py
		├compiled(is here that the file-test-dev go)
				
		├coreLib
				└compiler.py
				└Exceptions.py
				└teste.jhp
				└Types.py
				└resources.py
				└Ast.py(actual file now)
		└logs
				
'''
class Program:
	def __init__(self, states):
		self.childs = states
		
	def __str__(self):
		return f"{self.childs}"



class ValueAssign:
	def __init__(self, Type, name, value):
		self.typ = Type
		self.name = name
		self.value = value
		self.variety = ''
		self.defineVariety()
		
	def defineVariety(self):
		if self.name.startswith('#'):
			self.variety = 'v'
		elif self.name.startswith('$'):
			self.variety = 'c'
			self.value = const(self.value)
		else:
			raise UndefinedVarietyException("{} no has a variety symbol".format(self.name))
			
	def __str__(self):
		return f"variety={self.variety}; type={self.typ}; name={self.name}; value={self.value}"

class FuncDefine:
	def __init__(self, returnType, name, args, codeBlock):
		self.returnT = returnType
		self.name = name
		self.args = args
		self.code = codeBlock


		
class binOperation:
	def __init__(self, op, oper1, oper2):
		self._availableOpers = ['+', '-', '.', '*', '/', '%', '**']
		self.operator = op
		self.opperand1 = oper1
		self.opperand2 = oper2
		self._check()
	
	def _check(self):
		if self.operator in self._availableOpers:
			pass
		else:
			raise SyntaxException(" isn't a operator", 11, self.operator)
class bitwiseOperation:
	def __init__(self, op, bit1, bit2):
		self._availableOpers = ['&', '|', '^', '<<', '>>']
		self.operator = op
		self.bit1 = bit1
		self.bit2 = bit2
		self._check()
	
	
	def _check(self):
		if self.op in self._availableOpers:
			pass
		else:
			raise SyntaxException(" isn't a operator", 11, self.operator)
			
			

class unaryOperation:
	def __init__(self, op, operandORbit):
		self._availableOpers = ['-', '!', '++', '--']
		self.op = op
		self.oper_bit = operandORbit
		self._check()
		
	def _check(self):
		if self.op in self._availableOpers:
			pass
		else:
			raise SyntaxException(" isn't a operator", 11, self.operator)
	
class conditionalOperation:
	def __init__(self, op, cmpr1, cmpr2):
		self._availableOpers = ['<', '>', '>=', '<=', '==', '!=']
		self.op = op
		self.value1 = cmpr1
		self.value2 = cmpr2
		self._check()
		
	def _check(self):
		if self.op in self._availableOpers:
			pass
		else:
			raise SyntaxException(" isn't a operator", 11, self.operator)
		


class Argument:
	def __init__(self, Type, name):
		self.typ = Type
		self.name = name
		
		
class Block:
	def __init__(self):
		self.codeLines = []
		
	def addLine(self, code):
		self.codeLines.append(code)
		
class Value:
	def __init__(self, x):
		self.x = x
		

class IfStatement:
	def __init__(self, condition, block, Else=None, blockElse=None):
		self.cond = condition
		self.block = block
		if Else is not None and blockElse is not None:
			self.condElse = Else
			self.blockElse = blockElse
			
			
class ForStatement:
	def __init__(self, var, stopCondition, updater, block):
		self.var = var
		self.stopCond = stopCondition
		self.upd = updater
		self.block = block
class ForEveryStatement:
	def __init__(self, var, iterable, block):
		self.var = var
		self.collection = iterable
		self.block = block
		
class WhileStatement:
	def __init__(self, condition, block):
		self.cond = condition
		self.block = block
		
class ReturnValue:
	def __init__(self, keyword, value):
		self.__ = keyword
		self.x = value
	
class FuncCall:
	def __init__(self, name, params):
		self.name = name
		self.pars = params
		
class Parameter:
	def __init__(self, value):
		self.x = value