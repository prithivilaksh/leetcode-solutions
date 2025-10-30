# class Solution:
#     def fullJustify(self, words: List[str], mx: int) -> List[str]:
        

#         res,cl,line=[],0,[]
#         for word in words:
#             if cl+len(word)+len(line)>mx:
#                 gaps=max(1,len(line)-1)
#                 q=(mx-cl)//gaps
#                 r=(mx-cl)%gaps
#                 ires=""
#                 for w in line:
#                     ires+=w+" "*(q+(r>0))
#                     r-=1

#                 res.append(ires[:mx])
#                 cl,line=0,[]
            
#             cl+=len(word)
#             line.append(word)

#         ires=""
#         for w in line:ires+=w+" "
#         ires+=" "*(mx-len(ires))
#         res.append(ires[:mx])
        
#         return res

class Solution:
    def fullJustify(self, words: List[str], mx: int) -> List[str]:
        

        res,cl,line=[],0,[]
        for word in words:
            if cl+len(line)+len(word)>mx:
                gaps=max(1,len(line)-1)
                q,r=divmod(mx-cl,gaps)
                ires=""
                for w in line:
                    ires+=w+" "*q
                    if r: ires+=" ";r-=1

                res.append(ires[:mx])
                cl,line=0,[]
            
            cl+=len(word)
            line.append(word)

        ires=""
        for w in line:ires+=w+" "
        ires+=" "*mx
        res.append(ires[:mx])
        return res
                