# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# class Solution:
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         def max_depth(nestedList):
#             depth = 1
#             for item in nestedList:
#                 if item.isInteger():
#                     continue
#                 depth = max(depth, max_depth(item.getList()) + 1)
#             return depth

#         def dfs(nestedList, max_depth):
#             depth_sum = 0
#             for item in nestedList:
#                 if item.isInteger():
#                     depth_sum += item.getInteger() * max_depth
#                 else:
#                     depth_sum += dfs(item.getList(), max_depth - 1)
#             return depth_sum

#         depth = max_depth(nestedList)
#         return dfs(nestedList, depth)

# ############

# class Solution: # iterative
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         if not nestedList:
#         # can remove this check, an empty list in Python is considered "falsy"
#         # and the loop will exit when it reaches the end of the list
#             return 0

#         # weighted is like previous round result
#         unweighted = weighted = 0
#         while nestedList:
#             next_level = []
#             for a in nestedList:
#                 if a.isInteger():
#                     unweighted += a.getInteger()
#                 else:
#                     next_level.extend(a.getList())
#             weighted += unweighted
#             nestedList = next_level
#         return weighted


############

class Solution: # iterative
    def depthSumInverse(self, nlist: List[NestedInteger]) -> int:
        
        res=sum=0
        while nlist:
            tmplist=[]
            for x in nlist:
                if x.isInteger():sum+=x.getInteger()
                else: tmplist.extend(x.getList())
            res+=sum
            nlist=tmplist

        return res