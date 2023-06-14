import sys
sys.path.append("..")
from analyzers import jhpParser, jhpLexer
from Exceptions import *
import argparse
from datetime import datetime as dt
jhpl = jhpLexer.JHPLex()
jhpp = jhpParser.JHParse()
parser = argparse.ArgumentParser(
	description="Jovehp transpiler"
)

parser.add_argument('--file', action="store", dest="file", required=True, help="Write a file to compile")

args = parser.parse_args()

if str(args.file).endswith(".jhp"):
	file = open(str(args.file)) 
else:
	raise NotAJovehpFileException("it's not a Jovehp (jhp) file.", str(args.file))
	
activity = open(f'../logs/jovehp_activity_{(now := dt.now()).strftime("%Y%m%d")}-{now.strftime("%H%M%S")}.log', 'w')

method = input("Quer parsear ou tokenizar? [ parse / tokenize ]: ").lower()
if method == 'parse':
	print(parsed := jhpParser.analyze(file.read()))
	activity.write(f'{parsed}')
elif method == 'tokenize':
	for tok in jhpl.tokenize(file.read()):
		print("name='{}'; value='{}'; type='{}'; line={}; index={}; end={};".format(tok.type, tok.value, type(tok.value), tok.lineno, tok.index, tok.end))
		activity.write("name='{}'; value='{}'; type='{}'; line={}; index={}; end={};\n".format(tok.type, tok.value, type(tok.value), tok.lineno, tok.index, tok.end))
	
file.close()
activity.close()