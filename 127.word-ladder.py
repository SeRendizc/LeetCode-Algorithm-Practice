#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30204
#
# [127] 单词接龙
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque, defaultdict
        
        # 如果 endWord 不在列表中，直接返回 0
        if endWord not in wordList:
            return 0
        
        # 构建模式字典：pattern -> [words]
        # 例如 "hot" 生成 "*ot", "h*t", "ho*"
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])  # (当前单词, 到达步数)
        visited = {beginWord}
        
        while queue:
            word, steps = queue.popleft()
            
            # 如果找到了 endWord
            if word == endWord:
                return steps
            
            # 生成当前单词的所有模式
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                
                # 找出所有共享该模式的单词
                if pattern in pattern_dict:
                    for next_word in pattern_dict[pattern]:
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, steps + 1))
        
        return 0  # 无法到达 endWord
# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

