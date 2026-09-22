# class Solution:
#     def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, seconds: int) -> int:
        
#         # idea
#         # 1) different ways
#         #     possibly 2 ways
#         #     - 1:01 , 61
#         #     - 1:39, 99
#         #     - 40:39, 39:99 
#         #     - 1:60 , 2:00
#         #     - 1:61, 2:01
#         #     - 1:81, 2:21

#         #     possibly 1 way
#         #     - 1:40
#         #     - 1:59

#         #     if seconds%60 is in range 40,59 and seconds<60
#         # 2) find possible ways and calculate cost

#         def convert(m,s):
#             if m==0: return str(s)

#             res=str(m)
#             if s<10: res+="0"
#             res+=str(s)
#             return res

#         def ways(s) -> List[str]:
#             m,s=s//60,s%60
#             res=[]
#             if m>0 and s<40:
#                 m1,s1=m-1,s+60
#                 res.append(convert(m1,s1))    
#             if m<100: res.append(convert(m,s))       
#             return res

#         startAt=str(startAt)
#         def cost(s) -> int:
#             s,tot=startAt+s,0
#             for i in range(1,len(s)):
#                 if s[i-1]!=s[i]: tot+=moveCost
#                 tot+=pushCost
#             return tot

#         # 100:08
#         # 99:68
#         # for way in ways(seconds):
#         #     print(way,cost(way))
        
#         return min(cost(way) for way in ways(seconds))



# class Solution:
#     def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, seconds: int) -> int:
        
#         # idea
#         # 1) different ways
#         #     possibly 2 ways
#         #     - 1:01 , 61
#         #     - 1:39, 99
#         #     - 40:39, 39:99 
#         #     - 1:60 , 2:00
#         #     - 1:61, 2:01
#         #     - 1:81, 2:21

#         #     possibly 1 way
#         #     - 1:40
#         #     - 1:59

#         #     if seconds%60 is in range 40,59 and seconds<60
#         # 2) find possible ways and calculate cost

#         def convert(m,s):
#             return str(m*100+s)

#         def ways(s) -> List[str]:
#             m,s=s//60,s%60
#             res=[]
#             if m>0 and s<40:
#                 m1,s1=m-1,s+60
#                 res.append(convert(m1,s1))    
#             if m<100: res.append(convert(m,s))       
#             return res

#         startAt=str(startAt)
#         def cost(s) -> int:
#             s,tot=startAt+s,0
#             for i in range(1,len(s)):
#                 if s[i-1]!=s[i]: tot+=moveCost
#                 tot+=pushCost
#             return tot

#         # 100:08
#         # 99:68
#         # for way in ways(seconds):
#         #     print(way,cost(way))
        
#         return min(cost(way) for way in ways(seconds))


class Solution:

    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            if mins > 99 or secs > 99 or mins < 0: return float('inf')
            s, curr, res = str(mins * 100 + secs), str(startAt), 0
            for ch in s:
                if ch == curr: res += pushCost
                else:
                    res += (pushCost + moveCost)
                    curr = ch
            return res

        mins, secs = targetSeconds // 60, targetSeconds % 60
        return min(cost(mins, secs), cost(mins - 1, secs + 60))