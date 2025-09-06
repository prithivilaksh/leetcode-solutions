# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
        
#         n2a={"2":"abc","3":"def","4":"ghi","5":"jkl",\
#             "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

#         n,res,acc=len(digits),[],[]
#         def backtrack(i):
#             if i==n: 
#                 if acc:res.append(''.join(acc))
#                 return
#             for a in n2a[digits[i]]:
#                 acc.append(a)
#                 backtrack(i+1)
#                 acc.pop()
#         backtrack(0)
#         return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n2a={"2":"abc","3":"def","4":"ghi","5":"jkl",\
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        n,res=len(digits),[]
        def backtrack(i,acc):
            if i==n: 
                if acc:res.append(acc)
                return
            for a in n2a[digits[i]]:
                backtrack(i+1,acc+a)
        backtrack(0,"")
        return res
