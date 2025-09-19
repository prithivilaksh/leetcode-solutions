# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
#         h=[(-p,c) for p,c in zip(profits,capital)]
#         heapify(h)

#         while k and h:
#             tmp=[]
#             while h and h[0][1]>w: tmp.append(heappop(h))
#             if h: w+=-heappop(h)[0];k-=1
#             else: return w
#             while tmp: heappush(h,tmp.pop())
#         return w

# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
#         pc=[(p,c) for p,c in zip(profits,capital)]
#         pc.sort(key=lambda x:x[1])

#         i,n,h=0,len(pc),[]
#         for _ in range(k):
#             while i<n and pc[i][1]<=w:heappush(h,(-pc[i][0],pc[i][1]));i+=1
#             if h: w+=-heappop(h)[0]
#             else: break
#         return w


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        cp=[(c,p) for c,p in zip(capital,profits)]
        cp.sort(key=lambda x:x[0])

        i,n,h=0,len(cp),[]
        for _ in range(k):
            while i<n and cp[i][0]<=w:heappush(h,-cp[i][1]);i+=1
            if not h: break
            w+=-heappop(h)
        return w

