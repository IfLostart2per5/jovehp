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

  2: it throws syntax errors in unexpected situations;

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

## Operators

So... it'll have the must common operators in languages, such '*' for multiplication, '/' for divide, '+' for plus, "**" for power and more.

### Arimetics

everything is better with examples, yep?

```
integer $x, $y = 30, 11;
integer #x;


##adding numbers
#x = $x + $y;
##results to 41

##multiplying numbers
#x = $x * $y;
##results to 330

##dividing numbers
#x = $x / $y;
##results to 2 (*1)

#subtracting numbers
#x = $x - $y;
##results to 19

##raising x to power of y
#x = $x ** $y;
##results to 1,77147000e+16

##rest/module operator below
#x = $x % $y;
#results to 8
```
notes:
  1: if you use the division operator in integers, you must have to convert it to be a float/double, else, you'll only receive the integer part of the result.
  I'll explain this later.


## Conditional
these operators will return true|false, like other languages

```
integer $x = 5;
integer $y = 3;
boolean #result;



##greater than
#result = $x > $y;
##results to true

##less than
#result = $x < $y;
##results to false

##less or equals
#result = $x <= $y;
##results to false

##greater or equals
#result = $x >= $y;
##results to true

##equals
#result = $x == $y;
##results to false

##not equals
#result = $x != $y;
##results to true
```

Any errors talk with the dev or make a issue ;)


### Bitwise
C'mooooon! you'll not resists for these bitwise operators :D
They can be used for both bits and expressions.

```
``
study logic operations for this
``
integer $bit1 = 1;
integer $bit2 = 0;
boolean #result;

##and operation
#result = $bit1 & $bit2;
##results to false

##or operation
#result = $bit1 | $bit2;
##results to true

##not operation (*1)
#result = !$bit1;
##results to false
#result = !$bit2;
##results to true

##xor operation
#result = $bit1 ^ $bit2
##results to true

``
wanna use the not variants of these operators? agroup it in a expression and use the not operator on it, example
``
#result = !($bit1 ^ $bit2);
##results to false
```

notes:
  1: it will be more adapttative. defaultly, it will return your type equivalent, example:
  ```
integer $value = !1;
##results to 0
boolean $otherValue = !1;
##results to false
```

