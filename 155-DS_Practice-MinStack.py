'''
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

## BRUTE FORCE --> O(1)
class MinStack:

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        return self.array.append(val)

    def pop(self) -> None:
        return self.array.pop()

    def top(self) -> int:
        if self.array != []:
            return self.array[-1]

    def getMin(self) -> int:
        return min(self.array)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
print(obj.array)
