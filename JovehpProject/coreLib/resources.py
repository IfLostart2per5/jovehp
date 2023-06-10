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
				└resources.py(actual file now)
				└Ast.py
		└logs
				
'''
class const:
	def __init__(self, value):
		self.this = (value, )
	
	def __str__(self):
		return str(self.this[0])
#gerenciador de escopo		
class Scope:
	def __init__(self, scopeAlias="global", *args):
		self.level = 0
		self.alias = scopeAlias
		self.statements = args
		self._check()
		
	def _check(self):
		if self.level < 0:
			raise ValueError("Errno 10: no has a scope level started")
		
		if self.level % 2 != 0:
			raise ValueError("Errno 10: no has a scope level closed")