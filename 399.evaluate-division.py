#
# @lc app=leetcode.cn id=399 lang=python3
# @lcpr version=30204
#
# [399] 除法求值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构建图：graph[a] = [(b, a/b的值), ...]
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))
        
        def dfs(start, end, visited):
            # 从 start 到 end 的 DFS，返回路径乘积
            # 起点等于终点
            if start == end and start in graph:
                return 1.0
            # 起点不在图中
            if start not in graph:
                return -1.0
            
            visited.add(start)
            # 遍历所有邻居
            for neighbor, val in graph[start]:
                if neighbor not in visited:
                    # 递归找邻居到终点的路径
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return val * res
            
            return -1.0
        
        # 处理每个查询
        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        
        return ans
# @lc code=end



#
# @lcpr case=start
# [["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["b","c"],["bc","cd"]]\n[1.5,2.5,5.0]\n[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"]]\n[0.5]\n[["a","b"],["b","a"],["a","c"],["x","y"]]\n
# @lcpr case=end

#

