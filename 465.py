Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.

amt={
    0: -10+1+5=-4
    1: 10-1-5=4
    2: 5-5
}

class Solution:
    def minTransfers(self, txs: List[List[int]]) -> int:

        for u,v,x in txs:
            amt[u]-=x
            amt[v]+=x
        
        for x,v in amt.items():




    -8
    -1

    2
    3
    4

    4


    -7
    -2

    2
    3
    4

    3



    -2
    -5
    -17

    4
    4
    4
    12







    12=1100
    11=1011
       
       1000

       0111
       1100

       0100

       0011
       1100

       0000