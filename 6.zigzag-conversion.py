#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        rows = [[] for _ in range(numRows)]
        curr_row = 0
        going_down = False

        for c in s:
            rows[curr_row].append(c)
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        return ''.join(''.join(row) for row in rows)
        
        
        # if numRows == 1: return s
                
        # n = len(s)
        # scale = 2 * (numRows - 1)
        # group = n // scale + 1
        # seq = [[0 for _ in range(scale)] for _ in range(group)]  # seq[几组][几号]
        # ans = []
        # cnt = 0

        # for i in range(group):
        #     for j in range(scale):
        #         if cnt >= n: break
        #         seq[i][j] = s[cnt]
        #         cnt += 1
        
        # for l in range(group): 
        #     if seq[l][0]: ans.append(seq[l][0])

        # if numRows == 2:
        #     for l in range(group):
        #         if seq[l][1]: ans.append(seq[l][1])
        #     return "".join(ans)
        
        # for row in range(1, numRows - 1):    
        #     for l in range(group):
        #         if seq[l][row]: ans.append(seq[l][row])
        #         if seq[l][scale - row]: ans.append(seq[l][scale - row])

        # for l in range(group):
        #     if seq[l][numRows - 1]: ans.append(seq[l][numRows - 1])

        # return ''.join(ans)
        
        # 1 --> (2 -> 0) --> (3 -> 7) --> (4 -> 6) --> 5
        # 1 --> (2 -> 0) --> (3->n-3) ---> (i -> (n - i)) ---> n
# @lc code=end



#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#

