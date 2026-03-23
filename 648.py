# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
#         def ptree():
#             return defaultdict(ptree)
#         root=ptree()

#         def add(word):
#             node=root
#             for x in word:
#                 node=node[x]
#             node["#"]={}
        
#         def find(word):
#             node,res=root,""
#             for x in word+".":
#                 if "#" in node: return res
#                 if x not in node: return word
#                 node=node[x]
#                 res+=x
#             return word
            
        
#         for word in dictionary: add(word)
#         res=[find(word) for word in sentence.split(" ")]

#         return " ".join(res)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        d = []
        for i, w in enumerate(sorted(dictionary)):
            if i == 0 or (not w.startswith(d[-1])): 
                d.append(w)

        res = []
        for word in sentence.split():
            i = bisect_left(d, word)
            if i and word.startswith(d[i - 1]): res.append(d[i - 1])
            else: res.append(word)
            
        return ' '.join(res)