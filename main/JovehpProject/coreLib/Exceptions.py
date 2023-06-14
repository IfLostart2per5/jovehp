
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
				└Exceptions.py(actual file now)
				└teste.jhp
				└Types.py
				└resources.py
				└Ast.py
		└logs
				
'''


class LexException(Exception):
	def __init__(self, message):
		super().__init__(message)
		
class UndefinedTypeException(Exception):
	def __init__(self, message):
		message = "Errno 6: UndefinedTypeException: " + message
		super().__init__(message)
		

class KeywordNotFoundException(Exception):
	def __init__(self, message, word):
		message = "Errno 7: KeywordNotFoundException: {}" + message
		super().__init__(message.format(word))
		
class NotAJovehpFileException(Exception):
	def __init__(self, message, file):
		message = "Errno 8: NotAJovehpFileException: {} " + message
		super().__init__(message.format(file))

class BadStringException(Exception):
	def __init__(self, message):
		message = "Errno 9: BadStringException: " + message
		super().__init__(message)


class UndefinedVarietyException(Exception):
	def __init__(self, message):
		message = "Errno 10: UndefinedVarietyException: " + message
		
		super().__init__(message)
		

class SyntaxException(Exception):
	def __init__(self, message, errno, word):
		message = "Errno {}: SyntaxException: {}" + message
		super().__init__(message.format(errno, word))
		
class UndefinedValueException(Exception):
	def __init__(self, message, var):
		message = "Errno 12: UndefinedValueException: {}" + message
		super().__init__(message.format(var))