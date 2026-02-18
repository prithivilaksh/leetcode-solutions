# class Solution:
#     def isScramble(self, s1: str, s2: str) -> bool:
        
#         cnt=defaultdict(int)
#         for a,b in zip(s1,s2):
#             cnt[a]+=1;cnt[b]-=1
        
#         for v in cnt.values():
#             if v!=0: return False
        
#         del cnt

#         @cache
#         def dp(s1,s2):
#             if s1==s2: return True

#             n,match=len(s1),0
#             cnt=defaultdict(int)
#             for i in range(n-1):
#                 j=n-1-i
#                 if cnt[s1[i]]<0: match+=1
#                 cnt[s1[i]]+=1
#                 if cnt[s2[j]]>0: match+=1
#                 cnt[s2[j]]-=1

#                 if match==i+1:
#                     if dp(s1[:i+1],s2[-(i+1):]) and dp(s1[i+1:],s2[:j]): 
#                         return True

#             cnt.clear()
#             match=0
#             for i in range(n-1):
#                 j=i
#                 if cnt[s1[i]]<0: match+=1
#                 cnt[s1[i]]+=1
#                 if cnt[s2[j]]>0: match+=1
#                 cnt[s2[j]]-=1

#                 if match==i+1:
#                     if dp(s1[:i+1],s2[:i+1]) and dp(s1[i+1:],s2[i+1:]): 
#                         return True
            
#             return False
        
#         return dp(s1,s2)
                

# class Solution:
#     def isScramble(self, s1: str, s2: str) -> bool:

#         @cache
#         def dp(s1,s2):
#             if s1==s2: return True

#             n,match=len(s1),0
#             cnt=defaultdict(int)
#             for i in range(n-1):
#                 j=n-1-i
#                 if cnt[s1[i]]<0: match+=1
#                 cnt[s1[i]]+=1
#                 if cnt[s2[j]]>0: match+=1
#                 cnt[s2[j]]-=1

#                 if match==i+1:
#                     if dp(s1[:i+1],s2[-(i+1):]) and dp(s1[i+1:],s2[:j]): 
#                         return True

#             cnt.clear()
#             match=0
#             for i in range(n-1):
#                 j=i
#                 if cnt[s1[i]]<0: match+=1
#                 cnt[s1[i]]+=1
#                 if cnt[s2[j]]>0: match+=1
#                 cnt[s2[j]]-=1

#                 if match==i+1:
#                     if dp(s1[:i+1],s2[:i+1]) and dp(s1[i+1:],s2[i+1:]): 
#                         return True
            
#             return False
        
#         return dp(s1,s2)
                

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if Counter(s1)!=Counter(s2): return False
        def check_match(s1,s2):
            n,match=len(s1),0
            cnt=defaultdict(int)
            for i in range(n-1):
                if cnt[s1[i]]<0: match+=1
                cnt[s1[i]]+=1
                if cnt[s2[i]]>0: match+=1
                cnt[s2[i]]-=1
                if match==i+1 and dp(s1[:i+1],s2[:i+1]) and dp(s1[i+1:],s2[i+1:]): return True
            return False

        @cache
        def dp(s1,s2):
            if s1==s2: return True
            return check_match(s1,s2) or check_match(s1,s2[::-1])
        
        return dp(s1,s2)
                




        



        