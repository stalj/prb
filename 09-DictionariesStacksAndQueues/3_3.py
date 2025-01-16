import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct



def brackets_ok(expression):

    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack = [] 

 
    for char in expression:
        if char in "({[": 
            stack.append(char)
        elif char in ")}]":  
            if not stack or stack.pop() != bracket_pairs[char]:
                return False  

    return len(stack) == 0 


for i, expression in enumerate([expression1, expression2, expression3], 1):
    if brackets_ok(expression):
        print(f"Expression {i}: Brackets are correct")
    else:
        print(f"Expression {i}: Brackets are NOT correct")


