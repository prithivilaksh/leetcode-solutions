# class Solution:
#     def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        
#         left=defaultdict(list)
#         for a,b in cp: left[max(a,b)].append(min(a,b))

#         res,window,extra=0,[0,0],[0]*(n+1)
#         for r in range(1,n+1):
            
#             for l in left[r]:
#                 if l>window[1]: window=[window[1],l]
#                 elif l>window[0]: window=[l,window[1]]
            
#             res+=r-window[1]
#             extra[window[1]]+=window[1]-window[0]
        
#         return res+max(extra)

class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        
        
        # idea/observation:
        # 1) given n -> 1 2 3 ... n
        # 2) conflicting pairs -> resultant sub arrays should not have both the pairs
        # 3) if cp=[3,5] in 1 2 3 4 5 6 7
        #    possible sub arrays include
        #    1
        #    1 2, 2
        #    1 2 3, 2 3, 3
        #    1 2 3 4, 2 3 4, 3 4, 4
        #    1 2 3 4 5, 2 3 4 5, 3 4 5, 4 5, 5
        #    1 2 3 4 5 6, 2 3 4 5 6, 3 4 5 6, 4 5 6, 5 6, 6
        #    1 2 3 4 5 6 7, 2 3 4 5 6 7, 3 4 5 6 7, 4 5 6 7, 5 6 7, 6 7, 7
        #    l ... 3 ... 5 ... r => (3-l+1)*(r-5+1) subarrays need to be excluded
        # 4) for every right maintain 2 closest left and store the contribution of the closest 1
        # 5) if a < b < c and if [a,b] are conflicting pairs, we can consider [a,c] as also conflicting pairs as any sub array containing [a,c] will also have b

        r2l=defaultdict(list)
        for a,b in cp:
            r2l[max(a,b)].append(min(a,b))
        
        win,res,con=[0,0],0,defaultdict(int)
        for r in range(1,n+1):
            for l in r2l[r]:
                if win[1]<l: win=[win[1],l]
                elif win[0]<l: win=[l,win[1]]
            res+=r-win[1]
            con[win[1]]+=win[1]-win[0]
        
        return res+max(con.values())


           















