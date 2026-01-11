# class Node:
#     def __init__(self):
#         self.mp=defaultdict(lambda: Node())
    
# class WordDictionary:

#     def __init__(self):
#         self.root=Node()

#     def addWord(self, word: str) -> None:
#         node=self.root
#         for c in word+"#":
#             node=node.mp[c]

#     def search(self, word: str) -> bool:

#         def dfs(pos,node):
#             if pos==len(word): return '#' in node.mp
#             if word[pos]!=".":
#                 if word[pos] in node.mp: return dfs(pos+1,node.mp[word[pos]])
#                 return False

#             for c in node.mp:
#                 if dfs(pos+1,node.mp[c]): return True
#             return False
        
#         return dfs(0,self.root)


        


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)

    
class WordDictionary:

    def __init__(self):
        self.trie={}

    def addWord(self, word: str) -> None:
        node=self.trie
        for c in word+"#":
            node[c]=node.get(c,{})
            node=node[c]

    def search(self, word: str) -> bool:

        def dfs(pos,node):
            if pos==len(word): return '#' in node
            if word[pos]!=".":
                if word[pos] in node: return dfs(pos+1,node[word[pos]])
                return False

            for c in node:
                if dfs(pos+1,node[c]): return True
            return False
        
        return dfs(0,self.trie)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)