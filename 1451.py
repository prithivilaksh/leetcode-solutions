# class Solution:
#     def arrangeWords(self, text: str) -> str:
        
#         text=text[0].lower()+text[1:]
#         text=text.split(" ")
#         c2w=defaultdict(list)
#         for word in text: c2w[len(word)].append(word)

#         res=[]
#         for c in sorted(c2w.keys()):
#             res.extend(c2w[c])
        
#         res=" ".join(res)
#         return res[0].upper()+res[1:]
    

class Solution:
    def arrangeWords(self, text: str) -> str:
        
        text=text.split(" ")
        text[0]=text[0].lower()
        c2w=defaultdict(list)
        for word in text: c2w[len(word)].append(word)

        res=[]
        for c in sorted(c2w.keys()):
            res.extend(c2w[c])
        
        return " ".join(res).capitalize()
        