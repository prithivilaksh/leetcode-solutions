class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        
        def Node():
            return defaultdict(lambda: Node())

        trie=Node()

        def add(word):
            node=trie
            for c in word:
                node[c]["cnt"]=node[c].get("cnt",0)+1
                node=node[c]
        
        def get(word):
            node,tot=trie,0
            for c in word:
                tot+=node[c]["cnt"]
                node=node[c]    
            return tot
        
        for word in words: add(word)

        return [get(word) for word in words]

# TODO better solution