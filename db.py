# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from bisect import bisect_right
def solution(arr):
    # Implement your solution here
    mod=10**9
    n=len(arr)

    sarr=sorted(set(arr))

    rank={val:i+1 for i,val in enumerate(sarr)}
    m=len(sarr)

    bcl,bsl=[0]*(m+1),[0]*(m+1)
    bcr,bsr=[0]*(m+1),[0]*(m+1)

    def update(bit,idx,val):
        while idx<=m:
            # print(idx)
            bit[idx]+=val
            idx+=idx&(-idx)
    
    def query(bit,idx):
        s=0
        while idx>0:
            s+=bit[idx]
            idx-=idx&(-idx)
        return s
    
    for x in arr:
        update(bcr,rank[x],1)
        update(bsr,rank[x],x)

    tot=0

    for k in range(n):
        val=arr[k]
        r=rank[val]

        update(bcr,r,-1)
        update(bsr,r,-val)

        wk=val

        lcl=query(bcl,r-1)
        lsl=query(bsl,r-1)
        wk+=lsl+(k-lcl)*val


        limr=val-1

        if limr>0:
            idxlimr=bisect_right(sarr,limr)
            lcr=query(bcr,idxlimr)
            lsr=query(bsr,idxlimr)
            hcr=(n-1-k)-lcr
            wk+=lsr+hcr*limr

        tot=(tot+wk)%mod

        update(bcl,r,1)
        update(bsl,r,val)
    return tot


