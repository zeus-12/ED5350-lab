# ord() function converts a single Unicode character into its integer representation
# chr() function converts a Unicode code character into the corresponding string.

integer_rep = ord('a')
string = chr(integer_rep)

print(f'{integer_rep} is the integer representation of character a')
print(f'{string} is the corresponding string for unicode {integer_rep}')