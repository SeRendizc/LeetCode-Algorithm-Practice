#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        maxlen = 250
        curr = 0
        i = 0

        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        for _ in range(n): maxlen = min(maxlen, len(strs[_]))

        while curr < maxlen:
            for i in range(n):
                if strs[i][curr] != strs[0][curr]:
                    return strs[0][:curr] if curr else ''
            curr += 1
                
        return strs[0][:curr] if curr else ''
            
# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

