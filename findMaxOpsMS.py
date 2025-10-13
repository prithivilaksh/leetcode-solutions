
# given a string s, find the maximum number of operations which can be done
# operation: if s[i]==s[i+1] and s[i+1]!=s[i+2], replace s[i+2] with s[i]

#wrong
# def findMaxOpsMS(s):

#     n,res=len(s),0
#     for i in range(n-3,-1,-1):
#         if s[i]==s[i+1] and s[i+1]!=s[i+2]:
#             res+=(n-1)-(i+2)+1
#     return res


# if __name__=="__main__":
#     print(findMaxOpsMS("aabbcd"))
#     print(findMaxOpsMS("aabba"))


# from collections import defaultdict
# def getMaximumOperations(s):
#     # Write your code here
#     n=len(s)
#     s=" "+s
#     s=list(s)
#     end=n+1
#     res=0
#     dp=[defaultdict(int) for _ in range(n+1)]
    
#     for i in range(1,n+1):
#         for k in dp[i-1]: dp[i][k]=dp[i-1][k]
#         dp[i][s[i]]+=1

#     r=n
#     while r>=1:
#         l=r
#         while l>1 and s[l-1]==s[l]: l-=1
#         if l!=r:
#             if end!=n+1 and s[end]==s[l]: res+=end - r - 1 - (dp[end-1][s[l]] - dp[r][s[l]])
#             else : res+=n-r - (dp[end-1][s[l]] - dp[r][s[l]])
#             end=l
#         r=l-1
#     return res

# def getMaximumOperations(s):

#     res = cnt = 0
#     prev = d = None
#     for curr in s:
#         if curr == d:
#             res += cnt-1
#         else:
#             res += cnt
#             if curr == prev:
#                 cnt += 1
#                 d = curr
#         prev = curr
#     return res

def getMaximumOperations(s):

    n = len(s)
    s += '#'
    pre_c = '#'
    ans = idx = 0

    while idx < n: 
        if s[idx] == pre_c:
            ans -= 1
            
        elif s[idx] == s[idx + 1]:
            ans += n - idx - 2
            pre_c = s[idx]
            idx += 1
        
        idx += 1
    return ans

if __name__ == '__main__':
    print(getMaximumOperations("aabaab"))
    print(getMaximumOperations("aabbcd"))
    print(getMaximumOperations("aabba"))
