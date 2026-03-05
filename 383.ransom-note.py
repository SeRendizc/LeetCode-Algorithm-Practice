#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30204
#
# [383] 赎金信
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # return Counter(ransomNote) <= Counter(magazine)

        ranson_l = list(ransomNote)
        magazin_l = list(magazine)

        for i in range(len(ranson_l)):
            if ranson_l[i] not in magazin_l: return False
            else: magazin_l.remove(ranson_l[i])

        return True
# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#

