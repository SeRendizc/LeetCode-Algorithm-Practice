# @lcpr-before-debug-begin
from python3problem380 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=380 lang=python3
# @lcpr version=30204
#
# [380] O(1) 时间插入、删除和获取随机元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import random


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.index = {}  #下标映射：len(self.val)

    def insert(self, val: int) -> bool:
        if val in self.index: return False
        self.index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index: return False
        remove_idx = self.index[val]
        supp_val = self.vals[-1]

        self.vals[remove_idx] = supp_val
        self.index[supp_val] = remove_idx

        self.vals.pop()
        del self.index[val] 
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end



# def __init__(self):
#         self.vals = []
#         self.idx = {}

#     def insert(self, val: int) -> bool:
#         if val in self.idx:
#             return False
#         self.idx[val] = len(self.vals)
#         self.vals.append(val)
#         return True

#     def remove(self, val: int) -> bool:
#         if val not in self.idx:
#             return False

#         remove_idx = self.idx[val]
#         last_val = self.vals[-1]

#         self.vals[remove_idx] = last_val
#         self.idx[last_val] = remove_idx

#         self.vals.pop()
#         del self.idx[val]
#         return True

#     def getRandom(self) -> int:
#         return random.choice(self.vals)