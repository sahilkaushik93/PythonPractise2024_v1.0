'''
Input
["MaxStack","push","push","push","getMax","pop","top","getMax"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MaxStack maxStack = new MaxStack();
maxStack.push(-2);
maxStack.push(0);
maxStack.push(-3);
maxStack.getMin(); // return -3
maxStack.pop();
maxStack.top();    // return 0
maxStack.getMin(); // return -2
'''

# Approach: MultiStack --> O(1)
class MaxStack:

    def __init__(self):
        self.array = []
        self.max = []

    def push(self, val: int) -> None:
        self.array.append(val)

        if self.max:
            if val >= self.max[-1]:
                self.max.append(val)
        else:
            self.max.append(val)

    def pop(self) -> None:
        if self.max[-1] == self.array[-1]:
            self.max.pop()
        self.array.pop()

    def top(self):
        return self.array[-1]

    def getMax(self):
        return self.max[-1]



# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.pop()
param_2 = obj.getMax()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMax()
print(param_2)
print(param_3)
print(param_4)
print(obj.array)
