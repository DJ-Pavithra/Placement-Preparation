from collections import deque
class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1

    def pop(self) :
        if self.q1:
            return self.q1.popleft()
        else:
            return None
    def top(self) :
        if self.q1:
            return self.q1[0]
        else:
            return None
    def empty(self) :
        if len(self.q1)==0:
            return True
        else:
            return False


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(f"Poped value :{param_2} ")
print(f"Top value :{param_3} ")
print(f"Is stack empty :{param_4} ")