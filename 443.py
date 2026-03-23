# class Solution:
#     def compress(self, chars: List[str]) -> int:
        
#         l,prev,cnt=0,chars[0],1
#         for x in chars[1:]+["X"]:
#             if prev!=x:
#                 chars[l]=prev;l+=1
#                 if cnt>1: 
#                     for c in str(cnt):chars[l]=c;l+=1
#                 prev,cnt=x,1
#             else: cnt+=1
#         return l


# class Solution:
#     def compress(self, chars: List[str]) -> int:
        
#         l,prev,cnt=0,chars[0],1
#         for x in chars[1:]+["X"]:
#             if prev!=x:
#                 chars[l]=prev;l+=1
#                 if cnt>1: 
#                     cnt=str(cnt)
#                     chars[l:l+len(cnt)]=list(cnt)
#                     l+=len(cnt)
#                 prev,cnt=x,1
#             else: cnt+=1
#         return l

class Solution:
    def compress(self, s: List[str]) -> int:

        curr,cnt,pos=s[0],0,0
        for c in s+[" "]:
            if c==curr: cnt+=1
            else:
                ires=curr+("" if cnt==1 else str(cnt))
                s[pos:pos+len(ires)+1]=ires[:]
                pos+=len(ires)
                curr,cnt=c,1
        return pos






























