# class Solution:
#     def maxEnvelopes(self, envs: List[List[int]]) -> int:
#         envs.sort(key = lambda x:(x[0],-x[1]))
#         lis=[]
        
#         for i,[w,h] in enumerate(envs):

#             pos=bisect_left(lis,h)
#             if pos==len(lis): lis.append(h)
#             else: lis[pos]=h
        
#         return len(lis)


class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:

        envs.sort(key=lambda x:(x[0],-x[1]))
        seq=[]
        for _,h in envs:
            pos=bisect_left(seq,h)
            if pos==len(seq): seq.append(h)
            else: seq[pos]=h
        return len(seq)














