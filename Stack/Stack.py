stack=[]

stack.append(1)
stack.append(2)
stack.append(3)

top=stack.pop()

peek=stack[-1] if stack else None

print("Top element:", top)
print("Peek element:", peek)