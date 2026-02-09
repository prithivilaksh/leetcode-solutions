class Solution:
    def findMinDifference(self, tps: List[str]) -> int:
        ntp=[]
        for tp in tps:
            tp=tp.split(":")
            ntp.append(int(tp[0])*60+int(tp[1]))
        
        ntp.sort()
        res=ntp[0]-ntp[-1]+24*60
        for i in range(len(tps)-1):
            res=min(res,ntp[i+1]-ntp[i])
        
        return res


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        s=set()
        for t in timePoints:
            tmp=t.split(":")
            m=60*(int(tmp[0])) + int(tmp[1])
            print(m)
            if m in s:
                return 0
            else:
                s.add(m)
        
        l=list(s)
        l.sort()

        l.append(l[0]+60*24)

        ans=6000
        for i in range(len(l)-1):
            ans=min(ans, l[i+1]-l[i])
        
        return ans
        