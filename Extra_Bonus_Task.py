"""The idea is to create a regex which matches:
1 + 2 * 3 + 1+4
1+2
3*4+5
but not
1+2+3+4*"""

# Solution 1

import re

# Regular expression pattern
pattern = r"^\d+(?:[\+\*]\d+)*$"

# List of expressions to match
expressions = ["1+2*3+1+4", "1+2", "3*4+5", "1+2+3+4*"]

# Iterate over each expression
for expression in expressions:
    # Use re.match() to check if the expression matches the pattern
    if re.match(pattern, expression):
        # If the expression matches, print "Matched" along with the expression
        print(f"Matched: {expression}")
    else:
        # If the expression does not match, print "Not matched" along with the expression
        print(f"Not matched: {expression}")

print("_____________________________________________________")

# Solution 2

import re

# Regular expression pattern
pattern = r"^\d+(?:[\+\*]\d+)*$"

# List of expressions to match
expressions = ["1+2*3+1+4", "1+2", "3*4+5", "1+2+3+4*"]

# Compile the regex pattern
regex = re.compile(pattern)

# Iterate over each expression
for expression in expressions:
    # Use regex.match() to check if the expression matches the pattern
    if regex.match(expression):
        # If the expression matches, print "Matched" along with the expression
        print(f"Matched: {expression}")
    else:
        # If the expression does not match, print "Not matched" along with the expression
        print(f"Not matched: {expression}")
