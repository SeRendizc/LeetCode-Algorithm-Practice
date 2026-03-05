#
# @lc app=leetcode.cn id=211 lang=python3
# @lcpr version=30204
#
# [211] 添加与搜索单词 - 数据结构设计
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]
            
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            
            if char not in node.children:
                return False
            return dfs(index + 1, node.children[char])
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end



#
# @lcpr case=start
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"][[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]\n
# @lcpr case=end

#

