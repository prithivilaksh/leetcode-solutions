
# given 2 strings a and b, find the number of subsequence of a that are lexicographically greater than b mod 10^9+7

# x is lexicographically greater than y if
#     - x[i]>y[j] at the first position where they differ
#     - or len(x)>len(y) and y is a prefix of x



# observations:
#     - if i==m then everything before i in a was equal to b and a has ended, return 0
#     - if j==n and i!=m (y is a prefix of x) then all possible subsequences from i to m-1 whose length>=1 form lexicographically greater subsequences.
#         - assume i=5 and m-1=8 then the string will be a[5..8]
#         - possible subsequences' index are
#             -(empty)
#             -5
#             -56
#             -57
#             -58
#             -567
#             -568
#             -578
#             -5678
#             -6
#             -67
#             -68
#             -678
#             -7
#             -78
#             -8
#         -which is 2^l -1 where l is the length of a[5..8]
#     - if we include ith character
#         - if a[i]>b[j] then all possible subsequences from i+1 to m-1 whose length>=0 form lexicographically greater subsequences.
#         - if a[i]==b[j] continue finding with i+1 and j+1
#     - if we exclude ith character, find for i+1 and j

from functools import cache
def countOfLexiGreateSubSeq(a,b):

    m,n,mod=len(a),len(b),10**9+7
    @cache
    def helper(i,j):
        if i==m: return 0
        if j==n: return 2**(m-1-i+1)-1
        
        res=0
        if a[i]>b[j]: res=(res+2**(m-1-i-1+1))%mod
        elif a[i]==b[j]: res=(res+helper(i+1,j+1))%mod
        res=(res+helper(i+1,j))%mod
        return res

    return helper(0,0)


if __name__=="__main__":
    print(countOfLexiGreateSubSeq("ab", "a")) #2
    print(countOfLexiGreateSubSeq("aba", "ab")) #3
    print(countOfLexiGreateSubSeq("bab", "ab")) #5
    print(countOfLexiGreateSubSeq("abc", "ac")) #3
    print(countOfLexiGreateSubSeq("aaaa", "aa")) #5