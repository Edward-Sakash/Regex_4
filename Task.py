"""make happy
Task
Make any face happy. Create a function that takes a sentence containing sad faces and turn them into happy ones! This involves changing only the mouths.
Make sure to only change the face if there are eyes before them, round(3.4) wouldn't become round)3.4) (for example).

Examples:
Sad face examples: 😦 8( x( 😭
Happy face examples: 😃 8) x) 😉

Hint:
you can use capture groups
or lookbehind assertion: research on (?<=.....)

Input / Output
make_happy("My current mood: :(")    -->    "My current mood: :)"  
make_happy("I was hungry 8(")        -->    "I was hungry 8)"  
make_happy("print('x(')")            -->    "print('x)')"  """

# Solution 1

import re

def make_happy(sentence):
    happy_sentence = re.sub(r"(?<=[:8x\(])\(", ")", sentence)
    return happy_sentence

print("make_happy(\"My current mood: :(\")    -->    \"" + make_happy("My current mood: :(") + "\"")
print("make_happy(\"I was hungry 8(\")        -->    \"" + make_happy("I was hungry 8(") + "\"")
print("make_happy(\"print('x('\")            -->    \"" + make_happy("print('x('") + "\"")

print("__________________________________________________________")

print("make_happy(\"My current mood: :(\")    -->    \"{}\"".format(make_happy("My current mood: :(")))
print("make_happy(\"I was hungry 8(\")        -->    \"{}\"".format(make_happy("I was hungry 8(")))
print("make_happy(\"print('x('\")            -->    \"{}\"".format(make_happy("print('x('")))

print("__________________________________________________________")

#Solution 2
import re

def make_happy(sentence):
    happy_sentence = re.sub(r"(:|\d|x|;)(\()", r"\1)", sentence)
    return happy_sentence

print(make_happy("My current mood: :("))    # Output: "My current mood: :)"
print(make_happy("I was hungry 8("))        # Output: "I was hungry 8)"
print(make_happy("print('x(')"))            # Output: "print('x)'"

print("__________________________________________________________")

print(f"make_happy(\"My current mood: :(\")    -->    \"{make_happy('My current mood: :(')}\"")
print(f"make_happy(\"I was hungry 8(\")        -->    \"{make_happy('I was hungry 8(')}\"")
#print(f"make_happy(\"print('x('\")            -->    \"{make_happy("print('x(')")}\"") # smthg wrong here

print("__________________________________________________________")

import re

def make_happy(sentence):
    # Use capture groups to match sad faces and replace the sad mouth with a happy mouth
    happy_sentence = re.sub(r"(:|\d|x|;)(\()", r"\1)", sentence)
    return happy_sentence

# Examples
print(make_happy("My current mood: :("))    # Output: "My current mood: :)"
print(make_happy("I was hungry 8("))        # Output: "I was hungry 8)"
print(make_happy("print('x(')"))            # Output: "print('x)'"




