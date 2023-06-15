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

  2: it throws syntax error in situations that not're expected to this happen;

  3: it cannot declare variable in a function scope;

  4: currently it not have a target-language to transpile. suggestions are accepted ^-^;

  Currently, it are the errors that I can remember now. You found more errors? talk with the dev (the same person that is writting this README)
