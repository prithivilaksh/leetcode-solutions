
# given a string s, find the maximum number of operations which can be done
# operation: if s[i]==s[i+1] and s[i+1]!=s[i+2], replace s[i+2] with s[i]

def findMaxOpsMS(s):

    n,res=len(s),0
    for i in range(n-3,-1,-1):
        if s[i]==s[i+1] and s[i+1]!=s[i+2]:
            res+=(n-1)-(i+2)+1
    return res


if __name__=="__main__":
    print(findMaxOpsMS("aabbcd"))
    print(findMaxOpsMS("aabba"))