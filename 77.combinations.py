#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30204
#
# [77] 组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(start):
            if len(path) == k:
                ans.append(path[:])
                return
            toCount = n - k + len(path) + 1
            for i in range(start, toCount + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()
        
        dfs(1)
        return ans





















        # def dfs(start: int) -> None:
        #     if len(path) == k:
        #         ans.append(path[:])
        #         return

        #     need = k - len(path)
        #     upper = n - need + 1
        #     for num in range(start, upper + 1):
        #         path.append(num)
        #         dfs(num + 1)
        #         path.pop()

        # dfs(1)
        # return ans
# @lc code=end



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

