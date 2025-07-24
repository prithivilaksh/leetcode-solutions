# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
#         mp=defaultdict(int)
#         for word in words: mp[word]+=1

#         n,w,l=len(s),len(words),len(words[0])
#         res=[]

#         for i in range(n-(l*w)+1):
#             j,cnt=i,0
#             imp=copy.copy(mp)
#             while imp[s[j:j+l]]!=0:
#                 imp[s[j:j+l]]-=1
#                 j+=l;cnt+=1
#             if cnt==w:res.append(i)
        
#         return res

# class Solution:
#     def findSubstring(self, s, words):

#             l,res =len(words[0]), []
#             for left in range(l):
#                 cnt = collections.Counter(words)
#                 for right in range(left + l, len(s) + 1, l):
#                     word = s[right - l: right]
#                     cnt[word] -= 1
#                     while cnt[word] < 0:
#                         cnt[s[left:left + l]] += 1
#                         left += l
#                     if left + l * len(words) == right: res.append(left)
#             return res


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n,w,k=len(s),len(words),len(words[0])
        cnt,res=defaultdict(int),[]
        for word in words: cnt[word]+=1

        for l in range(k):
            icnt=copy.copy(cnt)
            for r in range(l,n-k+1,k):
                icnt[s[r:r+k]]-=1
                while icnt[s[r:r+k]]<0:
                    icnt[s[l:l+k]]+=1
                    l+=k
                if l+w*k==r+k: res.append(l)

        return res
