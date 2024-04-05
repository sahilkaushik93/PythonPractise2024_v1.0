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

# Approach1: BRUTE FORCE --> O(n)
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

    # This is causing the actual O(n) complexity
    def getMin(self) -> int:
        return min(self.array)

# Approach2: MultiStack --> O(1)
class MinStack:

    def __init__(self):
        self.array = []
        self.min = []

    def push(self, val: int) -> None:
        self.array.append(val)

        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.array[-1]:
            self.min.pop()
        self.array.pop()

    def top(self):
        return self.array[-1]

    def getMin(self):
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.pop()
param_2 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_2)
print(param_3)
print(param_4)
print(obj.array)
