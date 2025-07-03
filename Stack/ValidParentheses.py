# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

s=input("Enter the parentheses(without space):")

sol ={"}":"{","]":"[",")":"("}

stack=[]
flag=0

def Sol(s):
    if len(s)%2 !=0:
        return ( False)

    for ch in s:
        if ch in sol:
            if stack and stack[-1]==sol[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    if not stack:
       return True

t=Sol(s)
print(t)
