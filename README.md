# jovehp
A high-level language, transpiled and in future it'll be object-oriented. It is the first version of language, because its only are able to do the basic operations between types and basic instructions, such if and if...else, for and for-every(foreach) and while

Made with Python.


## Syntax

The language syntax will be verbose in some parts, and more "symbolic" in others. see a prototyped syntax below:

```
## lines starting with two hashtags are comments
## in semantic, functions name starting with "$" not're overwrittable, whatever, can't be rewritten
void func $test(integer $arg1, integer $arg2) {
  return $arg1 + $arg2;
}

``
multiline comments are delimited by two "`"
a
b
c
``

## some present types
## var, func names and etc. starting with '#' are overwrittable
integer #test = 37;
float #test2 = 32.827F;
complex number #test3 = 37+89i;
array[integer] #test4 = [2, 9, 3, 7];
## constant below
string $test5 = "Hello world";

echo[output=>"console"] f"Hello %test5 !";

```
it will be better in the future, but, currently, is it.


## Known errors and bugs

it have some errors, such:
  1: it doesn't recognize variables in for and for-every statements;

  2: it throws syntax errors in uexpected situations;

  3: it cannot declare variable in a function scope;

  4: currently it not have a target-language to transpile. suggestions are accepted ^-^;

  Currently, it are the errors that I can remember now. You found more errors? talk with the dev (the same person that is writting this README)




# Documentation
(Remember, it'll the basic syntax when it have a minimum final version (or a alpha), also, it isn't complete, but you can see the AST part in action :D)
To start, I'll explain the data types, and variables:
## Data types
```
##types representation
## "n" equals to a digit
##numbers between braces mean ranges
integer = n or -n;
float = n.n{1..6}F or -n.nF (it'll be ignore case);
double float = n.n{1..15} or -n.n{1..15};
character = 'c';
any = (literally any one of these types, except arrays, that should have array[any]);
array[type] = [e1, e2, e3... e_n];
complex number = n+nI or n-nI (it'll be ignore case);
string = "Hello world";
boolean = true or false;
```

## Variables and constants

(it is based on PHP)
To declare variables, uses "#" on the start of the name, to constants, uses "$" instead:

```
##a variable
integer #ten = 10;
##can be changed
#ten = 22;

##a constant
integer $twenty = 20;
## can't be changed, it'll throws a error
$twenty = 21;

```

