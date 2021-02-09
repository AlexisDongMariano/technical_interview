# A. Loop through the input string
# B. Append items in a list/stack called 'brackets'
# C. If the current item is closing bracket, ), ], }, 
# C.1. and the stack is empty, return False
# C.2. and the top of stack is a matching open bracket, pop the top of stack
# C.3. else, push in stack
# D. after the loop ended, if the stack is empty return True, else False

def balanced_brackets(input):
    brackets = []

    for i in input:
        if (i == ')' or i == ']' or i == '}') and not brackets:
            return False
        elif i == ')' and brackets[-1] == '(':
            brackets.pop()
        elif i == ']' and brackets[-1] == '[':
            brackets.pop()
        elif i == '}' and brackets[-1] == '{':
            brackets.pop()
        else:
            brackets.append(i)

    return True if not brackets else False


input = '([])[]({})'
input2 = '([)]'
input3 = '((()'

print(balanced_brackets(input))
print(balanced_brackets(input2))
print(balanced_brackets(input3))