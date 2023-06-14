import sys
sys.path.append("..")
from coreLib.Exceptions import *
from decimal import *
import re
#funcoes extras
def boolean(string):
	if string == "true":
		return True
	elif string == "false":
		return False
	else:
		if string[0] == "f":
			mean = "false"
		else:
			mean = "true"
		raise LexException("Errno 5: Lexical Error: {} is wrong, did you mean {}?")
		
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
				└Types.py(actual file now)
				└resources.py
				└Ast.py
		└logs
				
'''
'''
Tipos do Jovehp:

esse módulo conterá tipos adicionais ao python, e reformulação de alguns tipos nativos do python
(como o "array" por exemplo).

Quaisquer erros presentes (ou sugestões), não deixe de contatar o desenvolvedor!

versão pre-alpha 0.0.1-rb


por Alexandre Barreto
'''


'''
Tipo any: serve como "um tipo qualquer", como por exemplo, uma constante que pode receber qualquer valor:

//'$' no inicio indica uma constante
any $VALOR = 37
any $VALOR2 = 38.445F


e pra arrays:
//'#' no inicio indica uma variavel
array[any] #lista = [32, 'v', "Casa", true, 32+7i]



'''
class Any:
	regexes = {"integer": re.compile(r"\s*\d+\s*"),
		        "float": re.compile(r"\s*\d+(\.\d{1,6}F)\s*", re.IGNORECASE),
		        "double float": re.compile(r"\s*\d+(\.\d{1, 15})"),
		        "string": re.compile(r'"(.*?)"'),
		        "character": re.compile(r"'.'", re.DOTALL),
		        "array": re.compile(r"\[\s*\w*?\s*(,\s*\w+?\s*)*?\]"),
		        "boolean": re.compile(r"true|false"),
		        "complex number": re.compile(r"\s*(-?\d+(\.\d+)?)([+-]\d+(\.\d+)?)i\s*", re.IGNORECASE),
		        }
	
	def __init__(self, x):
		# o valor recebido e o seu tipo
		self.x = str(x)
		self.typeIt()
	
	#permitir o print
	def __str__(self):
		return str(self.x)
	
	#identificar tipos (e tipa-los)
	def typeIt(self):
		if Any.regexes["integer"].match(self.x):
			
			self.x = int(self.x)
		elif Any.regexes["float"].match(self.x):
			
			self.x = float(self.x)
		elif Any.regexes["double float"].match(self.x):
			
			self.x = double(self.x)
		elif Any.regexes["string"].match(self.x):
			pass
		elif Any.regexes["character"].match(self.x):
			self.x = char(self.x)
		elif Any.regexes["boolean"].match(self.x):
			
			self.x = boolean(self.x)
		elif Any.regexes["complex number"].match(self.x):
			
			self.x = self.x.lower()
			self.x = complex(self.x.replace("i", "j"))
		elif Any.regexes["array"].match(self.x):
			
			self.x = array("any", self.x)
		else:
			raise UndefinedTypeException("{} isn't a possible value.".format(self.x))
'''
Tipo double float:
um tipo numérico, que ter

'''
class double:
	def __init__(self, x):
		getcontext().prec = 15
		self.x = Decimal(x)
		
		
	def __add__(self, other):
		result = self.x + other.x
		return result.quantize(Decimal("0.0000000000000"))
		
	def __mul__(self, other):
		result = self.x * other.x
		return result.quantize(Decimal("0.0000000000000"))
		

		
	__rmul__ = __mul__
	
	__radd__ = __add__
	
	
	
	def __rminus__(self, other):
		result = other.x - self.x
		return result.quantize(Decimal("0.0000000000000"))
		
		
	def __rdiv__(self, other):
		result = other.x / self.x
		return result.quantize(Decimal("0.0000000000000"))
		
		
	

class char:
	def __init__(self, character: str, setEncoding="ascii"):
		self.encode = setEncoding
		self.char = str(character).encode(self.encode)
		self._check_()
	def __str__(self):
		return '%s' % (self.char)
		
	def _check_(self):
		if len(self.char) > 1:
			raise ValueError("Errno 1: character-type must have once character!")
		

		

class array:
	
	
	def _toArray(self, string, typeT):
		string = string.strip()
		string = string.replace("[", "")
		string = string.replace("]", "")
		string = string.split(",")
		match typeT:
			case "integer":
				return list(map(int, string))
			case "float":
				return list(map(float, string))
			case "string":
				return list(map(str, string))
			case "character":
				return list(map(char, string))
			case "boolean":
				return list(map(boolean, string))
			case "complex number":
				return list(map(complex, string))
			case "double float":
				return list(map(double, string))
			case "any":
				return [Any(i).x for i in string]
			case _:
				raise UndefinedTypeException("{} isn't a type".format(typeT))
				
			
	def __init__(self, type, string=None):
		self.type = type
		if string is not None:
			self._this = self._toArray(string, self.type)
		else: 
			self._this = []
		self._check_()
		
		
	@property
	def this(self):
		return self._this
		
	def _check_(self):
		match self.type:
			case "int":
				self.type = 0
			case "float":
				self.type = 0.0
			case "str":
				self.type = ""
			case "char":
				self.type = char('v', "utf-8")
			case "bool":
				self.type = False
			case "array":
				self.type = array("any")
			case "double":
				self.type = double(0.000000000001)
			case "complex":
				self.type = 0+0j
			case "any":
				self.type = Any(8).x
			case _:
				raise UndefinedTypeException("{} isn't a type".format(self.type))
	#torna o atributo inacessivel
	@this.setter
	def this(self):
		raise ValueError("Errno 2: private attribute")
		
	def __str__(self):
		return str(self._this)
		
		
	#adicionar itens
	def add(self, value):
		if type(value) is type(self.type):
			self._this.append(value)
		else:
			raise ValueError("Errno 5: uncompatible types")
	#pra retornar o indice
	def __getitem__(self, i):
		try:
			return self._this[i]
		except IndexError:
			return "IndexError! this index isn't a goal for this list lol 🤣🤣🤣"
 
 #teste dos tipos
if __name__ == "__main__":
	a = char("\t")
	arr = array("int")
	arr.add(4)
	teste = double(3.0)
	teste1 = double(3.1415956432524)
	arr.add(4)
	arr.add(0xff)
	print(arr)
	print(teste1 + teste)