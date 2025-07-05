class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:

        n = len(words)
        lr,rl,ans = [0] * n,[0] * n,[]

        if n == 1:
            return [0]
            
        def lcp(s, t):
            n = min(len(s), len(t))
            i = 0
            while i < n and s[i]==t[i]: i+=1
            return i
        
        for i in range(1, n):
            lr[i] = max(lr[i-1], lcp(words[i], words[i-1]))
            
        for i in range(n-2, -1, -1):
            rl[i] = max(rl[i+1], lcp(words[i], words[i+1]))

        
        for i in range(n):
            if i==0:
                ans.append(rl[i+1])
                continue
                
            if i==n-1:
                ans.append(lr[i-1])
                continue

            ans.append(max(lr[i-1], rl[i+1], lcp(words[i-1], words[i+1])))

        return ans
                
            