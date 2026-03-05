#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#

from typing import List


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    alphabets = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        path = []
        n = len(digits)

        def traceback(curr: int) -> None:
            if curr == n:
                ans.append(''.join(path))
                return
            for i in self.alphabets[digits[curr]]:
                path.append(i)
                traceback(curr + 1)
                path.pop()
            curr += 1

        traceback(0)
        return ans
        
        
        
        
        
        # if not digits:
        #     return []

        # ans: List[str] = []
        # path: List[str] = []

        # def backtrack(index: int) -> None:
        #     if index == len(digits):
        #         ans.append(''.join(path))
        #         return

        #     for ch in self.alphabets[digits[index]]:
        #         path.append(ch)
        #         backtrack(index + 1)
        #         path.pop()

        # backtrack(0)
        # return ans

# @lc code=end



#
# @lcpr case=start
# "23"\n


# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

