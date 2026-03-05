# @lcpr-before-debug-begin
from python3problem134 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30204
#
# [134] 加油站
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        total_cost = 0
        charge = [0] * (n + 1)
        for _ in range(n):
            total_gas += gas[_]
            total_cost += cost[_]
            charge[_] = gas[_] - cost[_]
        if total_cost > total_gas: return -1

        start = 0
        tank = 0
        while start < n:
            flag = False
            for i in range(start, n):
                tank += charge[i]
                if tank < 0:
                    start = i + 1
                    tank = 0
                    flag = True
                    break
            for i in range(start + 1):
                if flag:
                    flag = False
                    break
                if i == start:
                    return start
                tank += charge[i]
                if tank < 0:
                    start = i + 1
                    tank = 0
                    break
        return -1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#

