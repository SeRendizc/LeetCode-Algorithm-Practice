# @lcpr-before-debug-begin
from python3problem20 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        lefts = ['(', '{', '[']
        rights = [')', '}', ']']
        curr = []
        if len(s) % 2: return False
        for i in range(len(s)):
            if s[i] in lefts:
                curr.append(s[i])
            else:
                for j in range(3):
                    if s[i] == rights[j]:
                        break
                if not curr or curr.pop() != lefts[j]:
                    return False
        return False if curr else True
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

