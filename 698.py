class Solution:
    def canPartitionKSubsets(self, sticks: List[int], k: int) -> bool:
        
        if k==1: return True
        tot=sum(sticks)
        if tot%k!=0: return False
        tot,n=tot//k,len(sticks)
        sticks.sort(reverse=True)
        if sticks[0]>tot: return False

        def bt(pos,rem,tar):
            if tar==0: pos,rem,tar=0,rem-1,tot
            if rem==1: return True
            for i in range(pos,n):
                if i>pos and sticks[i-1]==sticks[i]: continue
                if sticks[i]<0 or sticks[i]>tar: continue
                sticks[i]=-sticks[i]
                if bt(i+1,rem,tar+sticks[i]): return True
                sticks[i]=-sticks[i]
                if tar==tot or tar==sticks[i]: return False
            return False
        
        return bt(0,k,tot)



