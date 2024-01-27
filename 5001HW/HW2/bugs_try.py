#Instruction: Give codes causing four bugs and comments on them
#1. ZeroDivisionError: Second operand of division or modulus operation is zero.
>>> print(1/0) 
# Division by zero is undefined in mathematics, and division by zero in Python is illegal.

#2. SyntaxError: A syntax error is a common error that the interpreter can detect when attempting to translate a Python statement into machine language.
>>> y = 5
>>> x = y + 2
>>> y + 2 = x
# The syntax of Python doesn't allow an expression like y + 2 to appear on the left side of the assignment operartor.

#3. IndexError: A sequence (list, string, tuple) index is out of range.
>>> seq = [2, 5, 11]
>>> print(seq[3])
#'3' is out of range of the list'seq' index, which induces an IndexError

#4. NameError: Specified local or global name does not exists
>>> print(x)
# x is not defined previously, which induces a NameError.