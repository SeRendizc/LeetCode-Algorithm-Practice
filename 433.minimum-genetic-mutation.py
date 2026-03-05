#
# @lc app=leetcode.cn id=433 lang=python3
# @lcpr version=30204
#
# [433] 最小基因变化
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque, defaultdict
        
        if endGene not in bank:
            return -1
        
        # 构建模式字典
        pattern_dict = defaultdict(list)
        for gene in bank:
            for i in range(len(gene)):
                pattern = gene[:i] + '*' + gene[i + 1:]
                pattern_dict[pattern].append(gene)

        # BFS
        queue = deque([(startGene, 0)])  # 初始步数为0
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()
            
            if gene == endGene:
                return steps
            
            for i in range(len(gene)):
                pattern = gene[:i] + '*' + gene[i + 1:]
                
                if pattern in pattern_dict:
                    for next_gene in pattern_dict[pattern]:
                        if next_gene not in visited:
                            visited.add(next_gene)
                            queue.append((next_gene, steps + 1))
        
        return -1
# @lc code=end



#
# @lcpr case=start
# "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AAAAACCC"\n"AACCCCCC"\n["AAAACCCC","AAACCCCC","AACCCCCC"]\n
# @lcpr case=end

#

