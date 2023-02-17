# Check for balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
 
# Function to check parentheses
def check(myStr):
    stack = []
    for i in range(len(myStr)):
        if myStr[i] in open_list:
            stack.append((myStr[i], i))
        elif myStr[i] in close_list:
            pos = close_list.index(myStr[i])
            if ((len(stack) > 0) and
                (open_list[pos] == stack[-1][0])):
                stack.pop()
            else:
                return i+1
    
    # print("The stack is: ", stack)
    if len(stack) == 0:
        return "Success"
    else:
        return stack[-1][1]+2
    
 
 
# Driver code
string = "{{{}}}"
print(check(string))
 
string = "h[{}{})(]"
print(check(string))
 
string = "{[}"
print(check(string))
