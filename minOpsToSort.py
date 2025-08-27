
# given a permutation of array of int from 1 to n.

# The following 2 operations are possible
# 1) move 1st element to the last
# 2) reverse the array

# return min operations to make the array sorted like [1,2,3,4,5..]


# eg1:
# ip: [3, 4, 5, 6, 1, 2]
# reverse [2, 1, 6, 5, 4, 3]
# left rotate [1, 6, 5, 4, 3, 2]
# left rotate [6, 5, 4, 3, 2, 1]
# reverse [1, 2, 3, 4, 5, 6]
# op: 4

# eg2
# ip: [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# reverse [2, 1, 10, 9, 8, 7, 6, 5, 4, 3]
# left rotate [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
# left rotate [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# reverse [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# op: 4

# eg3
# ip: [2, 3, 1]
# left rotate [3, 1, 2]
# left rotate [1, 2, 3]
# op: 2

# eg4
# ip: [2, 3, 4, 5, 6, 1]
# reverse [1, 6, 5, 4, 3, 2]
# left rotate [6, 5, 4, 3, 2, 1]
# reverse [1, 2, 3, 4, 5, 6]
# op: 3




# observation:
#     - let p1 be position of 1 and pn be position of n
#     - if p1==0 and pn==n-1 then return 0 // sorted and ascending
#     - if pn==0 and p1==n-1 then return 1 // sorted and descending
#     - if p1<pn Descending order
#         eg [2, 1, 8, 7, 6, 5, 4, 3],  [6, 5, 4, 3, 2, 1, 8, 7]
#         res=min(pn+1,n-pn+1)
#     - else pn<p1 Ascending order
#         eg [3, 4, 5, 6, 7, 8, 1, 2],  [7, 8, 1, 2, 3, 4, 5, 6] 
#         res=min(p1,n-p1+2)

def minOpsToSort(arr):
    n=len(arr)
    p1,pn=arr.index(1),arr.index(n)
    if p1==0 and pn==n-1: return 0
    if pn==0 and p1==n-1: return 1
    if p1<pn: return min(pn+1,n-pn+1)
    else: return min(p1,n-p1+2)


if __name__=='__main__':
    print(minOpsToSort([3, 4, 5, 6, 1, 2]))
    print(minOpsToSort([3, 4, 5, 6, 7, 8, 9, 10, 1, 2]))
    print(minOpsToSort([2, 3, 1]))
    print(minOpsToSort([2, 3, 4, 5, 6, 1]))
    print(minOpsToSort([2, 1, 8, 7, 6, 5, 4, 3]))
    print(minOpsToSort([6, 5, 4, 3, 2, 1, 8, 7])) 
    print(minOpsToSort([3, 4, 5, 6, 7, 8, 1, 2]))
    print(minOpsToSort([7, 8, 1, 2, 3, 4, 5, 6])) 



    