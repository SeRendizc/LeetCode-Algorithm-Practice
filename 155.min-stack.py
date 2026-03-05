#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MinStack:

    def __init__(self):
        self.vals = []
        self.minval = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        self.minval.append(val)
        self.minval.sort()

    def pop(self) -> None:
        if len(self.vals):
            self.minval.remove(self.vals.pop())
            self.minval.sort()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.minval[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

