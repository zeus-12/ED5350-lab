# operator precedence

print("() - Parenthesis\n** - Exponent\n+x - Unary Plus, -x - Unary Minus, ~x - Bitwise NOT\n* - Multiplication, / - Division, // - Floor Division, % - Modulus\n+ - Addition, - - Subtraction, << >> - Bitwise Shift Operators\n& - Bitwise AND\n^ - Bitwise XOR\n| - Bitwise OR\n==, !=, >, >=, <, <=, is, is not, in, not in - Comparisons, Identity, Membership Operators\nnot - Logical NOT\nand - Logical AND\nor - Logical OR")


# testing
equation = 5 * 6 - 8 /4
# applying operator precedence  - PEMDAS
# 5 * 6 - 8 /4 
# 5 * 6 - 2.0
# 30 -2.0
# 28.0
print("\n",equation == 28.0)

#Hence proved.
